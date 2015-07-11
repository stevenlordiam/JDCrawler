import urllib2, urllib, os, sys, random
from bs4 import BeautifulSoup
from progress.bar import Bar
start_page = int(sys.argv[1])
end_page = int(sys.argv[2]) + 1

user_agent_list = [
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
                    'Opera/9.25 (Windows NT 5.1; U; en)',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
                    'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
                    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
                    "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",

                    ] 
       
agent = random.choice(user_agent_list)

headers = {'User-Agent': agent, 'Connection': 'keep-alive'}

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