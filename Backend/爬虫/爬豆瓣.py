#-*- encoding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import openpyxl

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

# 创建一个工作簿
workbook = openpyxl.Workbook()
# 获取工作表
worksheet = workbook.active
# 添加表头
worksheet.append(['电影名', '评分'])

# 循环爬取 Top 250 的每一页
for i in range(10):
    # 构造请求 URL
    url = f'https://movie.douban.com/top250?start={i * 25}&filter='
    # 发送请求，添加请求头
    response = requests.get(url, headers=headers)
    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    # 获取电影列表
    movie_list = soup.find(class_='grid_view').find_all('li')

    # 循环处理每一部电影
    for movie in movie_list:
        # 获取电影名和评分
        name = movie.find(class_='title').text.strip()
        rating = movie.find(class_='rating_num').text.strip()
        # 添加到工作表中
        worksheet.append([name, rating])

# 保存工作簿
workbook.save('douban_top250.xlsx')
