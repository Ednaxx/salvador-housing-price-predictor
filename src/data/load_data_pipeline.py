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

            df = pd.concat([df, load_data()], axis=0)
            df = df.drop_duplicates(subset="id")
            df = df.set_index("id")

            df.to_csv("./data/housing_data.csv")
            
        else:
            df = load_data().set_index("id")
            df.to_csv("./data/housing_data.csv")
