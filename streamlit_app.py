import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Load Data
df = pd.read_csv('../data/metadata.csv')
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df_cleaned = df.dropna(subset=['title', 'publish_time'])

# Interactive Year Filter
year_min, year_max = int(df_cleaned['year'].min()), int(df_cleaned['year'].max())
year_range = st.slider("Select Year Range", year_min, year_max, (2020, year_max))
filtered_df = df_cleaned[df_cleaned['year'].between(year_range[0], year_range[1])]

# Publications by Year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title("Publications by Year")
st.pyplot(fig)

# Top Journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(5)
st.bar_chart(top_journals)

# Wordcloud
st.subheader("Word Cloud of Paper Titles")
text = " ".join(title for title in filtered_df['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

# Show sample data
st.subheader("Sample Data")
st.write(filtered_df.head())
