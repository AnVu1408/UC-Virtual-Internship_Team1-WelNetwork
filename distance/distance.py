import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors

 
# Load the full dataset
df = pd.read_csv("data/RURAL ICP with meter list.csv")
 
# Filter healthy meters (Aerial Installed - Enabled)
healthy_df = df[df['Aerial_info'] == 'Aerial Installed - Enabled']
healthy_df.to_csv("healthy_comms.csv", index=False)
 
# Filter unhealthy meters (everything else)
unhealthy_df = df[df['Aerial_info'] != 'Aerial Installed - Enabled']
unhealthy_df.to_csv("unhealthy_comms.csv", index=False)

healthy_df = pd.read_csv("healthy_comms.csv")
unhealthy_df = pd.read_csv("unhealthy_comms.csv")

# Filter only aerial-enabled healthy meters
healthy_df = healthy_df[healthy_df['Aerial_info'] == 'Aerial Installed - Enabled']

# Convert lat/lon to radians for haversine distance
healthy_coords = np.radians(healthy_df[['latitude', 'longitude']])
unhealthy_coords = np.radians(unhealthy_df[['latitude', 'longitude']])

# Fit model and find nearest neighbors
nbrs = NearestNeighbors(n_neighbors=5, metric='haversine').fit(healthy_coords)
distances, indices = nbrs.kneighbors(unhealthy_coords)
distances_m = distances * 6371000  # Convert to meters

# Collect results
results = []
for i, unhealthy_row in unhealthy_df.iterrows():
    for j in range(5):
        healthy_idx = indices[i, j]
        healthy_row = healthy_df.iloc[healthy_idx]
        results.append({
            'unhealthy_meter_id': unhealthy_row['Meter identifier'],
            'unhealthy_latitude': unhealthy_row['latitude'],
            'unhealthy_longitude': unhealthy_row['longitude'],
            'healthy_meter_id': healthy_row['Meter identifier'],
            'healthy_latitude': healthy_row['latitude'],
            'healthy_longitude': healthy_row['longitude'],
            'distance_meters': round(distances_m[i, j], 2),
            'rank': j + 1
        })

nearest_df = pd.DataFrame(results)
nearest_df = nearest_df.sort_values(by=['unhealthy_meter_id', 'distance_meters'])
nearest_df.to_csv('nearest_5_healthy_meters.csv', index=False)

