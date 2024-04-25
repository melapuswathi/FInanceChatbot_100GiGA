import streamlit as st
import anthropic
import clipboard

def main():
    st.title("Financial Advisor for Your Dreams")

    # Get the API key from the user
    api_key = "Your API Key here ";

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
                response = get_response(prompt, client)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
        
        # Add predefined templates
        templates = {
            "Investment advice": "What investment options do you recommend for a conservative investor?",
            "Retirement planning": "How much should I save each month to retire comfortably in 20 years?",
            "Debt management": "What is the best strategy to pay off my credit card debt?",
            "Financial goal setting": "Can you help me set financial goals for the next 5 years?",
            "Explaining finance terms": "Explain the finance term 'Net Worth' in simple language.",
            "Financial plan for career aspiration": "Provide a detailed financial plan to help me achieve my aspiration to become a doctor.",
            "Government schemes for education": "Find relevant government schemes for me as a girl living in Andhra Pradesh to help with my education fee.",
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
                    cols[1].success(f"'{template}' copied to clipboard!")

                if cols[0].button(template, key=f"template_{template}"):
                    st.session_state.messages.append({"role": "user", "content": description})
                    with st.chat_message("user"):
                        st.markdown(description)

                    with st.chat_message("assistant"):
                        response = get_response(description, client)
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})

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








 # if st.sidebar.checkbox("Show templates"):
        #     st.sidebar.header("Templates")
        #     for template, description in templates.items():
        #         st.sidebar.markdown(f"**{template}**")
        #         st.sidebar.write(description)
        #         if st.sidebar.button(f"copy", key=f"copy_{template}"):
        #             clipboard.copy(description)
        #             st.sidebar.success(f"'{template}' copied to clipboard!")

        #         if st.sidebar.button(template, key=f"template_{template}"):
        #             st.session_state.messages.append({"role": "user", "content": description})
        #             with st.chat_message("user"):
        #                 st.markdown(description)

        #             with st.chat_message("assistant"):
        #                 response = get_response(description, client)
        #                 st.markdown(response)
        #                 st.session_state.messages.append({"role": "assistant", "content": response})

# import streamlit as st
# import anthropic

# def main():
#     st.title("Financial Advisor for Your Dreams")

#     # Get the API key from the user
#     api_key = st.text_input("Enter your Anthropic API Key:", type="password")

#     if api_key:
#         # Create the Anthropic client
#         client = anthropic.Anthropic(api_key=api_key)

#         if "claude_model" not in st.session_state:
#             st.session_state["claude_model"] = "claude-3-haiku-20240307"

#         if "messages" not in st.session_state:
#             st.session_state.messages = []

#         for message in st.session_state.messages:
#             with st.chat_message(message["role"]):
#                 st.markdown(message["content"])

#         if prompt := st.chat_input("What is up?"):
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)

#             with st.chat_message("assistant"):
#                 response = get_response(prompt, client)
#                 st.markdown(response)
#                 st.session_state.messages.append({"role": "assistant", "content": response})
        
#         # Add predefined templates
#         templates = {
#             "Investment advice": "What investment options do you recommend for a conservative investor?",
#             "Retirement planning": "How much should I save each month to retire comfortably in 20 years?",
#             "Debt management": "What is the best strategy to pay off my credit card debt?",
#             "Financial goal setting": "Can you help me set financial goals for the next 5 years?"
#         }

#         if st.sidebar.checkbox("Show templates"):
#             st.sidebar.header("Templates")
#             for template, description in templates.items():
#                 st.sidebar.markdown(f"**{template}**")
#                 st.sidebar.write(description)
#                 if st.sidebar.button(template):
#                     st.session_state.messages.append({"role": "user", "content": description})
#                     with st.chat_message("user"):
#                         st.markdown(description)

#                     with st.chat_message("assistant"):
#                         response = get_response(description, client)
#                         st.markdown(response)
#                         st.session_state.messages.append({"role": "assistant", "content": response})
                
        

# def get_response(prompt, client):
#     """
#     Retrieves response from the Anthropic model based on the prompt.
#     """
#     message = client.messages.create(
#         model="claude-3-haiku-20240307",
#         max_tokens=600,
#         messages=[{"role": "user", "content": prompt}]
#     )

#     return ''.join(block.text for block in message.content)



# if __name__ == "__main__":
#     main()