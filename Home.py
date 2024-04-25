import streamlit as st

def main():
    st.set_page_config(page_title="Financial Advisor for Your Dreams", page_icon=":moneybag:", layout="wide")

    st.markdown("""
    <style>
    
    .container {
        max-width: 800px;
        padding: 20px;
        margin: 0 auto;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.2);
        animation: slideIn 2s ease-in-out;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
    }
    h1 {
        font-size: 36px;
        color: #333;
        margin-bottom: 20px;
        animation: fadeInUp 1s ease-in-out;
    }
    h2 {
        font-size: 24px;
        color: #333;
        margin-bottom: 10px;
        animation: fadeInUp 1s ease-in-out;
    }
    p {
        font-size: 18px;
        color: #333;
        margin-bottom: 20px;
        animation: fadeInUp 1s ease-in-out;
    }
    .button {
        background-color: #0070f3;
        color: #fff;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        cursor: pointer;
        text-decoration: none;
        display: inline-block;
        margin-top: 20px;
        padding: 10px 30px;
        transition: background-color 0.3s ease;
        animation: fadeInUp 1s ease-in-out;
    }
    .button:hover {
        background-color: #0057a1;
    }
    .button:focus {
        box-shadow: none;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    @keyframes slideIn {
        from {
            transform: translateY(50px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    @keyframes fadeInUp {
        from {
            transform: translateY(20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
    </style>
    
    <div class="container" >
        <h1>Welcome to Your Financial Advisor for Your Dreams</h1>
        <h2>Your Big Sister in the World of Finance</h2>
        <p>
            We understand that managing your finances can be overwhelming. That's why we're here to help you navigate the complex world of finance with ease and confidence.
            Our financial advisor is like your big sister, always ready to share valuable financial secrets and guide you towards achieving your financial dreams.
        </p>
        <a href="/chatbot" class="button" style="color:white">Explore the Chatbot</a>
        
    </div>
    
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
