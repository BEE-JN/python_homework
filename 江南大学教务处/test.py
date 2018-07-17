import requests
import time

url = "https://survey.zkeycc/pku/xsdc/?dm=bk"
if __name__=='__main__':
    while 1:
        r=requests.get(url)
        print(r.content)
        time.sleep(1)