import pandas as pd

def transform_data():
    df = pd.read_csv("../data/scraped_data.csv")

    df = df.drop_duplicates()
    df = df.drop(df.columns[0], axis=1)
    df = df.dropna(subset=["prices"])



    df['type'] = ''
    # Drop offices, rooms and other possible non-residential titles
    df = df[~df['titles'].str.contains('sala', case=False)]

    df.loc[df['titles'].str.contains('casa', case=False), 'type'] = 'house'
    df.loc[df['titles'].str.contains('apartamento|residencial', case=False), 'type'] = 'apartment'

    df = df.drop("titles", axis=1)


    addresses = df.addresses.str.split(" - ", expand=True)
    addresses = addresses.rename(columns={0: "streets", 1: "neighborhood"})
    addresses.neighborhood = addresses.neighborhood.str.replace(", Salvador", "")
    addresses = addresses.drop(addresses.columns[2], axis=1)

    df = df.drop("addresses", axis=1)
    df = pd.concat([df, addresses], axis=1)



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
    data = transform_data()
    data.to_csv("../data/transformed_data.csv", encoding='utf-8')
