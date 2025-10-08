import streamlit as st
st.title('My Certificates:')
st.write('Here are some extra certificates that I have gained:')

st.header('Kaggle Certificates')
with st.expander("Introduction to Programming"):
    st.image('certificates/Intro_to_Programming_Kaggle.png')

with st.expander('Python'):
    st.image('certificates/Python (Kaggle) - Ammara.png')

with st.expander('Data Visualistion'):
    st.image('certificates/Data_Visualization.png')
    
with st.expander('Pandas (Python)'):
    st.image('certificates/Pandas (Kaggle) -Ammara.png')

st.header('Code First Girls Certificates')

with open("certificates/Python (CFG)- Ammara Hajat.pdf", "rb") as file:
    st.download_button("Download Introduction to Python Certificate", file, "Python (CFG)- Ammara Hajat.pdf")

with open("certificates/Data_and_SQL_CFG.pdf", "rb") as file:
    st.download_button("Download Data and SQL Certificate", file, "Data_and_SQL_CFG.pdf")

with open("certificates/Javascript (CFG) - Ammara Hajat.pdf", "rb") as file:
    st.download_button("Download Introduction to JavaScript Certificate", file, "Javascript (CFG) - Ammara Hajat.pdf")

st.header('Other Certificates')

with open("certificates/Springpod Barclays Data Analytics - Ammara Hajat.pdf", "rb") as file:
    st.download_button("Download Springpod Data Analytics with Barclays Certificate", file, "Springpod Barclays Data Analytics - Ammara Hajat.pdf")
