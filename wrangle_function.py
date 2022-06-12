def wrangle(filepath):
    # Read CSV file
    df = pd.read_csv(filepath)

    # Subset data: Apartments in "Capital Federal", less than 400,000
    mask_ba = df["place_with_parent_names"].str.contains("Capital Federal")
    mask_apt = df["property_type"] == "apartment"
    mask_price = df["price_aprox_usd"] < 400_000
    df = df[mask_ba & mask_apt & mask_price]

    # Subset data: Remove outliers for "surface_covered_in_m2"
    low, high = df["surface_covered_in_m2"].quantile([0.1, 0.9])
    mask_area = df["surface_covered_in_m2"].between(low, high)
    df = df[mask_area]

    # Split "lat-lon" column
    df[["lat", "lon"]
       ] = df["lat-lon"].str.split(",", expand=True).astype(float)
    df.drop(columns="lat-lon", inplace=True)

    # Get place name
    df["neighborhood"] = df["place_with_parent_names"].str.split("|", expand=True)[
        3]
    df.drop(columns="place_with_parent_names", inplace=True)

    # drop features with null high counts
    df.drop(columns=['floor', "expenses"], inplace=True)

    # drop low/high cardinality categorical variables
    df.drop(columns=["property_type", "currency",
            "operation", "properati_url"], inplace=True)

    # drop leaky columns
    df.drop(columns=['price', 'price_aprox_local_currency',
            'price_per_m2', 'price_usd_per_m2'], inplace=True)

    # drop columns with multicollinearity
    df.drop(columns=["surface_total_in_m2", "rooms"], inplace=True)

    return df

    # use glob
files = glob("data/buenos-aires-real-estate-*.csv")
files


# for loop
# frames =[]
# for file in files:
#     df=wrangle(file)
#     frames.append(df)

# list comprehension
frames = [wrangle(file)for file in files]

df = pd.concat(frames, ignore_inde=True)
