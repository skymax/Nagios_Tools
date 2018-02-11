

class Mail(object):

    type = "mail"

    def __init__(self, ip=''):
        self.ip = ip

    def __str__(self ):
        return '(ip=%s)' % (self.ip);
