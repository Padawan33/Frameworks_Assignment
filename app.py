# Import necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# --- Part 1 & 2: Data Loading and Cleaning ---
# Load the metadata CSV file into a pandas DataFrame.
# The `st.cache_data` decorator caches the function's output to improve app performance,
# so the data is only loaded once.
@st.cache_data
def load_data():
    """Load the metadata from a CSV file."""
    df = pd.read_csv('metadata.csv')
    return df

df = load_data()

# Convert the 'publish_time' column to datetime objects and handle invalid dates.
# The `errors='coerce'` parameter turns invalid dates into `NaT` (Not a Time).
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Drop rows where the 'publish_time' is missing after the conversion.
df.dropna(subset=['publish_time'], inplace=True)

# Create a new column 'publish_year' by extracting the year from the datetime objects.
df['publish_year'] = df['publish_time'].dt.year

# --- Part 3: Data Analysis ---
# Count the number of publications for each year and sort by year.
year_counts = df['publish_year'].value_counts().sort_index()

# Find the top 10 most frequent journals in the dataset.
top_journals = df['journal'].value_counts().head(10)

# Count the number of papers for each source.
source_counts = df['source_x'].value_counts()

# Prepare text data for the word cloud by joining all non-null titles.
titles_text = " ".join(title for title in df['title'].fillna(''))
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)

# --- Part 4: Streamlit Application ---
# Set the title and a brief description for the app.
st.title("CORD-19 Data Explorer")
st.write("A simple application to explore the COVID-19 Open Research Dataset.")

# --- Visualizations ---
# 1. Plot Publications Over Time
st.header("Publications Over Time")
# Create a matplotlib figure and axes to hold the plot.
fig1, ax1 = plt.subplots(figsize=(10, 6))
# Create a bar chart using the year counts.
ax1.bar(year_counts.index, year_counts.values)
ax1.set_title('Number of Publications by Year')
ax1.set_xlabel('Publication Year')
ax1.set_ylabel('Number of Papers')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', linestyle='--')
# Display the matplotlib figure in the Streamlit app.
st.pyplot(fig1)

# 2. Plot Top Publishing Journals
st.header("Top 10 Publishing Journals")
fig2, ax2 = plt.subplots(figsize=(12, 8))
top_journals.plot(kind='barh', color='skyblue', ax=ax2)
ax2.set_title('Top 10 Publishing Journals')
ax2.set_xlabel('Number of Papers')
ax2.set_ylabel('Journal')
ax2.grid(axis='x', linestyle='--')
st.pyplot(fig2)

# 3. Plot Distribution of Papers by Source
st.header("Distribution of Papers by Source")
fig3, ax3 = plt.subplots(figsize=(10, 6))
source_counts.plot(kind='bar', color='lightcoral', ax=ax3)
ax3.set_title('Distribution of Papers by Source')
ax3.set_xlabel('Source')
ax3.set_ylabel('Number of Papers')
ax3.tick_params(axis='x', rotation=45)
ax3.grid(axis='y', linestyle='--')
st.pyplot(fig3)

# 4. Display Word Cloud
st.header("Word Cloud of Paper Titles")
st.image(wordcloud.to_array(), caption='Word Cloud', use_container_width=True)

# --- Display Raw Data ---
st.header("Raw Data Sample")
st.write("A sample of the first 10 rows of the cleaned dataset.")
# Display a sample of the DataFrame as an interactive table.
st.dataframe(df.head(10))