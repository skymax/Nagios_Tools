'''
Created on 2017-12-9

@author: sky
'''

class Disk(object):
    
    type = 'disk'
    def __init__(self, ip="", pathname=""):

        self.ip = ip
        self.pathname = pathname
    
    def __str__(self):

        return '(ip=%s,pathname=%s)' % (self.ip, self.pathname);
