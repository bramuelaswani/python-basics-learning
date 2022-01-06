import urllib.request
import json #javascript object notation
def main():
    def printResults(data):
    #use the json module to load data
     theJson=Json.load(data)
    #now we can accesss the content of Json like a python oject
    if "title" in theJson["metadata"] :
        print(theJson["metadata"]["title"])
        #output the numeber of events plus the magnitude and event name
        count=theJson["metadata"]["count"]
        print(str(count)+ "events recorded")
        #for each event print the place where it occured
        for i in theJson["features"]:
            print(i["properties"]["place"])
            print("........\n")
            #prints events mag more thsn 4
    for i in theJson["features"]:
           if i['properties']["mag"]>=4.0:
                    print("%2.if" % i["properties"]["mag"],["properties"]["place"])
                    print("........\n")
        
    #print only events where atleast one person reported the feeling
    print("events that were felt:")
    for i in theJson["features"]:
        feltReports=i["properties"]["felt"]
        if feltReports!=None:
            if feltReports>0:
                 print("%2.if" % i["properties"]["mag"],["properties"]["place"])
                 "reported" + str(feltReports)+ "times"
    
    urlData= "https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"
    webUrl = urllib.request.urlopen(urlData)
    print("result code:" + str(webUrl.getcode()))
    if (webUrl.getcode()==200):
        data=webUrl.read()
        printResults(data)
    else:
        print('received error, cannot parse results')
if __name__=="__main__":
        main()