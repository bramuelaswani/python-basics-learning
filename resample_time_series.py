df = df["P2"].resample("1H").mean().fillna(method="ffill").to_frame()
