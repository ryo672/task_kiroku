import streamlit as st
import gspread

@st.cache_resource
def get_sheet():
    gc = gspread.service_account_from_dict(st.secrets["gcp_service_account"])
    return gc.open_by_key("1ExDZNC88BQa7FRED-7IB_bAju3cYA1agUWHbnscv9YQ").sheet1

sheet = get_sheet()

task = st.text_input("")

if st.button("完了"):
    sheet.append_row([task])

count = len(sheet.col_values(1))
st.write(f"登った階段数：{count}")

kirok = {}
if st.button("記録"):
    for line in sheet.col_values(1):
        if line in kirok:
            kirok[line] += 1
        else:
            kirok[line] = 1
    st.write(kirok)