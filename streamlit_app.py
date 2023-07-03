import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Authenticate and access Google Sheets
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = Credentials.from_service_account_file('~/Downloads/scc-navigator-abbfd61b15dc.json', scopes=scope)
gc = gspread.authorize(creds)

# Google Sheets Configuration
source_sheet_key = '1hs8VpTGSAmf0wEW22UxGZB61MpFjUidp3tysF3BrGwg'
target_sheet_key = '1hs8VpTGSAmf0wEW22UxGZB61MpFjUidp3tysF3BrGwg'
source_sheet = gc.open_by_key(source_sheet_key).Source
target_sheet = gc.open_by_key(target_sheet_key).Target

# Page 1: Introduction
st.title("Survey Tool")

# Page 2: Questions
st.header("Question 1")
answer_1 = st.text_input("Enter your answer")

st.header("Question 2")
answer_2 = st.radio("Choose an option", ["Option 1", "Option 2", "Option 3"])

st.header("Question 3")
answer_3 = st.checkbox("Check this box if applicable")

# Page 3: Submit
if st.button("Submit"):
    # Submit the survey results to the target Google Sheet
    target_sheet.append_row([answer_1, answer_2, answer_3])
    st.success("Survey submitted successfully!")

# Run the app
if __name__ == '__main__':
    st.set_page_config(page_title="Survey Tool", page_icon=":pencil:")
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ("Introduction", "Questions", "Submit"))
    
    if page == "Introduction":
        st.sidebar.success("Introduction")
        st.sidebar.info("Welcome to the survey!")
        st.experimental_set_query_params(page="introduction")
        st.sidebar.markdown("---")
    elif page == "Questions":
        st.sidebar.success("Questions")
        st.experimental_set_query_params(page="questions")
        st.sidebar.markdown("---")
    elif page == "Submit":
        st.sidebar.success("Submit")
        st.experimental_set_query_params(page="submit")
        st.sidebar.markdown("---")

    if page == "Introduction":
        st.title("Introduction")
        st.write("Welcome to the survey! This survey is designed to collect feedback from users.")
        st.markdown("---")
    elif page == "Questions":
        st.title("Survey Questions")
        st.write("Please answer the following questions:")
        st.markdown("---")
    elif page == "Submit":
        st.title("Submit")
