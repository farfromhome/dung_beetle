#!/usr/bin/python
'''
use multiple thread get the first 50 pages from ubuntu-forum, 
but not perfect, because have some repetitive record
'''

import requests
from bs4 import BeautifulSoup
import threading

n = 0
url_list = ['http://ubuntuforums.org/forumdisplay.php?f=333',]
for x in range(1, 50):
    n += 1
    raw_url = 'http://ubuntuforums.org/forumdisplay.php?f=333&page=%d' % n
    url_list.append(raw_url)

class MyThread(threading.Thread):
    def __init__(self, func, args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
    def run(self):
        apply(self.func, self.args)

def running(url):
    # lock.acquire()
    html = requests.get(url)
    if html.status_code == 200:
        html_text = html.text

    soup = BeautifulSoup(html_text)
    with open('/home/zhg/Pictures/cao.txt', 'a+') as f:
        for link in soup.find_all('a', 'title'):
            s = 'http://ubuntuforums.org/' + str(link.get('href')) + ' ' + str(link.get_text().encode('utf-8'))
            f.writelines(s)
            f.writelines('\n')
    # lock.release()

if __name__ == '__main__':
    thread_list = [ MyThread(running, (url, )) for url in url_list ]
    for t in thread_list:
        t.setDaemon(True)
        t.start()
    for i in thread_list:
        i.join()
    print "process ended"

    # inspect repetition data
    with open('/home/zhg/Pictures/cao.txt', 'r') as f:
        f_list = f.readlines()
        set_list = set(f_list)
    for x in set_list:
        if f_list.count(x) > 1:
            print "the <%s> has found <%d>" % (x, f_list.count(x))



'''
multiprocess edition
'''
'''
import requests
from bs4 import BeautifulSoup
import multiprocessing

n = 0
url_list = ['http://ubuntuforums.org/forumdisplay.php?f=333', ]
for x in range(1, 50):
    n += 1
    raw_url = 'http://ubuntuforums.org/forumdisplay.php?f=333&page=%d' % n
    url_list.append(raw_url)

def running(url, q):
    html = requests.get(url)
    if html.status_code == 200:
        html_text = html.text
    soup = BeautifulSoup(html_text)
    with open('/home/zhg/Pictures/cao.txt', 'a+') as f:
        for link in soup.find_all('a', 'title'):
            s = 'http://ubuntuforums.org/' + str(link.get('href')) + ' ' + str(link.get_text().encode('utf-8'))
            f.writelines(s)
            f.writelines('\n')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    p = multiprocessing.Pool(len(url_list))
    q = manager.Queue()
    lock = manager.Lock()
    for x in url_list:
        p.apply_async(running, args=(x, q))
    p.close()
    p.join()
    print "process ended"

    with open('/home/zhg/Pictures/cao.txt', 'r') as f:
        f_list = f.readlines()
        set_list = set(f_list)
    for x in set_list:
        if f_list.count(x) > 1:
            print "the <%s> has found <%d>" % (x, f_list.count(x))
#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import multiprocessing

n = 0
url_list = ['http://ubuntuforums.org/forumdisplay.php?f=333', ]
for x in range(1, 50):
    n += 1
    raw_url = 'http://ubuntuforums.org/forumdisplay.php?f=333&page=%d' % n
    url_list.append(raw_url)

def running(url, q):
    html = requests.get(url)
    if html.status_code == 200:
        html_text = html.text
    soup = BeautifulSoup(html_text)
    with open('/home/zhg/Pictures/cao.txt', 'a+') as f:
        for link in soup.find_all('a', 'title'):
            s = 'http://ubuntuforums.org/' + str(link.get('href')) + ' ' + str(link.get_text().encode('utf-8'))
            f.writelines(s)
            f.writelines('\n')

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    p = multiprocessing.Pool(len(url_list))
    q = manager.Queue()
    lock = manager.Lock()
    for x in url_list:
        p.apply_async(running, args=(x, q))
    p.close()
    p.join()
    print "process ended"

    with open('/home/zhg/Pictures/cao.txt', 'r') as f:
        f_list = f.readlines()
        set_list = set(f_list)
    for x in set_list:
        if f_list.count(x) > 1:
            print "the <%s> has found <%d>" % (x, f_list.count(x))

'''
