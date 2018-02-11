'''
Created on 2017-12-9

@author: sky
'''

class Url(object):

    type = 'url'
    def __init__(self, ip="", port="",url = ""):
        self.ip = ip
        self.port = port
        self.url = url
    
    
    def __str__(self):
        return '(ip=%s,port=%s,url=%s)' % (self.ip, self.port, self.url);
