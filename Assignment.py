# Part 1: Data Loading and Basic Exploration

# Import the pandas library for data manipulation.
import pandas as pd
# Import the matplotlib library for plotting visualizations.
import matplotlib.pyplot as plt
# Import the WordCloud library for generating word clouds.
from wordcloud import WordCloud

# Load the metadata.csv file into a pandas DataFrame.
df = pd.read_csv('metadata.csv')

# Display the first 5 rows to ensure the data is loaded correctly.
print(df.head())

# Check the DataFrame dimensions (number of rows and columns).
print("\nDataFrame dimensions:", df.shape)

# Get a concise summary of the DataFrame, including data types and non-null values.
print("\nDataFrame info:")
df.info()

# Generate basic descriptive statistics for numerical columns.
print("\nBasic statistics for numerical columns:")
print(df.describe())


# Part 2: Data Cleaning and Preparation

# Convert the 'publish_time' column to a proper datetime format.
# The 'errors=coerce' argument will turn any unparseable dates into NaT (Not a Time).
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Drop any rows where the 'publish_time' is missing after the conversion.
df.dropna(subset=['publish_time'], inplace=True)

# Create a new column 'publish_year' by extracting the year from the 'publish_time' column.
df['publish_year'] = df['publish_time'].dt.year

# Display the updated DataFrame information to confirm the data type change.
print(df.info())

# Display the first few rows to show the new 'publish_year' column.
print(df.head())


# Part 3: Data Analysis and Visualization

# --- Analysis ---
# Count the number of papers published each year and sort the results.
year_counts = df['publish_year'].value_counts().sort_index()
print("\nPublications by year:")
print(year_counts)

# Identify and count the top 10 most frequent journals.
top_journals = df['journal'].value_counts().head(10)
print("\nTop 10 publishing journals:")
print(top_journals)

# Count the number of papers from each source.
source_counts = df['source_x'].value_counts()

# --- Visualizations ---
# Create a bar chart showing the number of publications over time.
plt.figure(figsize=(10, 6))
plt.bar(year_counts.index, year_counts.values)
plt.title('Number of Publications by Year')
plt.xlabel('Publication Year')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()

# Create a horizontal bar chart of the top 10 publishing journals.
plt.figure(figsize=(12, 8))
top_journals.plot(kind='barh', color='skyblue')
plt.title('Top 10 Publishing Journals')
plt.xlabel('Number of Papers')
plt.ylabel('Journal')
plt.grid(axis='x', linestyle='--')
plt.tight_layout()

# Create a single figure for the word cloud and show it.
# First, prepare a single string of all titles, filling missing values with an empty string.
titles_text = " ".join(title for title in df['title'].fillna(''))
# Generate a word cloud from the title text.
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles_text)
# Display the word cloud image.
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')

# Create a bar chart showing the distribution of papers by source.
plt.figure(figsize=(10, 6))
source_counts.plot(kind='bar', color='lightcoral')
plt.title('Distribution of Papers by Source')
plt.xlabel('Source')
plt.ylabel('Number of Papers')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()

# Show all generated plots at the end of the script.
plt.show()