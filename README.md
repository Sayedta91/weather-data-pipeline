# Weather Data Pipeline (ETL)

A modular end-to-end data pipeline that ingests real-time weather data from an external API, processes it, and stores it in a structured MySQL database.
Designed to demonstrate core data engineering and data architecture concepts, including ETL pipelines, data validation, and reliable data loading.

### What this project shows
- Building a modular ETL pipeline
- Working with real-time API data
- Transforming JSON data into structured datasets
- Implementing data quality checks
- Storing and querying data in a relational database

### Pipeline Overview
- Extract: Fetches hourly weather data from Open-Meteo API
- Transform: Converts JSON into structured tabular format
- Validate: Cleans data, enforces types, filters invalid values
- Load: Inserts data into MySQL with duplicate prevention

### Data Model
| Column | Description |
| ------------- | ------------- |
| time  | Timestamp of observation  |
| city | City name  |
| temperature  | Temperature (°C) |
| precipitation  | Precipitation level  |
| unique_id  |  Hash key (city + time) to prevent duplicates  |


### Tech Stack
- Python (Pandas, Requests)
- MySQL
- SQL
- Logging
- dotenv (for secure configuration)


## How to Run
1. Install dependencies
   
pip install -r requirements.txt

2. Create a MySQL database:
``` CREATE DATABASE weather_pipeline; ```

3. Add environment variables
```
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=weather_pipeline
DB_PORT=3306
```

4. Run the pipline:
``` python scripts/pipeline_weather.py ```

### Future Improvements
- Schedule pipeline runs (Airflow)
- Store data in cloud platforms (AWS S3 / Redshift)
- Add monitoring and alerting
- Expand data sources


### Author

Tariq Sayed
Aspiring Data Architect | Data Analyst
