
import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
from io import BytesIO

def handle_missing(df):
    return df.fillna(df.mean(numeric_only=True))

def remove_duplicates(df):
    return df.drop_duplicates()

def detect_outliers(df):
    numeric_cols = df.select_dtypes(include=[np.number])
    z_scores = np.abs(stats.zscore(numeric_cols, nan_policy='omit'))
    filtered_entries = (z_scores < 3).all(axis=1)
    return df[filtered_entries]

def clean_data(df):
    df = remove_duplicates(df)
    df = handle_missing(df)
    df = detect_outliers(df)
    return df

st.title("🧹 Data Cleaning Automation Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("🛠 Cleaning Options")
    if st.button("Clean Data"):
        cleaned_df = clean_data(df)
        st.success("Data cleaned successfully!")
        st.write(cleaned_df.head())

        buffer = BytesIO()
        cleaned_df.to_csv(buffer, index=False)
        buffer.seek(0)

        st.download_button("Download Cleaned CSV", buffer, file_name="cleaned_data.csv", mime="text/csv")
