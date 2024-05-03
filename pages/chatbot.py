import streamlit as st
import anthropic
import clipboard

from langchain.prompts import ChatPromptTemplate
import anthropic
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores.chroma import Chroma

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
Answer the question so that it is easily understandable. The context is provided so that you can take reference from this. Please take insiration from the cotext. You can also add things that you think are helpful for girls out there. Do not mention about the context provided. Answer as you usually answer.

{context}

---

{question}
"""



def main():
    st.set_page_config(page_title="Financial Advisor for Your Dreams", page_icon=":moneybag:", layout="wide")
    st.title("Financial Advisor for Your Dreams")

    # Get the API key from the user
    api_key = "YOUR_KEY";

    if api_key:
        # Create the Anthropic client
        client = anthropic.Anthropic(api_key=api_key)

        if "claude_model" not in st.session_state:
            st.session_state["claude_model"] = "claude-3-haiku-20240307"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("What is up?"):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = query(prompt, client)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Add predefined templates
        templates = {
            "Government schemes for education": "Find relevant government schemes for me as a girl living in Andhra Pradesh to help with my education fee.",
            "Investment advice": "What investment options do you recommend for a conservative investor?",
            "Retirement planning": "How much should I save each month to retire comfortably in 20 years?",
            "Debt management": "What is the best strategy to pay off my credit card debt?",
            "Financial goal setting": "Can you help me set financial goals for the next 5 years?",
            "Explaining finance terms": "Explain the finance term 'Net Worth' in simple language.",
            "Financial plan for career aspiration": "Provide a detailed financial plan to help me achieve my aspiration to become a doctor.",
            "Personal finance management advice": "Say my monthly income is Rs 50000, my expenses like rent, food, shopping, etc., are Rs 20000, and my debt is Rs 20000. I need to save Rs 200000 this year. How can I achieve this and manage my finances wisely?"
        }

        if st.sidebar.checkbox("Show templates"):
            st.sidebar.header("Templates")
            for template, description in templates.items():
                st.sidebar.markdown(f"**{template}**")
                st.sidebar.write(description)
                cols = st.sidebar.columns([8, 2])
                # cols[0], cols[1] =  st.columns()
                if cols[1].button(f"copy", key=f"copy_{template}"):
                    clipboard.copy(description)
                    cols[1].success("copied")

                if cols[0].button(template, key=f"template_{template}"):
                    st.session_state.messages.append({"role": "user", "content": description})
                    with st.chat_message("user"):
                        st.markdown(description)

                    with st.chat_message("assistant"):
                        response = query(description, client)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})


def query(query_text, client):
    # Prepare the DB with HuggingFaceBgeEmbeddings.
    embedding_function = HuggingFaceBgeEmbeddings(model_name="BAAI/bge-small-en-v1.5", model_kwargs={'device':'cpu'}, encode_kwargs={'normalize_embeddings': True})
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_relevance_scores(query_text, k=3)
    if len(results) == 0 or results[0][1] < 0.7:
        print("direct from claude")
        answer = get_response(query_text, client)
        return answer

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print("from context")
    response = get_response(prompt, client)
    return response



def get_response(prompt, client):
    """
    Retrieves response from the Anthropic model based on the prompt.
    """
    message = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )

    return ''.join(block.text for block in message.content)

if __name__ == "__main__":
    main()
