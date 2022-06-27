# group caste column
top_10 = df["caste_household"].value_counts().head(10).index
df["caste_household"] = df["caste_household"].apply(
    lambda c: c if c in top_10 else "other")
