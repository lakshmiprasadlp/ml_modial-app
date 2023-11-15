import streamlit as st
import joblib
import numpy as np

def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Health Insurance Cost Prediction Using ML</h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('gd model')
    
    p1 = st.slider('Enter Your Age',18,100)
    
    s1 = st.selectbox('Sex',('Male','Female'))
    
    if s1=='Male':
        p2=1
    else:
        p2=0
        
    p3 = st.number_input("Enter Your BMI Value")
    
    
    
    p4 = st.slider("Enter Number of Children",0,4)
    
    
    s2 = st.selectbox("Smoker",("Yes","No"))
    
    
    if s2=='Yes':
        p5=1
    else:
        p5=0
        
        
    p6 = st.slider("Enter Your Region",1,4)
    
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5,p6]])
        
        st.balloons()
        st.success('Your Insurance Cost is {}'.format(round(pred[0],2)))
        
    
    
"""

git commit -m "first commit"
git branch -M master
git remote add origin https://github.com/lakshmiprasadlp/ml_modial-app.git
git push -u origin master

venv
conda create -p venv python=3.8 -y
conda activate venv\

"""
        
    
    
    
if __name__ == '__main__':
    main()