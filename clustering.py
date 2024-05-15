import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import csv
from plate_classifier import Plate_Classifier

# Step 1: Read the CSV file into a pandas DataFrame
df = pd.read_csv("Earthquakes.csv")
f = open("cluster_assign.csv",'w')
wr = csv.writer(f)

# Step 2: Extract latitude and longitude columns
coordinates = df[['longitude', 'latitude']]

# Step 3: Perform k-means clustering
k = 100  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
df['cluster'] = kmeans.fit_predict(coordinates)
cluster_centers=kmeans.cluster_centers_
pc = Plate_Classifier()
for i in (cluster_centers):
    wr.writerow(pc.plate(i[0],i[1]))
    

# Step 4: Visualize the clustering results
plt.figure(figsize=(10, 6))
plt.scatter(df['longitude'], df['latitude'], c=df['cluster'], cmap='viridis', s=10)
plt.colorbar(label='Cluster')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('K-means Clustering with k='+str(k))
plt.show()

df.to_csv("result.csv",index=False)

f.close()