import streamlit as st
import pandas as pd
import dropbox 

# Dropbox access token
DROPBOX_ACCESS_TOKEN = "sl.BhtrxQG9Jq4XSJAQHxPavPEIgR9vfY-pX_ix9sbVrkn4xevr3I1JIykxHFsXEJA7vgqrQeq9iZGJE-VjpQdjuUvl9WjxI3Fa80sehKTKkYot-Xn0FZPY3I6APHIlRFg1V1X2wJXafasP"

# Name of the Excel file
EXCEL_FILE_NAME = "SSCExcel.xlsx"

# Name of the worksheet containing the options
WORKSHEET_NAME = "options"

# Name of the range in the worksheet
RANGE_NAME = "test"

# Connect to Dropbox
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

# Download the Excel file
_, res = dbx.files_download("/" + EXCEL_FILE_NAME)
data = res.content

# Load the Excel file into a pandas DataFrame
df = pd.read_excel(data, sheet_name=WORKSHEET_NAME, header=None, engine="openpyxl", range=RANGE_NAME)

# Convert DataFrame to a list of options
options = df[0].tolist()

# Display the checkbox survey question form
selected_options = st.multiselect("Select options:", options)

# Show the selected options
st.write("Selected options:", selected_options)
