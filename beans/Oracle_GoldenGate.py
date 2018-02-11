'''
Created on 2018-1-18

@author: sky
'''

class Oracle_GoldenGate(object):
    '''
    classdocs
    '''
    type = 'oracle goldengate'
    #ip|goldengate_path|goldengate_process

    def __init__(self, ip='', goldengate_path='', goldengate_process=''):
        self.ip = ip
        self.goldengate_path = goldengate_path
        self.goldengate_process = goldengate_process

    def __str__(self):
        return '(ip=%s,goldengate_path=%s,goldengate_process=%s)' % (self.ip, self.goldengate_path, self.goldengate_process);
