import numpy as np
import pandas as pd

def load_coffee_data(filename):
    # TODO
    return coffee_df

def load_weather_data(filename):
    # TODO
    return weather_df

def main():

    # Load data
    coffee_df = load_coffee_data('cafe_arabica_weekly.csv')

    # Combine the datasets on the date (Data) column
    combined_df = pd.merge(coffee_df, weather_df, on='Data', how='inner')
    # Probably


if __name__ == "__main__":
    main()


