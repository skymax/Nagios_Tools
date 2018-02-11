class WeblogicConsole(object):
    type = "weblogic-console"

    def __init__(self, ip='', port=''):
        self.ip = ip
        self.port = port

    def __str__(self):
        return '(ip=%s,port=%s)' % (self.ip, self.port)
