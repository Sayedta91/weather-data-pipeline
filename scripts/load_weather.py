import mysql.connector
import hashlib
from dotenv import load_dotenv
import os

load_dotenv()


# Connect to mysql database
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        auth_plugin="mysql_native_password",
        use_pure=True,
    )


# Create the weather_data table if it doesn't exist
def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            time DATETIME,
            temperature FLOAT,
            precipitation FLOAT,
            city VARCHAR(50),
            unique_id CHAR(32),
            UNIQUE(unique_id)
        )
    """)


def load_data(df):
    conn = get_connection()
    cursor = conn.cursor()

    create_table(cursor)

    # SQL insert query with IGNORE to avoid duplicates based on unique_id
    insert_query = """
        INSERT IGNORE INTO weather_data
        (time, temperature, precipitation, city, unique_id)
        VALUES (%s, %s, %s, %s, %s)
    """

    data_to_insert = []

    # Loop through each row in the dataframe
    for _, row in df.iterrows():
        unique_string = f"{row['city']}_{row['time']}"
        unique_id = hashlib.md5(unique_string.encode()).hexdigest()

        # Add rows to the list for insertion
        data_to_insert.append(
            (
                row["time"].to_pydatetime(),
                float(row["temperature"]),
                float(row["precipitation"]),
                row["city"],
                unique_id,
            )
        )

    # Insert all rows at once (Executemany)
    cursor.executemany(insert_query, data_to_insert)

    conn.commit()

    cursor.close()
    conn.close()

    print(f"Inserted {len(data_to_insert)} rows")


if __name__ == "__main__":
    from extract_weather import fetch_weather
    from transform_weather import transform_weather

    raw = fetch_weather()
    df = transform_weather(raw)

    load_data(df)
