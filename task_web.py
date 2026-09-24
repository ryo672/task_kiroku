
import streamlit as st
task = st.text_input("")
    
if st.button("完了"):
    with open("task.txt","a")as f:
        f.write(task+"\n")
    
count=0
with open("task.txt","r")as f:
    for line in f:
        count+=1
st.write(f"登った階段数：{count}")    

kirok={}

if st.button("記録"):
    with open("task.txt","r")as f:
        for line in f:
            if line in kirok:
                kirok[line]+=1
            else:
                kirok[line]=1
    st.write(kirok)

