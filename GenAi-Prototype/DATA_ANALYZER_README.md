# 📊 Customer Reviews Data Analyzer

## Overview

The `data_analyzer.py` file is a comprehensive Streamlit application that provides advanced data processing, AI-powered analysis, and multi-library visualization capabilities for customer review data. It combines traditional data analysis with cutting-edge AI sentiment analysis using Google's Gemini API, offering a complete training environment for data visualization and GenAI integration.

## What This App Does

### 🎯 Main Purpose

This application helps analyze customer review data to understand:

- Product performance based on customer sentiment (both numerical and AI-generated)
- Review patterns across different products with advanced visualizations
- Overall customer satisfaction metrics with comprehensive chart varieties
- AI-powered sentiment classification using Google Gemini
- Comparative analysis between traditional sentiment scores and AI interpretations

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
- **User sees**: Confirmation that reviews have been parsed and cleaned with loading spinner
- **Enhanced UX**: Loading indicators for better user feedback

#### 3. **🤖 Gemini AI Sentiment Analysis** ⚡

- **What it does**: Uses Google's Gemini AI to analyze sentiment of customer reviews
- **How it works**:
  - Integrates with Google Generative AI (Gemini 2.5 Flash model)
  - Processes first 10 reviews for demonstration purposes
  - Creates categorical sentiment labels (Positive, Negative, Neutral)
  - Stores results in separate AI dataset for comparison
- **User sees**:
  - "🤖 Gemini AI Sentiment Analysis" button
  - Loading spinner with progress message
  - Dedicated AI sentiment visualization chart
  - AI-analyzed dataset clearly labeled

#### 4. **Product Filtering** 🔍

- **What it does**: Allows users to filter reviews by specific products
- **How it works**: Dropdown menu with all available products plus "All Products" option
- **User sees**: Filtered dataset showing only selected product reviews
- **Enhanced**: Works with both original and AI-analyzed datasets

#### 5. **Comprehensive Data Visualization** 📊

##### **Core Visualizations**:

- **Sentiment Score Bar Chart**: Traditional Streamlit bar chart showing average sentiment by product
- **Gemini AI Results**: Interactive Plotly chart showing AI-generated sentiment distribution
- **Plotly Sentiment Distribution**: Categorical sentiment breakdown with custom colors
- **Interactive Data Table**: Displays filtered review data with dynamic dataset switching

##### **Chart Variety Training Examples** 🎯:

The app includes 6 different chart types across multiple libraries for comprehensive visualization training:

1. **Plotly Scatter Plot**: Product vs Sentiment with normalized sizing and color mapping
2. **Altair Line Chart**: Sentiment trend analysis with interactive tooltips
3. **Plotly Box Plot**: Sentiment distribution analysis with quartiles and outliers
4. **Altair Heatmap**: Product-sentiment matrix with binned sentiment levels
5. **Matplotlib Pyplot**: Professional histogram with statistical annotations and mean line
6. **Streamlit Native Scatter**: Simple, fast-rendering scatter chart

##### **Key Metrics Dashboard**:

- Total number of reviews
- Number of unique products
- Average sentiment score across all reviews

#### 6. **Multi-Library Chart Support** 📈

- **st.bar_chart()**: Native Streamlit bar charts
- **st.plotly_chart()**: Interactive Plotly visualizations
- **st.altair_chart()**: Altair/Vega-Lite charts with selections
- **st.pyplot()**: Matplotlib figures with custom styling
- **st.scatter_chart()**: Native Streamlit scatter plots
- All charts use `use_container_width=True` for responsive design

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

### Step 1: Setup and Start the Application

```bash
cd GenAi-Prototype
# Make sure your .env file contains GEMINI_API_KEY=your_api_key_here
streamlit run data_analyzer.py
```

### Step 2: Load Your Data

1. Click the **"📥 Ingest Dataset"** button
2. Wait for the success message confirming data load (shows number of reviews)

### Step 3: Clean the Data (Optional)

1. Click the **"🧹 Parse Reviews"** button
2. Watch the loading spinner as it creates cleaned versions of the review text
3. This creates a new `CLEANED_SUMMARY` column for further analysis

### Step 4: AI-Powered Sentiment Analysis (New!)

1. Click the **"🤖 Gemini AI Sentiment Analysis"** button
2. Watch as Gemini AI analyzes the first 10 reviews for demonstration
3. The app will create a separate AI-analyzed dataset with sentiment categories
4. View the dedicated **"🤖 Gemini AI Sentiment Analysis Results"** chart

### Step 5: Explore Your Data

#### **Basic Analysis**:

1. Use the **product dropdown** to filter by specific products
2. View the **data table** (automatically switches between original and AI-analyzed data)
3. Check the **sentiment score bar chart** to see which products perform best/worst
4. Review the **statistics dashboard** for overall insights

#### **Advanced Visualizations**:

Navigate through the **"🎯 Chart Variety Examples"** tabs to explore:

1. **Plotly Scatter**: Interactive scatter plot with color and size mapping
2. **Altair Line**: Trend analysis with selection intervals
3. **Plotly Box**: Distribution analysis with quartiles
4. **Altair Heatmap**: Product-sentiment correlation matrix
5. **Matplotlib Pyplot**: Statistical histogram with mean indicators
6. **Streamlit Scatter**: Native scatter chart implementation

#### **Comparative Analysis**:

- Compare traditional sentiment scores with AI-generated sentiment categories
- Filter data by product to see product-specific insights
- Use the comprehensive visualization suite for training and learning purposes

## 🔧 Technical Details

### Dependencies

#### **Core Libraries**:

- **streamlit**: Web app framework and UI components
- **pandas**: Data manipulation and analysis
- **re**: Regular expressions for text cleaning
- **os**: File path operations

#### **Visualization Libraries**:

- **plotly.express**: Interactive plotting library
- **altair**: Declarative statistical visualization library
- **matplotlib.pyplot**: Traditional plotting library

#### **AI Integration**:

- **google.generativeai**: Google Gemini API client
- **python-dotenv**: Environment variable management

### Key Functions

#### **Data Processing**:

- `get_dataset_path()`: Constructs the correct file path to the CSV
- `clean_text(text)`: Cleans and normalizes review text

#### **AI Integration**:

- `get_sentiment_with_gemini(text)`: Analyzes sentiment using Gemini AI
  - Uses Gemini 2.5 Flash model
  - Implements safety settings for content filtering
  - Returns validated sentiment categories (Positive/Negative/Neutral)
  - Includes comprehensive error handling

#### **Visualization Helpers**:

- `categorize_sentiment(score)`: Converts numerical scores to categories
- Multiple chart creation functions for different visualization types

### Session State Usage

- `st.session_state["df"]`: Stores the original loaded DataFrame
- `st.session_state["df_with_ai"]`: Stores AI-analyzed dataset (10 samples)
- Persists data across user interactions without reloading
- Enables seamless switching between original and AI-analyzed datasets

### Caching Strategy

- `@st.cache_data` decorator on `get_sentiment_with_gemini()` for performance
- Prevents redundant API calls for the same text inputs
- Improves app responsiveness during repeated analysis

## 💡 Use Cases

### Business Analysis

- **Product Performance**: Identify which products have the most negative reviews
- **Quality Issues**: Find common problems mentioned in reviews
- **Customer Satisfaction**: Track overall sentiment trends with both numerical and AI analysis
- **AI vs Traditional Comparison**: Compare AI-generated sentiment with numerical sentiment scores
- **Competitive Intelligence**: Analyze product performance across different categories

### Data Science & Training

- **Text Preprocessing**: Clean data for further analysis
- **Sentiment Analysis**: Understand customer emotions using both traditional and AI methods
- **Product Comparison**: Compare performance across product lines
- **Visualization Training**: Learn 6 different chart types across 4 visualization libraries
- **GenAI Integration**: Hands-on experience with Google Gemini API
- **Multi-modal Analysis**: Combine numerical data with AI-generated insights

### Educational Purposes

- **Streamlit Development**: Complete example of advanced Streamlit application
- **Chart Library Comparison**: Side-by-side examples of Plotly, Altair, Matplotlib, and native Streamlit
- **AI API Integration**: Real-world example of integrating GenAI into data applications
- **Session State Management**: Learn advanced Streamlit state management techniques
- **Error Handling**: Best practices for robust application development

## 🔍 Understanding the Results

### Sentiment Scores (Numerical)

- **Negative values** (e.g., -0.86): Very negative reviews
- **Values near 0**: Neutral reviews
- **Positive values**: Positive reviews
- **Range**: Typically between -1.0 and +1.0

### AI-Generated Sentiment Categories

- **Positive**: Reviews expressing satisfaction, praise, or positive experiences
- **Negative**: Reviews expressing dissatisfaction, complaints, or negative experiences
- **Neutral**: Reviews that are factual, balanced, or lack strong emotional indicators

### Chart Interpretation

#### **Traditional Charts**:

- **Lower bars** in sentiment score chart = products with more negative feedback
- **Higher bars** = products with better customer satisfaction

#### **AI Sentiment Charts**:

- **Red bars (Negative)**: Count of reviews classified as negative by Gemini AI
- **Gray bars (Neutral)**: Count of neutral reviews
- **Green bars (Positive)**: Count of positive reviews

#### **Comparative Analysis**:

- Compare numerical sentiment trends with AI categorical results
- Look for discrepancies between traditional scoring and AI interpretation
- Use both methods for comprehensive sentiment understanding

## 📁 File Structure

```
GenAi-Prototype/
├── data_analyzer.py          # Main application file (enhanced with AI & visualizations)
├── app.py                    # Basic Gemini AI example
├── customer_reviews.csv      # Data file (required)
├── DATA_ANALYZER_README.md   # This comprehensive documentation
├── requirements.txt          # Python dependencies (updated)
├── .env                      # Environment variables (GEMINI_API_KEY)
└── QUICK_SETUP_GUIDE.md     # Setup instructions
```

## 🚨 Troubleshooting

### Common Issues

#### **Data Loading**:

1. **"Dataset not found" error**: Ensure `customer_reviews.csv` is in the GenAi-Prototype folder
2. **Empty charts**: Make sure to click "Ingest Dataset" first
3. **No data showing**: Check that your CSV file has the correct column names

#### **AI Integration**:

4. **"GEMINI_API_KEY not found"**: Create a `.env` file with your Gemini API key
5. **"Gemini AI not available"**: Verify your API key is valid and has credits
6. **AI analysis fails**: Check internet connection and API quota limits
7. **Slow AI processing**: Normal behavior - processing 10 reviews takes 10-30 seconds

#### **Visualization Issues**:

8. **Charts not displaying**: Ensure all required libraries are installed
9. **Scatter plot size error**: Fixed in current version (normalizes negative values)
10. **Altair charts not interactive**: Check Altair version compatibility

### Requirements

Make sure your `requirements.txt` includes:

```
streamlit
pandas
plotly
altair
matplotlib
google-generativeai
python-dotenv
```

### Environment Setup

Create a `.env` file in the GenAi-Prototype directory:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 🎓 Learning Outcomes

After using this application, you will have hands-on experience with:

- **Streamlit Development**: Advanced UI components, session state, and caching
- **Data Visualization**: 4 different charting libraries with 6+ chart types
- **GenAI Integration**: Real-world AI API usage with Google Gemini
- **Error Handling**: Robust application development practices
- **Data Processing**: Text cleaning, sentiment analysis, and comparative analysis
- **Performance Optimization**: Caching strategies and efficient data handling

## 🚀 Next Steps

This application serves as a foundation for:

- Building more complex GenAI applications
- Learning advanced Streamlit techniques
- Exploring different visualization approaches
- Understanding AI API integration patterns
- Developing production-ready data applications

---

_This comprehensive data analyzer is part of the GenAI prototype suite and demonstrates advanced data processing capabilities alongside cutting-edge AI-powered features. It serves as both a functional application and a comprehensive training resource for modern data science and AI development._
