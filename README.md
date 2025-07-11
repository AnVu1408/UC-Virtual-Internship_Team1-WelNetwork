
# UC-Virtual-Internship_Team1-WelNetwork

This repository contains the code and data used in the UC Virtual Internship project by **Team 1** for **Wel Network**. The project primarily focuses on analyzing communication health between electricity meters in rural areas and visualizing the results through maps and data plots.

---

## 📁 Project Structure
<pre>
UC-VIRTUAL-INTERNSHIP\_Team1-WelNetwork/
├── data/
│   ├── AP endpoint numbers.csv
│   ├── meter\_routes\_primary\_only.json
│   ├── Routing tree table .csv
│   ├── RURAL ICP with meter list.csv
├── distance/
│   └── distance.py
├── map/
│   ├── map.html
│   └── map.py
├── healthy\_comm\_plot.py
├── healthy\_comms.csv
├── healthy\_comms2.csv
├── nearest\_5\_healthy\_meters.csv
├── unhealthy\_comms.csv
├── README.md

````
</pre> 

---

## 📌 Project Description

The goal of this project is to evaluate and improve the reliability of smart meter communication within rural electricity networks. The analysis focuses on:

- Identifying meters with unhealthy communication.
- Finding the nearest 5 healthy meters for each unhealthy one.
- Visualizing communication data using plots and interactive maps.

---

## 🔍 Main Components

- **`data/`**: Raw datasets including routing tables, meter info, and communication health.
- **`distance/`**: Code to compute distances between meters.
- **`map/`**: Scripts and HTML to generate and display an interactive map.
- **`healthy_comm_plot.py`**: Visualizes healthy vs unhealthy meter communications.
- **CSV Files**:
  - `healthy_comms.csv`, `healthy_comms2.csv`: Healthy meter records.
  - `unhealthy_comms.csv`: Meters with poor communication.
  - `nearest_5_healthy_meters.csv`: Lookup of nearby healthy meters.

---

## ⚙️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/AnVu1408/UC-Virtual-Internship_Team1-WelNetwork.git
cd UC-Virtual-Internship_Team1-WelNetwork
````

### 2. Install Dependencies

If your Python scripts require libraries like `pandas`, `folium`, etc., install them using:

```bash
pip install -r requirements.txt
```

### 3. Run Distance Calculations

```bash
python distance/distance.py
```

### 4. Generate Plot

```bash
python healthy_comm_plot.py
```

---

## 🗺️ How to Run the Interactive Map

### ✅ Requirements

* Ensure `map/map.html` exists.
* Ensure the `data/` folder is in the root directory with necessary CSV/JSON files.

### ▶️ Start a Local Server

```bash
python3 -m http.server
```

This command serves the current folder on:
[http://localhost:8000](http://localhost:8000)

### 🌐 Open the Map

In your browser, navigate to:
[http://localhost:8000/map/map.html](http://localhost:8000/map/map.html)

You will see an interactive map visualizing meter health and proximity.

---

## 📊 Datasets Used

* `AP endpoint numbers.csv`
* `RURAL ICP with meter list.csv`
* `Routing tree table .csv`
* `meter_routes_primary_only.json`

---

## ✍️ Authors

**Team 1 – UC Virtual Internship**:

* Le Kha An Vu
* Najiya Pattanath Mullassery
* Hansa Yasantha

GitHub: [@AnVu1408](https://github.com/AnVu1408)

---

## 📄 License

For academic and internal use only.
All data and resources provided by **Wel Networks** for educational purposes under agreement with the **University of Canterbury**.
