class Contact(object):
    '''
    classdocs
    '''

    type = "contact"


    def __init__(self, name="", use="", alias="", email="", phone_number="", weixinid=""):

        self.name = name
        self.alias = alias
        self.use = use
        self.email = email
        self.phone_number = phone_number
        self.weixinid = weixinid
    

    def __str__(self):
        return '(name=%s,alias=%s,use=%s,email=%s,phone_number=%s,weixindi=%s)' %\
               (self.name, self.alias,self.use,self.email,self.phone_number,self.weixinid);