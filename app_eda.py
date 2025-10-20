import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from ui_helpers import two_columns


def run_eda():
    st.markdown("<div class='card'><div class='big-title'>EDA: 데이터 탐색</div><div class='subtitle'>데이터를 시각적으로 분석하고 상관관계를 확인합니다.</div></div>", unsafe_allow_html=True)

    try:
        df = pd.read_csv('./data/Car_Purchasing_Data.csv')
    except Exception:
        st.error('데이터를 불러올 수 없습니다. data/Car_Purchasing_Data.csv 파일을 확인하세요.')
        return

    left, right = two_columns((2,1))

    with left:
        radio_menu = ['데이터프레임', '기본통계']
        radio_choice = st.radio('선택하세요', radio_menu)

        if radio_choice == radio_menu[0]:
            st.dataframe(df)
        else:
            st.dataframe(df.describe())

        st.subheader('최대 / 최소값 확인')
        min_max_menu = df.columns[4:]
        select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu)
        st.info(f"{select_choice}는 {int(df[select_choice].min())}부터 {int(df[select_choice].max())}까지 있습니다")

    with right:
        st.subheader('상관관계 분석')
        multi_menu = df.columns[4:]
        columns_multi_choice = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu, default=list(multi_menu[:3]))

        if len(columns_multi_choice) >= 2:
            corr = df[columns_multi_choice].corr(numeric_only=True)
            st.dataframe(corr)

            fig, ax = plt.subplots(figsize=(4, 3))
            sb.heatmap(corr, vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidths=0.8, ax=ax)
            st.pyplot(fig)

    st.subheader('각 컬럼간의 Pair Plot')
    pair_vars = ['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount']
    # 안전하게 pairplot 그리기 (메모리 주의)
    try:
        sample = df[pair_vars].sample(n=min(300, len(df)), random_state=1)
        pair_fig = sb.pairplot(sample)
        st.pyplot(pair_fig)
    except Exception as e:
        st.warning(f'Pair plot을 그릴 수 없습니다: {e}')
        

    
    
    
    





    