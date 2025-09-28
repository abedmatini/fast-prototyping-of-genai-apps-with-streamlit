# import packages
import streamlit as st
import pandas as pd
import re
import os


# Helper function to get dataset path
def get_dataset_path():
    # Get the current script directory (GenAi-Prototype folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the path to the CSV file in the same directory
    csv_path = os.path.join(current_dir, "customer_reviews.csv")
    return csv_path


# Helper function to clean text
def clean_text(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s]', '', text)
    return text


st.title("📊 Customer Reviews Data Analyzer")
st.write("This is your data processing and analysis app.")

# Layout two buttons side by side
col1, col2 = st.columns(2)

with col1:
    if st.button("📥 Ingest Dataset"):
        try:
            csv_path = get_dataset_path()
            st.session_state["df"] = pd.read_csv(csv_path)
            st.success(f"Dataset loaded successfully! ({len(st.session_state['df'])} reviews)")
        except FileNotFoundError:
            st.error("Dataset not found. Please check that customer_reviews.csv is in the GenAi-Prototype folder.")

with col2:
    if st.button("🧹 Parse Reviews"):
        if "df" in st.session_state:
            st.session_state["df"]["CLEANED_SUMMARY"] = st.session_state["df"]["SUMMARY"].apply(clean_text)
            st.success("Reviews parsed and cleaned!")
        else:
            st.warning("Please ingest the dataset first.")

# Display the dataset if it exists
if "df" in st.session_state:
    # Product filter dropdown
    st.subheader("🔍 Filter by Product")
    product = st.selectbox("Choose a product", ["All Products"] + list(st.session_state["df"]["PRODUCT"].unique()))
    st.subheader(f"📁 Reviews for {product}")

    if product != "All Products":
        filtered_df = st.session_state["df"][st.session_state["df"]["PRODUCT"] == product]
    else:
        filtered_df = st.session_state["df"]
    
    st.dataframe(filtered_df)
    
    # Add sentiment analysis visualization
    st.subheader("📈 Sentiment Score by Product")
    grouped = st.session_state["df"].groupby(["PRODUCT"])["SENTIMENT_SCORE"].mean()
    st.bar_chart(grouped)
    
    # Add some basic statistics
    st.subheader("📊 Dataset Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Reviews", len(st.session_state["df"]))
    
    with col2:
        st.metric("Products", st.session_state["df"]["PRODUCT"].nunique())
    
    with col3:
        avg_sentiment = st.session_state["df"]["SENTIMENT_SCORE"].mean()
        st.metric("Avg Sentiment", f"{avg_sentiment:.3f}")

# run the app with: streamlit run data_analyzer.py
