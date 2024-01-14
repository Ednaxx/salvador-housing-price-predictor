import numpy as np

def build_features(df):
    # Missing neighborhood set to NaN
    df.neighborhood = df.neighborhood.apply(lambda x: np.nan if x == "BA" else x)

    # Drop null prices and areas over 2000m^2
    df = df[~(df.prices.isna())]
    df = df[~(df.areas > 2000)]

    # neighborhood Price/Area

    neighborhood_house_price_sum =  df[df.type == "house"].groupby("neighborhood").prices.sum()
    neighborhood_house_area_sum =  df[df.type == "house"].groupby("neighborhood").areas.sum()

    neighborhood_apartment_price_sum =  df[df.type == "apartment"].groupby("neighborhood").prices.sum()
    neighborhood_apartment_area_sum =  df[df.type == "apartment"].groupby("neighborhood").areas.sum()

    def calculate_neighborhood_area_price(x):
        if x.type == "house" and x.neighborhood in neighborhood_house_price_sum:
            return neighborhood_house_price_sum[x.neighborhood] / neighborhood_house_area_sum[x.neighborhood]
        if x.type == "apartment" and x.neighborhood in neighborhood_house_price_sum:
            return neighborhood_apartment_price_sum[x.neighborhood] / neighborhood_apartment_area_sum[x.neighborhood]
        else: return np.nan

    df["neighborhood_area_price"] = df.apply(calculate_neighborhood_area_price, axis=1)

    df.type = df.type.replace({"house": 0, "apartment": 1})

    return df