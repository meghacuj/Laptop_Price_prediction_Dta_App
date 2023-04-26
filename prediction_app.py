import streamlit as st
import pandas as pd

st.title("Laptop_Price_Prediction_Data_App")

st.sidebar.subheader("Jupyter_notebook_Link")
st.sidebar.markdown("http://localhost:8888/notebooks/Data%20analysis_Innomatics_Research_labs/Laptop_prediction_model_Analysis.ipynb")


st.sidebar.header("Upload CSV")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Load the uploaded file
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)









st.header("MEGHA KUMARI")
st.write("Connect me on Linkedin")
st.write("https://www.linkedin.com/in/megha-kumari-43169b137/")

st.write("Connect me on Github")
st.write("https://github.com/meghacuj")




#Add Jupyter link notebook 
st.sidebar.header("sidebar")

st.sidebar.title("Enter laptop features")
ram_size = st.sidebar.slider("RAM Size", 2, 32, 8)
ram_type = st.sidebar.selectbox("RAM Type", ["DDR3", "DDR4"])
hdd_size = st.sidebar.slider("HDD Size (GB)", 128, 2000, 500)
ssd_size = st.sidebar.slider("SSD Size (GB)", 0, 1000, 256)
os = st.sidebar.selectbox("Operating System", ["Windows", "MacOS", "Linux"])




