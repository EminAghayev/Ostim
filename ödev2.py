import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

df = pd.read_csv("git_commit.csv")

# ---- Analizler Başlıyor ----

# Tarihsel Commit Sayısı (Haftalık)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)
weekly_commits = df.resample('W').count()['Commit ID']

plt.figure(figsize=(10, 5))
weekly_commits.plot()
plt.title("Haftalık Commit Sayısı")
plt.xlabel("Tarih")
plt.ylabel("Commit Sayısı")
plt.grid(True)
plt.tight_layout()
plt.show()

# Geliştirici Bazlı Commit Sayısı
plt.figure(figsize=(8, 4))
sns.countplot(x='Developer', data=df.reset_index(), palette='viridis')
plt.title("Geliştirici Bazlı Commit Sayısı")
plt.xlabel("Geliştirici")
plt.ylabel("Commit Sayısı")
plt.tight_layout()
plt.show()

# Geliştirici Bazlı Eklenen/Silinen Satır Sayısı
dev_stats = df.groupby('Developer')[['Lines Added', 'Lines Deleted']].sum().sort_values(by='Lines Added', ascending=False)

dev_stats.plot(kind='bar', stacked=True, figsize=(8, 5), colormap='Set2')
plt.title("Geliştirici Bazlı Kod Değişiklikleri")
plt.ylabel("Toplam Satır")
plt.tight_layout()
plt.show()

# En Çok Değişen Dosyalar (Top 10)
top_files = df['File Changed'].value_counts().head(10)

plt.figure(figsize=(8, 4))
top_files.plot(kind='barh', color='coral')
plt.title("En Çok Değişen Dosyalar")
plt.xlabel("Değişiklik Sayısı")
plt.tight_layout()
plt.show()

# Eklenen vs Silinen Satır Scatter Plot
plt.figure(figsize=(6, 6))
sns.scatterplot(x='Lines Added', y='Lines Deleted', hue='Developer', data=df.reset_index())
plt.title("Eklenen vs. Silinen Satır")
plt.tight_layout()
plt.show()
