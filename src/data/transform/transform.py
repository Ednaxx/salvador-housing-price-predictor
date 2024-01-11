import pandas as pd

def transform_data(df):
    print("Transforming data.")

    df = df.drop_duplicates(subset=["id"])
    df = df.dropna(subset=["prices"])


    df['type'] = ''
    # Drop offices, rooms and other possible non-residential titles
    df = df[~df['titles'].str.contains('sala', case=False)]

    df.loc[df['titles'].str.contains('casa', case=False), 'type'] = 'house'
    df.loc[df['titles'].str.contains('apartamento|residencial', case=False), 'type'] = 'apartment'

    df = df.drop("titles", axis=1)


    neighborhood = df.addresses.str.split(" - ", expand=True)
    neighborhood = neighborhood[neighborhood.columns[1]]
    neighborhood = neighborhood.str.split(",", expand=True)
    neighborhood = neighborhood[neighborhood.columns[0]]
    neighborhood = neighborhood.rename("neighborhood")

    df = df.drop("addresses", axis=1)
    df = pd.concat([df, neighborhood], axis=1)


    df.prices = df.prices.str.strip(" ")
    df.prices = df.prices.str.replace("R$ ", "")
    df.prices = df.prices.str.replace("      Preço abaixo do mercado", "")
    df.prices = df.prices.str.replace("A partir de     ", "")
    df.prices = df.prices.str.replace(".", "")

    df.prices = pd.to_numeric(df.prices)



    df.replace(" -- ", "", inplace=True)

    def parse_range_and_mean(value):
        if '-' in value:
            start, end = map(int, value.split('-'))
            return (start + end) / 2
        else:
            return float(value) if value != '' else None

    columns_to_transform = ['areas', 'bedrooms', 'bathrooms', 'parkingSpots']
    for column in columns_to_transform:
        df[column] = df[column].apply(parse_range_and_mean)


    return df



if __name__ == '__main__':
    scraped_data = pd.read_csv("./data/scraped_data.csv")
    if (scraped_data.columns[0] == "Unnamed: 0"): scraped_data = scraped_data.drop(scraped_data.columns[0], axis=1)
    data = transform_data(scraped_data)
    data = data.set_index("id")
    data.to_csv("./data/transformed_data.csv", encoding='utf-8')
