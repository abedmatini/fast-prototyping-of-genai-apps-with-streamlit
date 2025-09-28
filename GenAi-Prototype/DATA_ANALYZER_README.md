# 📊 Customer Reviews Data Analyzer

## Overview

The `data_analyzer.py` file is a Streamlit application that provides data processing and analysis capabilities for customer review data. It allows users to load, clean, filter, and visualize customer feedback data in an interactive web interface.

## What This App Does

### 🎯 Main Purpose

This application helps analyze customer review data to understand:

- Product performance based on customer sentiment
- Review patterns across different products
- Overall customer satisfaction metrics

### 📋 Key Features

#### 1. **Data Ingestion** 📥

- **What it does**: Loads the `customer_reviews.csv` file into the application
- **How it works**: Reads CSV data using pandas and stores it in Streamlit's session state
- **User sees**: Success message with the number of reviews loaded
- **File location**: Looks for `customer_reviews.csv` in the same directory as the script

#### 2. **Data Cleaning** 🧹

- **What it does**: Cleans and preprocesses the review text data
- **How it works**:
  - Converts text to lowercase
  - Removes punctuation and special characters
  - Strips whitespace
  - Creates a new `CLEANED_SUMMARY` column
- **User sees**: Confirmation that reviews have been parsed and cleaned

#### 3. **Product Filtering** 🔍

- **What it does**: Allows users to filter reviews by specific products
- **How it works**: Dropdown menu with all available products plus "All Products" option
- **User sees**: Filtered dataset showing only selected product reviews

#### 4. **Data Visualization** 📈

- **Sentiment Analysis Chart**: Bar chart showing average sentiment score by product
- **Interactive Data Table**: Displays filtered review data in a sortable table
- **Key Metrics Dashboard**: Shows three important statistics:
  - Total number of reviews
  - Number of unique products
  - Average sentiment score across all reviews

## 📊 Data Structure

### Input Data (`customer_reviews.csv`)

The application expects a CSV file with these columns:

- **PRODUCT**: Name of the product being reviewed
- **DATE**: Date of the review
- **SUMMARY**: Text content of the customer review
- **SENTIMENT_SCORE**: Numerical sentiment score (negative = bad, positive = good)
- **Order ID**: Unique identifier for the order

### Example Data

```
PRODUCT,DATE,SUMMARY,SENTIMENT_SCORE,Order ID
Alpine Skis,2023-10-30,"The skis have durability issues...",-0.86290675,2031
Thermal Gloves,2023-11-10,"The waterproof gloves suffered...",-0.8224165,2029
```

## 🚀 How to Use

### Step 1: Start the Application

```bash
cd GenAi-Prototype
streamlit run data_analyzer.py
```

### Step 2: Load Your Data

1. Click the **"📥 Ingest Dataset"** button
2. Wait for the success message confirming data load

### Step 3: Clean the Data (Optional)

1. Click the **"🧹 Parse Reviews"** button
2. This creates cleaned versions of the review text

### Step 4: Explore Your Data

1. Use the **product dropdown** to filter by specific products
2. View the **data table** to see individual reviews
3. Check the **sentiment chart** to see which products perform best/worst
4. Review the **statistics dashboard** for overall insights

## 🔧 Technical Details

### Dependencies

- **streamlit**: Web app framework
- **pandas**: Data manipulation and analysis
- **re**: Regular expressions for text cleaning
- **os**: File path operations

### Key Functions

- `get_dataset_path()`: Constructs the correct file path to the CSV
- `clean_text(text)`: Cleans and normalizes review text

### Session State Usage

- `st.session_state["df"]`: Stores the loaded DataFrame
- Persists data across user interactions without reloading

## 💡 Use Cases

### Business Analysis

- **Product Performance**: Identify which products have the most negative reviews
- **Quality Issues**: Find common problems mentioned in reviews
- **Customer Satisfaction**: Track overall sentiment trends

### Data Science

- **Text Preprocessing**: Clean data for further analysis
- **Sentiment Analysis**: Understand customer emotions
- **Product Comparison**: Compare performance across product lines

## 🔍 Understanding the Results

### Sentiment Scores

- **Negative values** (e.g., -0.86): Very negative reviews
- **Values near 0**: Neutral reviews
- **Positive values**: Positive reviews

### Chart Interpretation

- **Lower bars** in sentiment chart = products with more negative feedback
- **Higher bars** = products with better customer satisfaction

## 📁 File Structure

```
GenAi-Prototype/
├── data_analyzer.py          # Main application file
├── customer_reviews.csv      # Data file (required)
├── DATA_ANALYZER_README.md   # This documentation
└── requirements.txt          # Python dependencies
```

## 🚨 Troubleshooting

### Common Issues

1. **"Dataset not found" error**: Ensure `customer_reviews.csv` is in the GenAi-Prototype folder
2. **Empty charts**: Make sure to click "Ingest Dataset" first
3. **No data showing**: Check that your CSV file has the correct column names

### Requirements

Make sure your `requirements.txt` includes:

```
pandas
streamlit
```

---

_This data analyzer is part of the GenAI prototype suite and demonstrates data processing capabilities alongside AI-powered features._
