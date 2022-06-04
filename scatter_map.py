fig = px.scatter_mapbox(
    df,  # Our DataFrame
    lat="lat",
    lon="lon",
    width=600,  # Width of map
    height=600,  # Height of map
    color="price_aprox_usd",
    # Display price when hovering mouse over house
    hover_data=["price_aprox_usd"],
)

fig.update_layout(mapbox_style="open-street-map")

fig.show()
