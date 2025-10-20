import streamlit as st
import joblib
import pandas as pd
from ui_helpers import two_columns


def run_ml():
    st.markdown("<div class='card'><div class='big-title'>구매 금액 예측하기</div><div class='subtitle'>아래 정보를 입력하면, 금액을 예측해 드립니다.</div></div>", unsafe_allow_html=True)

    left, right = two_columns((2,1))

    with left:
        gender_list = ['여자', '남자']
        gender = st.radio('성별을 입력하세요', gender_list, horizontal=True)
        gender_data = 0 if gender == gender_list[0] else 1

        age = st.number_input('나이를 입력하세요.', min_value=20, max_value=90, value=35)
        salary = st.number_input('연봉 입력 (달러)', min_value=10000, value=50000, step=1000)
        debt = st.number_input('카드빚 입력 (달러)', min_value=0, value=2000, step=100)
        worth = st.number_input('자산 입력 (달러)', min_value=10000, value=20000, step=1000)

        predict_btn = st.button('예측하기!')

    with right:
        st.markdown("<div class='card'><b>예측 도움말</b><div class='subtitle'>입력값에 따라 예측값이 달라집니다. 평균 연봉 대비 자산, 카드빚 비율이 중요한 요인입니다.</div></div>", unsafe_allow_html=True)

    if predict_btn:
        try:
            regressor = joblib.load('./model/regressor.pkl')
        except Exception:
            st.error('모델 파일을 불러올 수 없습니다. model/regressor.pkl 파일이 존재하는지 확인하세요.')
            return

        new_data = [{'Gender': gender_data, 'Age': age, 'Annual Salary': salary, 'Credit Card Debt': debt, 'Net Worth': worth}]
        df_new = pd.DataFrame(data=new_data)

        try:
            y_pred = regressor.predict(df_new)
        except Exception as e:
            st.error(f'예측에 실패했습니다: {e}')
            return

        if y_pred is None or len(y_pred) == 0:
            st.warning('예측값을 생성할 수 없습니다.')
            return

        price = f"{int(round(y_pred[0])):,}"
        st.success(f"예측한 금액은 {price} 달러입니다.")
        st.write('입력 요약:')
        st.json(df_new.to_dict(orient='records')[0])

    
    
