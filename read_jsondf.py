def wrangle(filename):
    #open compressed file,load into dict
    with gzip.open(filename,"r") as f:
        data=json.load(f)
    #turn dict into dataframe
    df=pd.DataFrame().from_dict(data["data"]).set_index("company_id")
    return df

    
df = wrangle("data/poland-bankruptcy-data-2009.json.gz")
print(df.shape)
df.head()