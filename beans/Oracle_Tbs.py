'''
Created on 2017-12-9

@author: sky
'''

class Oracle_Tbs(object):
    '''
    classdocs
    '''

    type = "oracle-tbs"

    def __init__(self, ip='', sid='', tbs=''):
        self.sid = sid
        self.ip = ip
        self.tbs = tbs

    def __str__(self):
        return '(ip=%s,sid=%s,tbs=%s)' % (self.ip, self.sid, self.tbs);
