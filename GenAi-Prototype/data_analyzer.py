# import packages
import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import matplotlib.pyplot as plt
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
    
    # Add Plotly sentiment breakdown visualization
    if "SENTIMENT_SCORE" in st.session_state["df"].columns:
        st.subheader(f"📊 Plotly Chart - Sentiment Distribution for {product}")
        
        # Create sentiment categories based on sentiment scores
        def categorize_sentiment(score):
            if score >= 0.6:
                return "Positive"
            elif score <= 0.4:
                return "Negative"
            else:
                return "Neutral"
        
        # Apply sentiment categorization to filtered data
        filtered_df_with_sentiment = filtered_df.copy()
        filtered_df_with_sentiment["Sentiment_Category"] = filtered_df_with_sentiment["SENTIMENT_SCORE"].apply(categorize_sentiment)
        
        # Create Plotly bar chart for sentiment distribution using filtered data
        sentiment_counts = filtered_df_with_sentiment["Sentiment_Category"].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']

        # Define custom order and colors
        sentiment_order = ['Negative', 'Neutral', 'Positive']
        sentiment_colors = {'Negative': 'red', 'Neutral': 'lightgray', 'Positive': 'green'}
        
        # Only include sentiment categories that actually exist in the data
        existing_sentiments = sentiment_counts['Sentiment'].unique()
        filtered_order = [s for s in sentiment_order if s in existing_sentiments]
        filtered_colors = {s: sentiment_colors[s] for s in existing_sentiments if s in sentiment_colors}
        
        # Reorder the data according to our custom order (only for existing sentiments)
        sentiment_counts['Sentiment'] = pd.Categorical(sentiment_counts['Sentiment'], categories=filtered_order, ordered=True)
        sentiment_counts = sentiment_counts.sort_values('Sentiment')
        
        fig = px.bar(
            sentiment_counts,
            x="Sentiment",
            y="Count",
            title=f"Distribution of Sentiment Classifications - {product}",
            labels={"Sentiment": "Sentiment Category", "Count": "Number of Reviews"},
            color="Sentiment",
            color_discrete_map=filtered_colors
        )
        fig.update_layout(
            xaxis_title="Sentiment Category",
            yaxis_title="Number of Reviews",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Add Altair sentiment score distribution histogram
        st.subheader(f"📈 Altair Chart - Sentiment Score Distribution for {product}")
        
        # Create Altair histogram using add_params instead of add_selection
        interval = alt.selection_interval()
        histogram_chart = alt.Chart(filtered_df).mark_bar().add_params(
            interval
        ).encode(
            alt.X("SENTIMENT_SCORE:Q", bin=alt.Bin(maxbins=10), title="Sentiment Score"),
            alt.Y("count():Q", title="Frequency"),
            tooltip=["count():Q"]
        ).properties(
            width=600,
            height=400,
            title=f"Distribution of Sentiment Scores - {product}"
        )
        st.altair_chart(histogram_chart, use_container_width=True)
        
        # Add variety of additional chart examples for training purposes
        st.subheader(f"🎯 Chart Variety Examples for {product}")
        
        # Create tabs for different chart types
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Plotly Scatter", "Altair Line", "Plotly Box", "Altair Heatmap", "Matplotlib Pyplot", "Streamlit Scatter"])
        
        with tab1:
            st.write("**Plotly Scatter Plot - Product vs Sentiment Score**")
            # Create a copy of filtered_df and add normalized size column
            scatter_df = filtered_df.copy()
            # Transform sentiment scores to positive values for size (min value becomes 1, max becomes proportional)
            min_sentiment = scatter_df["SENTIMENT_SCORE"].min()
            max_sentiment = scatter_df["SENTIMENT_SCORE"].max()
            # Normalize to range [1, 20] for better visualization
            scatter_df["size_normalized"] = ((scatter_df["SENTIMENT_SCORE"] - min_sentiment) / 
                                           (max_sentiment - min_sentiment) * 19 + 1)
            
            scatter_fig = px.scatter(
                scatter_df, 
                x="PRODUCT", 
                y="SENTIMENT_SCORE",
                color="SENTIMENT_SCORE",
                size="size_normalized",
                title=f"Product Sentiment Scatter Plot - {product}",
                color_continuous_scale="RdYlGn",
                hover_data=["SENTIMENT_SCORE"]
            )
            scatter_fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(scatter_fig, use_container_width=True)
        
        with tab2:
            st.write("**Altair Line Chart - Sentiment Trend by Index**")
            # Add index for trend visualization
            filtered_df_with_index = filtered_df.reset_index()
            line_chart = alt.Chart(filtered_df_with_index).mark_line(point=True).encode(
                x=alt.X('index:O', title='Review Index'),
                y=alt.Y('SENTIMENT_SCORE:Q', title='Sentiment Score'),
                tooltip=['index:O', 'SENTIMENT_SCORE:Q', 'PRODUCT:N']
            ).properties(
                width=600,
                height=300,
                title=f"Sentiment Score Trend - {product}"
            )
            st.altair_chart(line_chart, use_container_width=True)
        
        with tab3:
            st.write("**Plotly Box Plot - Sentiment Distribution by Product**")
            # Use the full dataset for box plot to show distribution across products
            box_fig = px.box(
                st.session_state["df"] if product == "All Products" else filtered_df,
                x="PRODUCT",
                y="SENTIMENT_SCORE",
                title=f"Sentiment Score Distribution Box Plot - {product}",
                color="PRODUCT"
            )
            box_fig.update_layout(xaxis_tickangle=-45, showlegend=False)
            st.plotly_chart(box_fig, use_container_width=True)
        
        with tab4:
            st.write("**Altair Heatmap - Product Sentiment Matrix**")
            # Create binned sentiment scores for heatmap
            filtered_df_heatmap = filtered_df.copy()
            filtered_df_heatmap['Sentiment_Bin'] = pd.cut(
                filtered_df_heatmap['SENTIMENT_SCORE'], 
                bins=5, 
                labels=['Very Low', 'Low', 'Medium', 'High', 'Very High']
            )
            
            # Create aggregated data for heatmap
            heatmap_data = filtered_df_heatmap.groupby(['PRODUCT', 'Sentiment_Bin']).size().reset_index(name='Count')
            
            heatmap_chart = alt.Chart(heatmap_data).mark_rect().encode(
                x=alt.X('PRODUCT:N', title='Product'),
                y=alt.Y('Sentiment_Bin:N', title='Sentiment Level'),
                color=alt.Color('Count:Q', scale=alt.Scale(scheme='blues')),
                tooltip=['PRODUCT:N', 'Sentiment_Bin:N', 'Count:Q']
            ).properties(
                width=400,
                height=200,
                title=f"Product-Sentiment Heatmap - {product}"
            )
            st.altair_chart(heatmap_chart, use_container_width=True)
        
        with tab5:
            st.write("**Matplotlib Pyplot - Sentiment Score Histogram**")
            # Create matplotlib figure
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Create histogram
            ax.hist(filtered_df['SENTIMENT_SCORE'], bins=15, alpha=0.7, color='skyblue', edgecolor='black')
            ax.set_xlabel('Sentiment Score')
            ax.set_ylabel('Frequency')
            ax.set_title(f'Sentiment Score Distribution (Matplotlib) - {product}')
            ax.grid(True, alpha=0.3)
            
            # Add statistics text
            mean_score = filtered_df['SENTIMENT_SCORE'].mean()
            std_score = filtered_df['SENTIMENT_SCORE'].std()
            ax.axvline(mean_score, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_score:.3f}')
            ax.legend()
            
            # Display using st.pyplot()
            st.pyplot(fig)
            plt.close()  # Close figure to free memory
        
        with tab6:
            st.write("**Streamlit Native Scatter Chart**")
            # Prepare data for st.scatter_chart (needs specific format)
            scatter_data = filtered_df[['SENTIMENT_SCORE']].copy()
            scatter_data['Product_Index'] = range(len(scatter_data))
            scatter_data = scatter_data.rename(columns={'SENTIMENT_SCORE': 'Sentiment'})
            
            # Create native Streamlit scatter chart
            st.scatter_chart(
                data=scatter_data,
                x='Product_Index',
                y='Sentiment',
                size=None,  # Optional: can add size column
                color=None  # Optional: can add color column
            )
            st.caption(f"Native Streamlit scatter chart showing sentiment scores by review index for {product}")
    
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
