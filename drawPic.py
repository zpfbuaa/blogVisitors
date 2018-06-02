# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 下午2:04
# @Author  : 伊甸一点
# @FileName: drawPic.py
# @Software: PyCharm
# @Blog    : http://zpfbuaa.github.io

import matplotlib.pyplot as plt
import math
import time
import pickle

def readData(file_name, data_root = 'data/'):
    date = []
    visitors = []
    flagViews = []

    with open(data_root + file_name,'r') as f:
        data = f.readlines()
    for i in range(len(data)-1, 0, -1):
        item_data = data[i].split('\t')
        date.append(item_data[0])
        visitors.append(int(item_data[1]))
        flagViews.append(int(item_data[2].split('\n')[0]))

    return date, visitors, flagViews

def draw_pic(label, draw_data, today = time.strftime('%Y%m%d', time.localtime(time.time())), result_root = 'result/'):
    data_len = len(draw_data)
    x = range(0,data_len)

    round = int(math.ceil(data_len/100))

    for i in range(0,round):
        start = 100 * i
        if i == round-1:
            end = data_len
        else:
            end = 100 + 100 * i
        plt.plot(x[start:end],draw_data[start:end],label=str(start)+'~'+str(end))

    plt.xlabel('Date')
    plt.ylabel(label)
    plt.title('Blog '+label+' Start Date 2015.12.17')
    plt.legend()
    plt.savefig(result_root+label + str(today) + '.jpg')
    plt.show()



def drawDiff(visitors, flagViews):
    diff = []
    data_len = len(visitors)
    for i in range(0, data_len):
        diff.append(flagViews[i] - visitors[i])
    draw_pic('Diff', diff)

def save_pickle(date, visitors, flagViews, pickle_root = 'pickle/'):
    try:
        with open(pickle_root+'date.pickle','wb') as date_file, \
             open(pickle_root+'visitors.pickle','wb') as visitors_file, \
             open(pickle_root+'flagViews.pickle','wb') as flagViews_file:
            pickle.dump(date, date_file)
            pickle.dump(visitors, visitors_file)
            pickle.dump(flagViews, flagViews_file)
    except IOError as err:
        print('IOError', str(err))
    except pickle.PickleError as err:
        print('PickleError', str(err))


def draw(file_name, load_pickle, pickle_root = 'pickle/'):
    if load_pickle:
        print('Loading Pickle...')
        try:
            with open(pickle_root+'date.pickle','rb') as df, \
            open(pickle_root+'visitors.pickle','rb') as vf, \
            open(pickle_root+'flagViews.pickle','rb') as ff:
                date = pickle.load(df)
                visitors = pickle.load(vf)
                flagViews = pickle.load(ff)
                print('Loading Done!')
        except IOError as err:
            print('IOError', str(err))
        except pickle.PickleError as err:
            print('PickleError', str(err))
    else:
        date, visitors, flagViews = readData(file_name)
        save_pickle(date, visitors, flagViews)

    draw_pic('Visitors', visitors)

    draw_pic('FlagViews', flagViews)

    drawDiff(visitors, flagViews)

today = time.strftime('%Y%m%d', time.localtime(time.time()))

data_file = 'blog_'+str(today)

draw(file_name=data_file, load_pickle=False)
