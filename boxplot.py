df = 7
fig, ax = plt.subplots(figsize=(15, 6))
df["P2"].plot(kind='box', vert=False,
              title="Distribution of PM2.5 Readings", ax=ax)
