# UC-Virtual-Internship_Team1-WelNetwork

This repository contains the code and data used in the UC Virtual Internship project by Team 1 for Wel Network. The project primarily focuses on analyzing communication health between electricity meters in rural areas and visualizing the results through maps and data plots.

## 📁 Project Structure

UC-VIRTUAL-INTERNSHIP_Team1-WelNetwork/
├── data/
│ ├── AP endpoint numbers.csv
│ ├── meter_routes_primary_only.json
│ ├── Routing tree table .csv
│ ├── RURAL ICP with meter list.csv
├── distance/
│ └── distance.py
├── map/
│ ├── map.html
│ └── map.py
├── healthy_comm_plot.py
├── healthy_comms.csv
├── healthy_comms2.csv
├── nearest_5_healthy_meters.csv
├── unhealthy_comms.csv
├── README.md


## 📌 Project Description

The goal of this project is to evaluate and improve the reliability of smart meter communication within rural networks. We analyze both healthy and unhealthy communication patterns using provided datasets and visualize results for better decision-making support.

## 🔍 Main Components

- **data/**: Contains all relevant input datasets including routing tables, meter IDs, and communication data.
- **distance/**: Includes scripts for calculating distances between meters (e.g., `distance.py`).
- **map/**: Contains scripts and HTML for visualizing communication data on a map (e.g., `map.py`, `map.html`).
- **healthy_comm_plot.py**: Script to visualize communication data (healthy vs. unhealthy).
- **CSV files**:
  - `healthy_comms.csv`, `healthy_comms2.csv`: Records of meters with good communication.
  - `unhealthy_comms.csv`: Meters with poor or failed communication.
  - `nearest_5_healthy_meters.csv`: Reference for nearest working meters to each unhealthy one.

## ⚙️ How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AnVu1408/UC-Virtual-Internship_Team1-WelNetwork.git
   cd UC-Virtual-Internship_Team1-WelNetwork
Install dependencies (if required, e.g., pandas, folium):

bash
Copy
Edit
pip install -r requirements.txt
Run distance calculations:

bash
Copy
Edit
python distance/distance.py
Generate communication plots:

bash
Copy
Edit
python healthy_comm_plot.py
View map visualizations:

See next section for instructions.

🗺️ How to Run the Interactive Map
✅ Requirements
Ensure map.html is located in the map/ folder.

Ensure the data/ folder is at the root level and contains all necessary datasets.

▶️ Start a Local Server
To view the map in your browser, start a simple HTTP server:

bash
Copy
Edit
python3 -m http.server
This will serve files in the current directory at http://localhost:8000.

🌐 Open the Map
Once the server is running, open the following link in your browser:

bash
Copy
Edit
http://localhost:8000/map/map.html
You should now see an interactive map that visualizes meter communication health.

📊 Datasets Used
Smart meter routing and location information.

Primary meter routes and endpoint communication health.

👥 Team Members
An Vu
Hansa Aruna Yasantha
Najiya Pattanath Mullassery
Supervised under the UC Virtual Internship 

📄 License
For academic and internal use only.
All data and resources provided by Wel Networks for educational purposes under agreement with the University of Canterbury.
