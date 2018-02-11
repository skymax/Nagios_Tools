#################################################################
# #HOST_IP#
# SERVICE DEFINITIONS
#
#################################################################
 
#mail pop
define service{
        use                     mail-service
        host_name               #HOST_NAME#
        service_description     mail pop
        check_command           check_pop
        }

#mail smtp
define service{
        use                     mail-service
        host_name               #HOST_NAME#
        service_description     mail smtp
        check_command           check_smtp
        }

#mail imap
#define service{
#        use                     mail-service
#        host_name               #HOST_NAME#
#        service_description     mail imap
#        check_command           check_imap
#        }

#http 
define service{
        use                     mail-service
        host_name               #HOST_NAME#
        service_description     mail http
        check_command           check_http
        }
