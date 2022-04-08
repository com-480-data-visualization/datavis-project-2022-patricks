from asyncio import Future
from multiprocessing import Lock
from platform import release
import re
from time import sleep
from tkinter.messagebox import NO
from bs4 import BeautifulSoup
from urllib import request
import requests
import pandas as pd
import numpy as np
import threading
from concurrent.futures import ThreadPoolExecutor



# def fetch_parse_html(url, headers = None):
#     if headers is None:
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
#     try:
#         html = requests.get(url, headers = headers, allow_redirects=False).content
#     except:
#         return None
#     bs = BeautifulSoup(html,"html.parser")
#     return bs

# def extract_from_bs(bs, criterion = None):
#     if criterion is None:
#         # name = None
#         # date = None
#         try:
#             # name = bs.find(name='div', attrs={'class': {'product_title'}}).find(name='h1').contents[0]
#             date = bs.find(name='li', attrs={'class': {'summary_detail release_data'}}).find(name='span', attrs={'class':{"data"}}).contents[0]
#         except:
#             date = "nan"
#     return date

# def worker(url, name, headers = None, criterion = None):

#     bs = fetch_parse_html(url, headers)
#     res = extract_from_bs(bs, criterion)
#     return res, name

# global release_date
# release_date = {"name":[], "date":[]}
# global lock
# lock = threading.Lock()

# def add_result(future: Future):
#     global lock
#     lock.acquire()
#     global release_date
#     date, name = future.result()
#     release_date["name"].append(name)
#     release_date["date"].append(date)
#     lock.release()
    


# with ThreadPoolExecutor(max_workers= 8) as pool:
#     data = pd.read_csv("C:\\Users\\49387\\Desktop\\games_of_all_time.csv", sep=",")
#     for i,(url,name) in enumerate(zip(data['url'].to_numpy(), data['game_name'].to_numpy())):
#         f = pool.submit(worker, url, name)
#         f.add_done_callback(add_result)
#     while len(release_date['name']) < data.shape[0]:
#         sleep(20)
#         print(f"{len(release_date['name'])}/{data.shape[0]}")

#     temp = pd.DataFrame(release_date)
#     temp.to_csv("C:\\Users\\49387\\Desktop\\temp.csv", sep=",")
#     # np.save('C:\\Users\\49387\\Desktop\\my_file.npy', release_date)
#     # data.insert(data.shape[1], 'release_date', release_date)
#     # data.to_csv("new_m.csv",sep=',')

data = pd.read_csv("C:\\Users\\49387\\Desktop\\games_of_all_time.csv", sep=",", index_col=0)

release_date = pd.read_csv("C:\\Users\\49387\\Desktop\\temp.csv", sep=",", index_col=0, usecols=[1,2])

a = release_date.join(data, on="name" )
a.to_csv("C:\\Users\\49387\\Desktop\\new_data.csv", sep=",")
# print(release_date)