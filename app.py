import streamlit as st

from app_home import run_home
from app_eda import run_eda
from app_ml import run_ml
from ui_helpers import set_page_config, inject_css


def main():
    # 페이지 설정 및 공통 CSS
    set_page_config()
    inject_css()

    # 깔끔한 사이드바 헤더
    st.sidebar.markdown("""<div style='padding:10px 8px'><h2 style='margin:0'>🚗 자동차 예측</h2><p style='margin:0;color:#64748b'>데이터 분석 & 가격 예측</p></div>""", unsafe_allow_html=True)

    menu = ['Home', 'EDA', 'ML']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0]:
        run_home()
    elif choice == menu[1]:
        run_eda()
    elif choice == menu[2]:
        run_ml()


if __name__ == '__main__':
    main()

