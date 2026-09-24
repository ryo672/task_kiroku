import streamlit as st
import gspread

# ▼gspread接続（毎回開き直すと重いので、Streamlitのキャッシュで1回だけ実行）
@st.cache_resource
def get_sheet():
    gc = gspread.service_account(filename="task-kiroku-key.json")
    return gc.open_by_key("1ExDZNC88BQa7FRED-7IB_bAju3cYA1agUWHbnscv9YQ").sheet1

sheet = get_sheet()

# ▼入力欄
task = st.text_input("")

# ▼完了ボタン → スプレッドシートに追記
if st.button("完了"):
    sheet.append_row([task])

# ▼累計カウント表示
count = len(sheet.col_values(1))
st.write(f"登った階段数：{count}")

# ▼記録ボタン → 集計表示
kirok = {}
if st.button("記録"):
    for line in sheet.col_values(1):
        if line in kirok:
            kirok[line] += 1
        else:
            kirok[line] = 1
    st.write(kirok)