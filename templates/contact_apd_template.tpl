# #HOST_NAME# #SERVICE_DESC# #USER_GROUPS#
define serviceescalation{
                host_name #HOST_NAME#
                service_description #SERVICE_DESC#
                first_notification 1
                last_notification 0
                notification_interval 0
                contact_groups #USER_GROUPS#
                }

