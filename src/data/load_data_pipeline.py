from extract.extract import get_data
from transform.transform import transform_data
import pandas as pd
import os

def load_data():
    scraped_data = get_data()
    clean_data = transform_data(scraped_data)

    return clean_data

if __name__ == "__main__":
        if os.path.exists("./data/housing_data.csv"):
            df = pd.read_csv("./data/housing_data.csv")
            if (df.columns[0] == "Unnamed: 0"): df = df.drop(df.columns[0], axis=1)
            df = pd.concat([df, load_data()], axis=0)
            df = df.drop_duplicates(subset=["areas","bedrooms","bathrooms","parkingSpots","prices","type","streets","neighborhood"])
            df.to_csv("./data/housing_data.csv")
            
        else:
            load_data().to_csv("./data/housing_data.csv")
