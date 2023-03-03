# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:32:53 2022

@author: Benk
"""
import pandas as pd
import pandas_profiling
import streamlit as st
from streamlit_pandas_profiling import st_profile_report


# pip list --format=freeze
#C:\Users\Benk\Desktop\PowerBi\Personal Key Indicators of Heart 
# streamlit run CKD-Profiling.py
st.sidebar.header('Exploratory Data Analysis APP ')

st.sidebar.image("profilingPicture.png", use_column_width=True)



option=st.sidebar.selectbox('Choose a dataset:',
     (' ','Load a dataset','Use example dataset' ))

if option=='Load a dataset': 
    uploaded_file=st.sidebar.file_uploader("Upload a dataset (CSV file)", type=['csv'] , accept_multiple_files=False, key=None,help=None ,
                               on_change=None, args=None, kwargs=None, disabled=False)
    if uploaded_file is not None:
         df = pd.read_csv(uploaded_file)
         pr = df.profile_report()
         st.header('**Dataset:**')
         st.write(df)
         if st.sidebar.button('Generate Report'):
            st.write('---')
            st.header('**Pandas Profiling Report**')
            st_profile_report(pr)
    
         

if option=='Use example dataset': 
    option=st.sidebar.selectbox('Try a preloaded dataset:',
     ('Diabetes dataset','Chronic Kidney Disease Dataset' ))
    if option=='Diabetes dataset': 
        df=pd.read_csv('diabetes.csv')
        pr = df.profile_report()
        st.header('**Dataset:**')
        st.write(df)
        if st.sidebar.button('Generate Report'):
            st.write('---')
            st.header('**Pandas Profiling Report**')
            st_profile_report(pr)
    
    if option=='Chronic Kidney Disease Dataset': 
        df=pd.read_csv('kidney_disease.csv')
        pr = df.profile_report()
        st.header('**Dataset:**')
        st.write(df)
        if st.sidebar.button('Generate Report'):
            st.write('---')
            st.header('**Pandas Profiling Report**')
            st_profile_report(pr)

st.sidebar.write("""
         ######  This app uses Pandas_Profiling and Streamlit to automate data profiling and exploratory data analysis. It's easy to use and can help streamline your work. [LinkedIn](https://www.linkedin.com/in/lamisghoualmi/), [Github](https://lamisghoualmi.github.io/)
         """)

st.sidebar.write("""
         ######                                             By Lamis Ghoualmi
         """)         





    
         


            
