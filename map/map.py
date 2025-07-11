import pandas as pd
import json
import os

# === File paths ===
routing_csv = os.path.join('./data/Routing tree table .csv')
ap_csv = os.path.join('./data/AP endpoint numbers.csv')
output_json = os.path.join('./data/meter_routes_primary_only.json')

# === Load CSVs ===
routing_df = pd.read_csv(routing_csv)
ap_df = pd.read_csv(ap_csv)

# === Strip and standardize column names ===
routing_df.columns = routing_df.columns.str.strip()
ap_df.columns = ap_df.columns.str.strip()

# === Rename routing table columns ===
routing_df = routing_df.rename(columns={
    'device_name': 'device',
    'hopcount': 'hopcount',
    'location_latLonPoint': 'device_point',
    'apName': 'ap_name',
    'apLatLonPoint': 'ap_point',
    'apRank': 'ap_rank'
})

# === Filter only PRIMARY routes ===
routing_df = routing_df[routing_df['ap_rank'].str.upper().str.strip() == 'PRIMARY']

# === Extract GPS coordinates from routing table ===
routing_df[['device_lat', 'device_lon']] = routing_df['device_point'].str.extract(r'(-?\d+\.\d+),\s*(-?\d+\.\d+)')
routing_df[['ap_lat', 'ap_lon']] = routing_df['ap_point'].str.extract(r'(-?\d+\.\d+),\s*(-?\d+\.\d+)')

# === Convert to float and drop rows with missing data ===
routing_df[['device_lat', 'device_lon', 'ap_lat', 'ap_lon']] = routing_df[['device_lat', 'device_lon', 'ap_lat', 'ap_lon']].astype(float)
routing_df = routing_df.dropna(subset=['device_lat', 'device_lon', 'ap_lat', 'ap_lon'])

# === Final output structure ===
output_df = routing_df[['device', 'device_lat', 'device_lon', 'ap_name', 'ap_lat', 'ap_lon', 'hopcount']]
output = output_df.to_dict(orient='records')

# === Save to JSON ===
with open(output_json, 'w') as f:
    json.dump(output, f, indent=2)

print(f"✅ Exported {len(output)} primary routes to {output_json}")
