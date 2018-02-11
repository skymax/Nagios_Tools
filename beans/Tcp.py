'''
Created on 2017-12-9

@author: sky
'''

class Tcp(object):
    
    type = 'tcp'
    def __init__(self, ip="", port=""):
        self.ip = ip
        self.port = port


    def __str__(self):
        return '(ip=%s,port=%s)' % (self.ip, self.port);
