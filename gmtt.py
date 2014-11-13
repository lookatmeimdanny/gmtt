#! /usr/bin/python

from bs4 import BeautifulSoup
from TumblPost import *

def readInputFile( fileName ):
    global success
    try:
        f = open( fileName, 'r' )
        fStr = f.read()
        success = 1
        return fStr
    except IOError:
        print( "Oops, no file named " + fileName + ", going on to next one..." )
        success = 0

def parseInputFile( fileString ):
    soup = BeautifulSoup( fileString )
    contentSoup = soup.find( "div", class_ = "content" )
    
    headerStr = contentSoup.find( "h1" ).get_text()
    bodyStr = contentSoup.find_all( "p" )[1].prettify( formatter="minimal" )

    #separate date from title
    dateStr = headerStr.split( '"' )[0].strip( ': ' )
    titleStr = headerStr.split( '"' )[1].strip( '"' )
    
    #print( titleStr + "\n\n\n" + dateStr + "\n\n\n" + bodyStr )

    #print( titleStr )
    tPost = TumblPost( dateStr, titleStr, bodyStr )
    tPost.PostToTumblr()

def main():
    endValue = 198 #last file number
    
    fPath = "../data/"

    for i in range( 197 , endValue + 1 ):
        fName = ("%08d" % i) + ".html"
        fStr = readInputFile( fPath + fName )
        if success:
            print( fName )
            parseInputFile( fStr )
    
if __name__ == "__main__":
    main()
    
