def wrangle(collection):
    results = collection.find(
        {"metadata.site": 29, "metadata.measurement": "P2"},
        projection={"P2": 1, "timestamp": 1, "_id": 0},
    )

    df = pd.DataFrame(results).set_index("timestamp")
    # localize timezone
    df.index = df.index.tz_localize('UTC').tz_convert("Africa/Nairobi")

    # remove outliers
    df = df[df["P2"] < 500]

    # resampple a time series data
    df = df["P2"].resample("1H").mean().fillna(method="ffill").to_frame()

    # create a lag feature i.e new col with lag of 1
    df["P2.L1"] = df["P2"].shift(1)
    # drop na
    df.dropna(inplace=True)

    return df
