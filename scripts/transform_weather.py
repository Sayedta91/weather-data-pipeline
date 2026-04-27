import pandas as pd


def transform_weather(all_data):
    # store individual city dataframes in a list
    dfs = []

    # Loop through each city's weather data and create a dataframe
    for data in all_data:
        hourly = data["hourly"]
        city = data["city"]

        df = pd.DataFrame(
            {
                "time": hourly["time"],
                "temperature": hourly["temperature_2m"],
                "precipitation": hourly["precipitation"],
                "city": city,
            }
        )

        # Convert time column to datetime format
        df["time"] = pd.to_datetime(df["time"])

        # Append the city's dataframe to the list
        dfs.append(df)

    # Concatenate all city dataframes into a single dataframe
    final_df = pd.concat(dfs, ignore_index=True)

    return final_df


if __name__ == "__main__":
    from extract_weather import fetch_weather

    raw_data = fetch_weather()
    df = transform_weather(raw_data)

    print(df.head())
