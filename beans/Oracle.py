

class Oracle(object):

    type = "oracle"

    def __init__(self, ip='', sid='', port=''):
        self.sid = sid
        self.ip = ip
        self.port = port

    def __str__(self ):
        return '(ip=%s,sid=%s,port=%s)' % (self.ip, self.sid, self.port);
