import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def run_eda():
    # 데이터 불러오기
    df = pd.read_csv('./data/Car_Purchasing_Data.csv')

    st.text('이 데이터는 Car_Purchasing_Data.csv 데이터입니다.')

    # 데이터 보여준다
    # st.dataframe(df)

    # if st.checkbox('기본통계보기') :
    #     st.dataframe(df.describe())
    # else :
    #     pass

    radio_menu = ['데이터프레임','기본통계']
    radio_choice = st.radio('선택하세요', radio_menu)

    if radio_choice == radio_menu[0]:
        st.dataframe(df)
    elif radio_choice == radio_menu[1]:
        st.dataframe(df.describe())

    # 각 컬럼의 최대 / 최소값 확인
    # 나이대는 20살 부터 70살까지 있다
    # 연봉은 20000달러부터 100000달러까지 있다

    st.subheader('최대 / 최소값 확인')

    min_max_menu = df.columns[ 4 : ]
    select_choice = st.selectbox('컬럼을 선택하세요', min_max_menu )

    print(select_choice)

    st.info(f"{select_choice}는 { int(df[select_choice].min()) }부터 { int(df[select_choice].max()) }까지 있습니다")


    # 상관관계분석
    st.subheader('상관관계분석')
    
    multi_menu = df.columns[ 4 : ]
    colums_multi_choice = st.multiselect('컬럼을 2개 이상 선택하세요', multi_menu)
    # print(colums_multi_choice)
    
    # st.dataframe( df.corr(numeric_only=True) )

    # fig1 = plt.figure()
    # sb.heatmap(data=df.corr(numeric_only=True), vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidth=1)
    # st.pyplot(fig1) 

    if len(colums_multi_choice) >= 2 :

        st.dataframe(df[colums_multi_choice].corr(numeric_only=True))

        fig1 = plt.figure()
        sb.heatmap(data=df[colums_multi_choice].corr(numeric_only=True), vmin=-1, vmax=1, cmap='coolwarm', annot=True, fmt='.2f', linewidth=1)
        st.pyplot(fig1) 

    st.subheader('각 컬럼간의 Pair Plot')
    pair = sb.pairplot(data=df, vars=['Age', 'Annual Salary', 'Credit Card Debt', 'Net Worth', 'Car Purchase Amount'])
    st.pyplot(pair)
        

    
    
    
    





    