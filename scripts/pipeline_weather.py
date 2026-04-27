import logging
from extract_weather import fetch_weather
from transform_weather import transform_weather
from load_weather import load_data
from validate_weather import validate_weather

# Configure logging
logging.basicConfig(
    filename="weather_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def run_pipeline():
    try:
        logging.info("Starting weather pipeline.")

        # Step 1 - Extract
        logging.info("Fetching weather data.")
        raw_data = fetch_weather()

        # Step 2 - Transform
        logging.info("Transforming data.")
        df = transform_weather(raw_data)
        logging.info(f"Transformed {len(df)} records")

        # Step 3 - Validate
        logging.info("Validating data.")
        df = validate_weather(df)

        # Step 4 - Load
        logging.info("Loading data into database.")
        load_data(df)

        logging.info("Pipeline completed successfully!")

    except Exception as e:
        # Log error if something fails
        logging.error(f"Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    run_pipeline()
