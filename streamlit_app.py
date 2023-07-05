import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import os

# Google Sheets API credentials
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

google_sheets_credentials = os.getenv('GOOGLE_SHEETS_CREDENTIALS')
creds_dict = json.loads(google_sheets_credentials)
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)

client = gspread.authorize(creds)

# Google Sheets tab name
sheet_name = "responses"

# Streamlit app
st.title("Survey Form")

# Ask multiple-choice question
st.subheader("Multiple Choice Question")
mcq_options = ['Option 1', 'Option 2', 'Option 3']
mcq_response = st.selectbox("Select an option", mcq_options)

# Ask checkbox question
st.subheader("Checkbox Question")
checkbox_options = ['Option 1', 'Option 2', 'Option 3']
checkbox_response = st.multiselect("Select options", checkbox_options)

# Ask text question
st.subheader("Text Question")
text_response = st.text_input("Enter your response")

# Submit button
if st.button("Submit"):
    # Access the Google Sheet
    sheet = client.open("Survey Responses").worksheet(Target)
    
    # Append responses to the Google Sheet
    response_values = [mcq_response, checkbox_response, text_response]
    sheet.append_row(response_values)
    
    st.success("Responses submitted successfully!")

