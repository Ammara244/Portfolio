import streamlit as st
st.title('My Certificates:')

with st.expander("Data Overview"):
    st.image('certificates/Intro_to_Programming_Kaggle.png')

st.image('certificates/Python (Kaggle) - Ammara.png')
st.image('certificates/Data_Visualization.png')
st.image('certificates/Pandas (Kaggle) -Ammara.png')


with open("certificates/Data_and_SQL_CFG.pdf", "rb") as file:
    st.download_button("Download Certificate", file, "Data_and_SQL_CFG.pdf")
