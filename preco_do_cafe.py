import os
import numpy as np
import pandas as pd


data_dir = "data"

def load_coffee_data(filename):
    """Load the coffee price data from CSV"""
    coffee_df = pd.read_csv(filename,
                            decimal=",",
                            thousands=".",
                            parse_dates=['Data'],
                            dayfirst=True)
    return coffee_df

def load_weather_data(filename):
    """Load the daily weather data from CSV"""
    daily_weather_df = pd.read_csv(filename,
                           sep=";",
                           decimal=",",
                           thousands=".",
                           skiprows=10,
                           parse_dates=['Data Medicao'],
                           dayfirst=True)
    daily_weather_df.columns = daily_weather_df.columns.str.strip()

    return daily_weather_df

def main():

    # Load coffee data
    coffee_file = "cafe_arabica_weekly.csv"
    coffee_path= os.path.join(data_dir, coffee_file)
    coffee_df = load_coffee_data(coffee_path)
    print(coffee_df.head())

    # Load weather data
    weather_file = "dados_83393_D_1970-01-01_2024-05-14.csv"
    weather_path= os.path.join(data_dir, "daily_weather", weather_file)
    weather_df = load_weather_data(weather_path)
    print(weather_df.head())




if __name__ == "__main__":
    main()


