import streamlit as st
import joblib
import numpy as np
import sklearn
"""
@author: lp
"""
def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction Using ML</h2>
    </div>
    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model=joblib.load("lr_model")
    
    agg=st.slider("enter your age",18,100)
    
    gender=st.selectbox("Enter the gender",("male","female"))
    
    if gender=="male":
        gender=1
    else:
        gender=0
    bmi=st.number_input("enter the bmi value")

    childr=st.slider("Enter the no of children",0,5)
    
    smoker=st.selectbox("are you smoker ",("yes","no"))
    
    if smoker=="yes":
        smoker=1
    else:
        smoker=0
    
    reg=st.slider("enter the reagion",1,4)
    
    if st.button("predict"):
        pre= model.predict([[agg,gender,bmi,childr,smoker,reg]])
        
        st.success("Your Insurence Coste is {}".format(pre[0]))
    
    
      
if __name__ == '__main__':
    main()
    
    
"""

git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/lakshmiprasadlp/ml_modial-app.git
git push -u origin master

venv
conda create -p venv python=3.8 -y
conda activate venv\

streamlit run app.py
"""
        
    
    
