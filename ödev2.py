import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from faker import Faker
import random

# Sahte veri oluştur
# fake = Faker()
# np.random.seed(42)

# # Geliştiriciler
# developers = ['Ali', 'Ayşe', 'Mehmet', 'Elif', 'Ahmet']

# # 200 commitlik veri üret
# data = []
# for _ in range(200):
#     commit_id = fake.sha1()
#     dev = random.choice(developers)
#     date = fake.date_between(start_date='-6M', end_date='today')
#     file_changed = fake.file_name(extension='py')
#     lines_added = np.random.poisson(lam=10)
#     lines_deleted = np.random.poisson(lam=5)
#     commit_msg = fake.sentence(nb_words=6)
#     data.append([commit_id, dev, date, file_changed, lines_added, lines_deleted, commit_msg])

# df = pd.DataFrame(data, columns=['Commit ID', 'Developer', 'Date', 'File Changed', 'Lines Added', 'Lines Deleted', 'Commit Message'])
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
