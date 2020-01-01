from bs4 import BeautifulSoup
import requests

import numpy as np
import threading

from matplotlib.font_manager import FontProperties
from matplotlib.figure import Figure
import os

area_list = ['臺北市', '新北市', '桃園市', '臺中市', '臺南市', '高雄市',
             '基隆市', '新竹市', '嘉義市',
             '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣']

item_list = ['食品', '飲品', '菸品', '停車', '汽油', '其他']

def winners_count(period, table_id):
    url = 'https://www.etax.nat.gov.tw/etw-main/web/ETW183W3_' + period
    html = requests.get(url).content.decode('utf-8')
    sp = BeautifulSoup(html, 'html.parser')
    table = sp.find('table', {'id': table_id})
    rows = table.find_all('tr')

    area_count = dict.fromkeys(area_list, 0)
    item_count = dict.fromkeys(item_list, 0)
    for row in rows[1:]:
        row_tds = row.find_all('td')
        item = row_tds[4].text[:2]
        try:
            item_count[item] += 1
        except:
            item_count['其他'] += 1

        area = row_tds[3].text[:3]
        try:
            area_count[area] += 1
        except:
            if (area == '桃園縣'):
                area_count['桃園市'] += 1

    return item_count, area_count


item_sum_1000 = np.zeros(len(item_list))
area_sum_1000 = np.zeros(len(area_list))
item_sum_200 = np.zeros(len(item_list))
area_sum_200 = np.zeros(len(area_list))


def winner_sum(period_list, item_sum_1000, area_sum_1000, item_sum_200, area_sum_200):
    for period in period_list:
        item_count_1000, area_count_1000 = winners_count(period, 'fbonly')
        item_count_200, area_count_200 = winners_count(period, 'fbonly_200')
        item_sum_1000 += list(item_count_1000.values())
        area_sum_1000 += list(area_count_1000.values())
        item_sum_200 += list(item_count_200.values())
        area_sum_200 += list(area_count_200.values())


def bar_chart():
    font = FontProperties(fname=os.environ['WINDIR'] + '\\Fonts\\kaiu.ttf', size=12)
    f = Figure(figsize=(16, 9))

    a = f.add_subplot(211)
    a.bar(np.arange(len(item_list)) - 0.2, item_sum_1000, width=0.4, label='1000萬')
    a.bar(np.arange(len(item_list)) + 0.2, item_sum_200, width=0.4, label='200萬')
    a.set_xticks(np.arange(len(item_list)))
    a.set_xticklabels(item_list, fontproperties=font)

    b = f.add_subplot(212)
    b.bar(np.arange(len(area_list)) - 0.2, area_sum_1000, width=0.4, label='1000萬')
    b.bar(np.arange(len(area_list)) + 0.2, area_sum_200, width=0.4, label='200萬')
    b.set_xticks(np.arange(len(area_list)))
    b.set_xticklabels(area_list, fontproperties=font)

    print('Generated Fig: ' + str(f))
    #f.savefig('ResultFig.png')
    return f


def GenerateFig(period):
    selected_period = [period]
    thread1 = threading.Thread(target=winner_sum, args=(
        selected_period[:len(selected_period) // 2], item_sum_1000, area_sum_1000, item_sum_200, area_sum_200))
    thread2 = threading.Thread(target=winner_sum, args=(
        selected_period[len(selected_period) // 2:], item_sum_1000, area_sum_1000, item_sum_200, area_sum_200))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print('Data collect complete. Generating Fig.')
    return bar_chart()

#Testing Code
def GenerateFigTest():
    fff = GenerateFig('10303')
    fff.savefig('ResultFig2.png')
    print('Fig Saved.')