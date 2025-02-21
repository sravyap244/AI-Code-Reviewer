import streamlit as st
import google.generativeai as ai

#set up page config
st.set_page_config(page_title="AI Code Reviewer",layout="wide")

#load api key from streamlit secrets

google_api_key=st.secrets["google_api_key"]
if not google_api_key:
    st.error("⚠️ Google API Key not found! Add it in Streamlit secrets.")
    st.stop()

# configure google gemini API

ai.configure(api_key=google_api_key)

#AI System Prompt
system_prompt="you are an AI code reviewer sharp on bugs, obsessed with optimization, and dedicated to writing clean, efficient code.You can only resolve data science related code issues." 
model=ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=system_prompt)

#streamlit UI
st.title("💬:An AI Code Reviewer")

#code input
user_prompt=st.text_area("Enter Your Python code here...:") 

#review button
st.header("Code Review")
if st.button("Review Code"):
    if user_prompt.strip():
        st.info("your code is being reviewed....")

        #ai prompt with system instructions
        prompt=system_prompt+f"\n\nHere is your code for review\n```python\n{user_prompt}\n```"

        try:
            #get ai response
            model=ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",system_instruction=system_prompt)
            response=model.generate_content(prompt)
            feedback=response.text

            st.subheader("Bug Report")
            st.markdown(f'<div class="stMarkdown">{feedback}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f'Error: {str(e)}')

    else:
        st.warning("Are you kidding, I'm missing the code here..")

# Footer
st.markdown("---")
st.write("📌 Developed by **sravya** ❤️ using Google Gemini & Streamlit")

    
             
