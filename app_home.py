import streamlit as st
import pandas as pd
from ui_helpers import info_card, two_columns


def run_home():
    st.markdown("<div class='card'><div class='big-title'>자동차 데이터를 분석하고, 예측하는 앱</div><div class='subtitle'>탐색적 데이터분석과 자동차 구매 예상 금액을 예측하는 인터랙티브 앱입니다.</div></div>", unsafe_allow_html=True)

    # 데이터 요약 카드
    try:
        df = pd.read_csv('./data/Car_Purchasing_Data.csv')
        c1, c2, c3 = two_columns((3,1,2)) if False else st.columns([3,1,2])
        with c1:
            st.markdown("""<div class='card'><b>데이터셋 정보</b><div class='subtitle'>Car_Purchasing_Data.csv</div></div>""", unsafe_allow_html=True)
            st.write(f"행: {df.shape[0]}  ·  열: {df.shape[1]}")
        with c2:
            st.markdown("<div class='metric-box'><div style='font-weight:700'>Avg Price</div><div>$ {int(df['Car Purchase Amount'].mean()):,}</div></div>", unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='card'><b>출처</b><div class='subtitle'>Kaggle - Car Purchasing Dataset</div></div>", unsafe_allow_html=True)
    except Exception:
        st.info('데이터를 불러올 수 없습니다. data/Car_Purchasing_Data.csv 파일을 확인하세요.')

    st.image('./image/car.jpeg', use_column_width=True)