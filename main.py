# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import re
import gc
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
def hello():
    #text = text.replace(" ","+")
    # print(text)
    # url = f'https://www.bing.com/search?q=%2B"{text}"&qs=n&form=QBRE&sp=-1&pq=%2B"{text.lower()}"'
    url = 'https://www.google.com/search?q=' + "gfg"
    # Crafting the proper request
    header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0'}
    response=requests.get(url,headers= header, allow_redirects=True)



    content = BeautifulSoup(response.content, 'html.parser')
    # content = BeautifulSoup(page.text,'html.parser')
    # print("start of data.....")
    # print(content)
    # print("end ....")
    gc.collect()
    # print(content.prettify())

    # file = open('read1.txt', 'w')
    # file.write(content.prettify())
    # file.close()
    # yuRUbf class name google search

    #return content
    # link= content.find('h2')
    for a in content.find_all('a', href=True):
        if a['href']!='#' and re.findall("^http",a['href']):
            print("Found the URL:", a['href'])
    print(content.find('a')['href'])
    # print(content)
    try:
        element=content.find('li',class_='b_algo').h2
        link= element.find('a')['href']

        # print("" link
    except:
        print("some error occured")


hello()

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
