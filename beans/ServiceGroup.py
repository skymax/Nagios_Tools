'''

@author: sky
'''

class ServiceGroup(object):
    '''
    classdocs
    '''

    type = 'servicegroup'
    def __init__(self, name="", alias=""):

        self.name = name
        self.alias = alias
    
    def get_Name(self):
        return self.name
        
    def get_Alias(self):
        return self.alias
        
    def set_Name(self,name):
        self.name = name
    
    def set_Alias(self,alias):
        self.alias = alias
    
    def __str__(self):
        return '(name=%s,alias=%s)' %(self.name, self.alias);