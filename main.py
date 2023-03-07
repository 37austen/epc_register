import streamlit as st
import pandas as pd 
import numpy as np 

st.set_page_config(layout="wide")

@st.cache_data
def upload_epc_data(str):
    
    df = pd.read_csv(str,compression="zip")

#     df[['POSTCODE_SECTOR','POSTCODE_SEC_2']] = df['POSTCODE'].str.split(" ", 0, expand=True)

    return(df)


df = upload_epc_data("ezyzip.zip")

columns = list(df.columns)

with st.sidebar:
    st.write("Keyword Filters (case sensitive)")
    type = st.text_input("Property Type", "")
    area = st.text_input('Area', "")
    postcode = st.text_input('Postcode', "")

options = st.multiselect(
    'Select columns to show',
    columns,
    columns)


df = df[options]

if type is not None or  area is not None or postcode is not None:
    
    if "PROPERTY_TYPE" in options:
       
        df = df[df.PROPERTY_TYPE.str.contains(type)]
    
    if "CONSTITUENCY_LABEL" in options:
       
        df = df[df.CONSTITUENCY_LABEL.str.contains(area)]

    if "POSTCODE" in options:
    
        df = df[df.POSTCODE.str.contains(postcode)]
    

st.dataframe(df, height=500,width=3000)

st.download_button(
                label="Download",
                data=df.to_csv(index=False).encode('utf-8'),
                key = 200,
                file_name=f'EPC Download.csv',
                mime="text/csv")
