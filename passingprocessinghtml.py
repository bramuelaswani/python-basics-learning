from html.parser import HTMLparser
class myHTMLparser:
def main():
    #instantiate the paser and feed it some HTML
    parser=myHTMLparser
    f=open("sammplehtml.html")
    if f.mode=="r":
        conntents=f.read()
        parser.feed(contents)
        







if __name__=="_main_":
    main()