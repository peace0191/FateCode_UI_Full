import streamlit as st
from app_ui import show_dashboard

# 페이지 설정
st.set_page_config(page_title="FateCode Dashboard", layout="wide")

# 메인 실행
if __name__ == "__main__":
    show_dashboard()
