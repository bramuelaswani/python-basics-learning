import urllib.request

#fetchindg data
def main():
    webUrl=urllib.request.urlopen("https://www.youtube.com")
    print('result code:' + str(webUrl.getcode( )))

    #read data
    data=webUrl.read()
    print(data)
main()