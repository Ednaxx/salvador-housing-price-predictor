from extract.extract import get_data
from transform.transform import transform_data
import pandas as pd

def load_data():
    scraped_data = get_data(1, 2)
    clean_data = transform_data(scraped_data)

    return clean_data

if __name__ == "__main__":
    try:
        df = pd.read_csv("./data/housing_data.csv")
        df = pd.concat([df, load_data()], axis=0)
        df = df.drop_duplicates(subset="id")
    except:
        df = load_data()
    
    df.to_csv("./data/housing_data.csv", index=False)
