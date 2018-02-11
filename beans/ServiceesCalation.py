
class ServiceesCalation(object):
    # HOST_NAME# #SERVICE_DESC# #USER_GROUPS#

    type = 'serviceescalation'

    def __init__(self, host_name='', service_desc='', user_groups=[]):
        self.host_name = host_name
        self.service_desc = service_desc
        self.user_groups = user_groups[:]

    def __str__(self):
        return 'host_name=%s,service_desc=%s,user_groups=%s)' % (self.host_name,self.service_desc,self.user_groups)
