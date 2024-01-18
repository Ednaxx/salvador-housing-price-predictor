from src.data.extract.extract import get_data
from src.data.transform.transform import transform_data
import pandas as pd

def load_data(i):
    scraped_data = get_data((1 + (i * 50)), (51 + (i * 50)))
    clean_data = transform_data(scraped_data)

    return clean_data

if __name__ == "__main__":
    for i in range(5):
        try:
            df = pd.read_csv("./data/housing_data.csv")
            new_data = load_data(i)

            df = pd.concat([df, new_data], axis=0)
            df = df.drop_duplicates(subset="id")
        except:
            df = load_data()
        
        df.to_csv("./data/housing_data.csv", index=False)
