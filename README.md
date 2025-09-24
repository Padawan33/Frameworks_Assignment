# Frameworks_Assignment

CORD-19 Data Analysis and Visualization
This project explores a subset of the COVID-19 Open Research Dataset (CORD-19) to perform data loading, cleaning, and visualization. The analysis focuses on understanding publication trends, identifying key journals, and visualizing frequent topics in the research papers. The final output is a Python script and a simple web application built with Streamlit to display the findings.

Required Tools
To run this project, you need Python 3.7+ and the following libraries. You can install them using pip:

Bash

pip install pandas matplotlib seaborn streamlit wordcloud
Project Structure
metadata.csv: The primary dataset used for the analysis.

Assignment.py: A Python script containing all the data loading, cleaning, analysis, and visualization code. This file generates and displays the plots in separate windows.

app.py: A Streamlit web application that displays all the visualizations and a sample of the data on a single web page.

How to Run the Project
Running the Analysis Script
To run the full data analysis and see the visualizations in separate windows, execute the following command in your terminal:

Bash

python Assignment.py
Running the Web Application
To launch the Streamlit web application and view all the results in your browser, use this command in your terminal:

Bash

python -m streamlit run app.py
Keep the terminal running to keep the app accessible.

Key Findings
Publications Over Time: The analysis revealed a steady increase in publications related to the topic, with a significant spike in recent years, reflecting the global focus on infectious disease research.

Top Publishing Journals: "Journal of Virology" and "PLoS One" were identified as the leading journals with the highest number of publications in the dataset.

Common Research Topics: A word cloud of paper titles highlighted key terms such as "Respiratory," "Syndrome," "Infection," and "Virus," which are central to the research.

Data Sources: The majority of the papers in this dataset originate from the PMC and Elsevier sources.

Reflection
This assignment provided a practical experience with a full data science workflow, from raw data to a user-friendly application. A key challenge was troubleshooting the environment setup, particularly with library installations and correctly launching the Streamlit app. Learning to use plt.show() correctly and managing the Streamlit server process were valuable lessons. The project demonstrated the power of using libraries like pandas for data manipulation and Streamlit for creating interactive and shareable dashboards.