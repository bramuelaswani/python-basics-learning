# Create pivot table
foundation_pivot = pd.pivot_table(
    df, index="foundation_type",values="severe_damage",aggfunc=np.mean
    ).sort_values(by="severe_damage")
foundation_pivot