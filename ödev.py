import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import pandas as pd
df = pd.read_csv("git_commit.csv")
# Sadece sayısal sütunlarla çalışalım
numeric_data = df[["Lines Added", "Lines Deleted"]]

# Veriyi ölçekleyelim (normalize)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# K-Means ile kümeleme (örnek olarak 3 küme)
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(scaled_data)

# Küme etiketlerini orijinal veriye ekle
df["Cluster"] = clusters

# Görselleştirme
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Lines Added", y="Lines Deleted", hue="Cluster", palette="Set1", s=60)
plt.title("Kümeleme: Lines Added vs Lines Deleted")
plt.xlabel("Lines Added")
plt.ylabel("Lines Deleted")
plt.grid(True)
plt.tight_layout()
plt.show()