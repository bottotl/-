import urllib2
import re
import time

userids = ['244525', '5912241', '6472328', '6472388', '6474190', '6475060', '6476192']

tokens = ['032acce16227a36008cfbaef09a04398ccee0bd0', 'c4e5db8454363e28df24a61b6aba212ca209b52b', '2705807afca972c6397315f24500bafa04b38d2f', 'a61bcfadcc9a6321a10dcc3f20fc822c7aff2459', '48ca127b3dabc24b12ae82ad8cb95804d24af36b', 'f5bae1d690c4ec6345ab1e0ff345041d5ef2b520', 'bbb88ff77ab97ec6ec1293f45832478f60ee9deb']

totalcount = 0

def makeUrl(userid, token, share_page, shop_id):
    url = 'http://g37-34977.webapp.163.com/challenge?callback=jQuery11130787183841296764_1482908955429'
    url = url + '&user_id=' + userid
    url = url + '&token=' + token
    url = url + '&share_page=' + share_page
    url = url + '&shop_id=' + shop_id
    # print url
    return url

def sendPost(url):
    req = urllib2.Request(url)
    request = urllib2.urlopen(req)
    html = request.read()
    handelHtml(html)

def handelHtml(html):
    pattern = r'"result": true'
    errors = re.findall(pattern, html)
    global totalcount
    if len(errors) > 0:
        totalcount = totalcount + 1


if __name__ == "__main__":
    count = len(userids)
    while True :
        totalcount = 0
        share_page = raw_input("share_page:")
        for x in xrange(0,count):
            for shop_id in xrange(1,9):
                url = makeUrl(userids[x], tokens[x], share_page, str(shop_id))
                sendPost(url)
        print 'success:' + str(totalcount)
