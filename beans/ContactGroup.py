class ContactGroup(object):


    type = 'contactgroup'

    def __init__(self, name='',alias='',members = []):

        self.name = name
        self.alias = alias
        self.members = members[:]


    def __str__(self):
        return '(name=%s,alias=%s,members=%s)' %\
               (self.name, self.alias,self.members)