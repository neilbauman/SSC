import streamlit as st
import dropbox
import pandas as pd

# Dropbox API configuration
DROPBOX_ACCESS_TOKEN = "sl.BhslzSQeUA-9MywLRZK3QupDGNiwNzOCf-UowpduhfSRa-vBsIIJ6AUUVDpRUAyFnSlvyFF2ddXFYATzgmopiJub39mlc_wK5zUlh8Rprok_hxOM2EjZllb9u0Y2yVNqFt4Q8HvVSAOc"

# Connect to Dropbox
dbx = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

# Load Excel file from Dropbox
_, res = dbx.files_download("/SSCExcel.xlsx")
df = pd.read_excel(res.content, sheet_name="options", range="test")

# Display the form
options = df["test"].tolist()
selected_options = st.multiselect("Select options:", options)

# Save the form results back to the Excel file
# Write your code to save the results to the "results" sheet

# Run the Streamlit app
if __name__ == "__main__":
    st.title("Your Streamlit App")
    # Add the rest of your app code here

