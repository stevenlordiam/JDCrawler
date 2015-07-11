import urllib2
import urllib
import os
import sys
from bs4 import BeautifulSoup
from progress.bar import Bar
start_page = int(sys.argv[1])
end_page = int(sys.argv[2]) + 1

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

def fetch_data(url):
    try:
        request = urllib2.Request(url,None, headers)
        respond = urllib2.urlopen(request)
        return respond.read()
    except urllib2.URLError,error:
        print error.reason

def fetch_image_list(page):
    url = 'http://jandan.net/ooxx/page-' + str(page) + '#comments'
    html = fetch_data(url)
    try:
        soup = BeautifulSoup(html,"html.parser")
    except TypeError:
        return []
    imgs = soup.find_all('img')
    image_list = []
    for img in imgs:
        src = ''
        if img.has_attr('org_src'):
            src =img['org_src']
        else:
            src = img['src']
        if src.find('sinaimg') != -1:
            image_list.append(src)
    return image_list


def save_image(image_url, filename, new_path):
    image = fetch_data(image_url)
    f = file(new_path+filename,'wb')
    f.write(image)
    f.close()

def crawler():
    bar = Bar('Processing', max=end_page-start_page)
    for i in range(start_page,end_page):
        imagelist = fetch_image_list(i)
        for image_url in imagelist:
            new_path = './image/'+str(i)+'/'
            if not os.path.isdir(new_path):
                os.makedirs(new_path)
            save_image(image_url, image_url.split('/')[-1], new_path)
        print '--------------------------------------------'
        print 'finish getting data from page ' + str(i)
        bar.next()
        print
    bar.finish()
    print '--------------------------------------------'
    print 'All pictures saved sucessfully!'
    print '--------------------------------------------'
    
if __name__ == "__main__": crawler()