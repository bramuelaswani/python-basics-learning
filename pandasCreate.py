import pandas as pd
#path = ("C:\Users\User\Desktop\bramuel\KEDIZOH")
#airbnb = pd.read_excel('sample.xlsx',header='infer')
airbnb2=pd.read_csv('Bankers.csv')
print(airbnb2.head())
#print(airbnb2.Name[0])
#print(airbnb2.iloc[3]) #getting row
#print(airbnb2.iloc[:,1]) #getting column
#print(airbnb2['Name'][4])
#print(airbnb2.loc[1,'Surname']) #getting content in specified field
#print(airbnb2.set_index('Customer ID')) #settting index
#print(airbnb2['Surname']=='Reid')
#print(airbnb2.loc[(airbnb2.Surname)=='Reid'|(airbnb2.Color=="White")]) #only selects those with surname Reid
#print(airbnb2.loc[airbnb2.Name.notnull()]) #prints all withou names
airbnb2['Names']=airbnb2['Name']+" "+ airbnb2["Surname"]
#print(airbnb2.sort_values('Names'))
airbnb2['country']="kenya"
print(airbnb2)
#airbnb=pd.io.json.read_jso('Sample3.json', orient='index')

#print(airbnb.index)
#print(airbnb.sort_values('Rep',ascending=False).head())
#print(airbnb[airbnb["Units"]>70])
#airbnb["total"]=airbnb["Units"] * airbnb["Unit Price"] #add column
#airbnb.loc[3,"Rep"]="Kedizo" #Updating database
'''for x in airbnb.index:
    if airbnb.loc[x,"Units"]<85:
        airbnb.drop(x,inplace=True)     
print(airbnb.sort_values("total",ascending=False))#.head())

#print([airbnb[["OrderDate","total"]].head()])'''

'''#removing duplicates
print(airbnb.to_string())
airbnb.corr() #correlations
print(airbnb.duplicated())'''

#saving panda file
#airbnb.to_excel("modified3.xlsx")



