

#################################################################
# #HOST_IP#
# SERVICE DEFINITIONS
#
#################################################################
 
#CPU load
define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     CPU Load
        check_command           check_nrpe!alias_cpu
        }
       
#the free drive space . / . the remote host
define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     c: Free Space
        check_command           check_nrpe!alias_disk_c
        }

 

define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     check-memory
        check_command           check_nrpe!alias_mem
        }

define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     System Up Time
        check_command           check_nrpe!alias_up
        }

