#REQUIREMENTS: This scripts takes a url, URL Should be of youtube page.
#WORKING: After this takes arguments, it will crawl the whole page and exract the titles of each video that is in the page.

import os, sys
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def scrape_video_titles(playlist_url: str, opts: Options):
    assert isinstance(playlist_url, str)
    Chromepath = input('Enter the Path Of Chrome Webdriver')
    driver = webdriver.Chrome(options=opts, executable_path=Chromepath)
    driver.get(playlist_url)
    # get html
    elem = driver.find_element_by_tag_name('html')
    elem.send_keys(Keys.END)
    time.sleep(3)
    elem.send_keys(Keys.END)
    innerHTML = driver.execute_script("return document.body.innerHTML")
    driver.close()
    # parse the html
    page_soup = bs(innerHTML, 'html.parser')
    res = page_soup.find_all('a', {'class': 'yt-simple-endpoint style-scope ytd-video-renderer'},)
    # get titles
#    print(res)
    titles=[]
    for video in res:
        if video.get('title') != None:
            titles.append((video.get('title')))
    return titles
if __name__ == "__main__":
    print('Make sure that you are using terminal (Like termux)')
    clearType = input('This is Terminal YES OR NO? (y/n): ').lower()
    if clearType == 'y':
        clear = lambda:os.system('clear')
    elif clearType == 'n':
        sys.exit()
    else:
        print('Invalid input!!!')
        sys.exit()
    print('Installing The dependencies That are required')
    colors = {
            "re": "\u001b[31;1m",
            "gr": "\u001b[32m",
            "ye": "\u001b[33;1m",
        }
    wt = (
        """
        Youtube
        """
        )
    time.sleep(1)
    re = "\u001b[31;1m"
    gr = "\u001b[32m"
    ye = "\u001b[33;1m"
    if sys.version_info[0] < 3:
        telet = lambda :os.system('pip install -U beautifulsoup4')
        telet1 = lambda :os.system('pip install -U selenium')
        telet2 = lambda :os.system('pip install -U pandas')        
    elif sys.version_info[0] >= 3:
        telet = lambda :os.system('pip install -U beautifulsoup4')
        telet1 = lambda :os.system('pip install -U selenium')
        telet2 = lambda :os.system('pip install -U pandas') 
    telet()
    telet1()
    telet2()
    time.sleep(1)
    print(wt)
    clear()
    urls= input(re+'Enter the URL of the youtube page:')
    filename1 = input(gr+'Enter the saving name of file')
    filename = filename1 + '.txt'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    opts = Options()
    opts.add_argument(f'user-agent={user_agent}')
    #urls = pd.read_csv('C:/Users/Nautiyal/Desktop/youtube.csv')
    save_path = filename
    # get titles
    print(re+'Running ........ ')
    titles = scrape_video_titles(urls, opts)
    with open(save_path, 'a', encoding="utf-8") as f:
        f.write(str(titles))
    print(re+'Successfully Saved ','\n',':-)','\n','#VIASK')
    print(ye+wt)
