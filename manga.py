#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      prasanna
#
# Created:     15-01-2016
# Copyright:   (c) prasanna 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os
import requests
import urllib.request
from bs4 import BeautifulSoup
for j in range(469,470):
    for i in range(1,30):

        str1 = "http://www.mangatown.com/manga/fairy_tail/v38/c"+str(j)+"/"+str(i)+".html"
        try:
            page = requests.get(str1).content
            s = BeautifulSoup(page)
            imgblock = s.find("div",{"class":"read_img"})
            imgtag = imgblock.find("img")
            url = imgtag['src']
            print(url)
            imagename = str(i)
            filename=str1[25:50]
            directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
            if not os.path.exists(directory):
                os.makedirs(directory)
            filepath = os.path.join(directory,imagename+".jpg")
            urllib.request.urlretrieve(url,filepath)

        except :
            pass
def main():
    pass

if __name__ == '__main__':
    main()
