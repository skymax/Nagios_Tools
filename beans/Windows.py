'''
Created on 2017-12-9

@author: sky
'''

from Host import Host

class Windows(Host):
    '''
    classdocs
    '''

    type = "win"

    def __init__(self, group_name='', ip='',hostname=''):
        self.group_name = group_name
        self.ip = ip
        self.hostname = hostname

    def __str__(self):
        return '(ip=%s,hostname=%s,group_name=%s)' %(self.ip, self.hostname, self.group_name )