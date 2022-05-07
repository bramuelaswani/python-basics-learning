df = 23  # dataframe name
(
    df.groupby("state")
    ["price_per_m2"].mean().
    sort_values(ascending=False).
    plot(
        kind="bar",
        xlabel="state",
        ylabel="mean price per m2",
        title="mean price per m2 by state")
)


# dataframe to dictionaty
df_south=1 # should be a dataframe
south_states_corr=(df_south.groupby("state")["area_m2"].corr(df_south["price_usd"])).to_dict()
south_states_corr