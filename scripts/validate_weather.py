import pandas as pd


def validate_weather(df):

    # remove nulls
    df = df.dropna()

    # Ensure types are correct
    df["temperature"] = df["temperature"].astype(float)
    df["precipitation"] = df["precipitation"].astype(float)

    # Filter out unrealistic values
    df = df[(df["temperature"] > -50) & (df["temperature"] < 60)]
    df = df[(df["precipitation"] >= 0) & (df["precipitation"] < 500)]

    return df
