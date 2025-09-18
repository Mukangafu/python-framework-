import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv('../data/metadata.csv')

# Basic exploration
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Data cleaning
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year
df_cleaned = df.dropna(subset=['title', 'publish_time'])

# Publications by year
year_counts = df_cleaned['year'].value_counts().sort_index()
plt.figure(figsize=(8,4))
sns.barplot(x=year_counts.index, y=year_counts.values)
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Publications")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('../images/publications_year.png')
plt.show()

# Top Journals
top_journals = df_cleaned['journal'].value_counts().head(10)
plt.figure(figsize=(8,4))
sns.barplot(y=top_journals.index, x=top_journals.values)
plt.title("Top 10 Journals Publishing COVID-19 Papers")
plt.xlabel("Number of Publications")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig('../images/top_journals.png')
plt.show()

# Wordcloud for Titles
text = " ".join(title for title in df_cleaned['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10,5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Paper Titles")
plt.tight_layout()
plt.savefig('../images/wordcloud.png')
plt.show()
