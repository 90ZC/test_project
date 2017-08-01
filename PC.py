import re
import requests as req
import bs4
from bs4 import BeautifulSoup as bs

def HtmlGet(url,code='utf-8'):
    try:
        request=req.get(url)
        request.raise_for_status()
        request.encoding=code
        return request.text
    except:
        return ""

def HtmlAss(li,url):
    html=HtmlGet(url,'GB2312')
    soup=bs4.BeautifulSoup(html,"html.parser")
    l=soup.find_all('a')
    for i in l:
        try:
            href=i.attrs['href']
            st=re.findall(r"[s][hz]\d{6}",href)[0]
            li.append(st)
        except:
            continue
    return li

def HtmlPri(li,fileurl,url):
    count=0
    for i in li:
        url2=url+i+".html"
        html=HtmlGet(url2)
        try:
            if html=="":
                continue
            dic = {}
            list=[]
            soup=bs4.BeautifulSoup(html,"html.parser")
            info=soup.find('div',attrs={'class':'stock-bets'})
            name=info.find_all(attrs={'class':'bets-name'})[0]
            price=info.find_all('strong',attrs={'class':'_close'})[0]
            list.append(name.text.strip().split()[0])
            list.append(price.text)
            dic.update({'股票名称：':str(list)})
            with open(fileurl,'a') as f:
                f.write(str(dic)+'\n')
                count=count+1
                print('\r当前进度：{:.2f}%'.format(count/len(li)),end='')
                f.close()
        except:
            f.close()
            #traceback.print_exc()
def main():
    li=[]
    url="http://quote.eastmoney.com/stocklist.html"
    url2="https://gupiao.baidu.com/stock/"
    fileurl="F:\\t.txt"
    #url2=""
    li=HtmlAss(li,url)
    HtmlPri(li,fileurl,url2)

main()