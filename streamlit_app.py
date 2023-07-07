import streamlit as st
import openpyxl
import dropbox

dropbox_access_token = "sl.BhslzSQeUA-9MywLRZK3QupDGNiwNzOCf-UowpduhfSRa-vBsIIJ6AUUVDpRUAyFnSlvyFF2ddXFYATzgmopiJub39mlc_wK5zUlh8Rprok_hxOM2EjZllb9u0Y2yVNqFt4Q8HvVSAOc"
dbx = dropbox.Dropbox(dropbox_access_token)

# Name of the Excel file
EXCEL_FILE_NAfile_path = "/SSCExcel.xlsx"
_, res = dbx.files_download(file_path)
content = res.content
workbook = openpyxl.load_workbook(content)

sheet_options = workbook["options"]
test_range = sheet_options["test"]
options = [cell.value for cell in test_range]


st.title("SSC Navigator")
selected_options = st.multiselect("Select options:", options)
if st.button("Submit"):
    results_sheet = workbook["results"]
    # Write the form results to the "results" sheet
    # (you need to customize this based on your form structure)
    # results_sheet.append(...)
    # Save the updated workbook and upload it back to Dropbox
    updated_content = openpyxl.writer.excel.save_virtual_workbook(workbook)
    dbx.files_upload(updated_content, file_path, mode=dropbox.files.WriteMode.overwrite)

