import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn2

# Data
data = {
    'No': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Judul Buku': [
        'The Roman Mythology Saga', 'Jupiter\'s Reign: A Roman Mythology Tale',
        'Mars and Venus: Love and War', 'Heroes of Rome: A Mythological Journey',
        'The Epic of Roman Gods', 'The Fall of Olympus: A Roman Myth Retold',
        'The Legend of Mars: War Chronicles', 'Venus in Rome: Tales of Love',
        'Roman Deities: Stories of the Ancient Gods', 'Mythological Heroes of the Roman Empire'
    ],
    'Jumlah Penjualan Buku': [15000, 10000, 12500, 20000, 8000, 7500, 9000, 14000, 5000, 11000],
    'Jumlah Pembeli': [14500, 9800, 12000, 19800, 7900, 7200, 8700, 13500, 4800, 10500],
    'Sentimen': [0.8, 0.1, 0.9, 0.7, 0.2, -0.3, 0.85, 0.9, 0.3, 0.75]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Jumlah Penjualan Buku'], df['Sentimen'], color='blue')
plt.xlabel('Jumlah Penjualan Buku')
plt.ylabel('Sentimen')
plt.title('Scatter Plot Jumlah Penjualan vs Sentimen')
plt.show()

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(df['No'], df['Jumlah Penjualan Buku'], marker='o', label='Jumlah Penjualan Buku')
plt.plot(df['No'], df['Jumlah Pembeli'], marker='o', label='Jumlah Pembeli')
plt.xlabel('No')
plt.ylabel('Jumlah')
plt.title('Line Plot Jumlah Penjualan dan Jumlah Pembeli')
plt.legend()
plt.show()

# Bar Plot
plt.figure(figsize=(10, 6))
sns.barplot(x='Judul Buku', y='Jumlah Penjualan Buku', data=df)
plt.xticks(rotation=90)
plt.xlabel('Judul Buku')
plt.ylabel('Jumlah Penjualan Buku')
plt.title('Bar Plot Jumlah Penjualan Buku per Judul')
plt.show()

# Point Plot
plt.figure(figsize=(10, 6))
sns.pointplot(x='No', y='Sentimen', data=df)
plt.xlabel('No')
plt.ylabel('Sentimen')
plt.title('Point Plot Sentimen per Buku')
plt.show()

# Venn Diagram
# As Venn diagrams are for two or three sets, let's create two sets: Positive Sentiment and High Sales
positive_sentiment = set(df[df['Sentimen'] > 0]['Judul Buku'])
high_sales = set(df[df['Jumlah Penjualan Buku'] > 10000]['Judul Buku'])

plt.figure(figsize=(10, 6))
venn2([positive_sentiment, high_sales], ('Positive Sentiment', 'High Sales'))
plt.title('Venn Diagram of Positive Sentiment and High Sales')
plt.show()
