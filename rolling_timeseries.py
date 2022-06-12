
# weekly rolled
df = 6
fig, ax = plt.subplots(figsize=(15, 6))
df["P2"].rolling(168).mean().plot(
    ax=ax, ylabel="PM2.5", title="Weeky Rolling Average")
