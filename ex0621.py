#import webbrowser
#address=input('輸入地址:')
#webbrowser.open('https://www.google.com.tw/maps/place/'+address)


#import urllib.request
#response=urllib.request.urlopen('https://tw.yahoo.com/')
#html=response.read()
#print(html)

import requests
url='https://tw.yahoo.com/'
html_body=requests.get(url)
html_body.encoding='utf-8'
print(html_body.text)


string = "python"
print(string[3:5])