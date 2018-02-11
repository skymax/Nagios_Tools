'''
Created on 2017-12-9

@author: sky
'''

class Log(object):
    
    type = 'log'
    def __init__(self, ip="", desc="", pattern=""):

        self.ip = ip
        self.desc = desc
        self.pattern = pattern


    def __str__(self):

        return '(ip=%s,desc=%s,pattern=%s)' % (self.ip, self.desc, self.pattern);
