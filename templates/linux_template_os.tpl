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
        check_command           check_nrpe!check_load
        }

#the number of currently logged
define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     Current Users
        check_command           check_nrpe!check_users
        }
       
#the free drive space . / . the remote host
define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     / Free Space
        check_command           check_nrpe!check_root
        }


#the total number of processes . the remote host.
define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     Total Processes
        check_command           check_nrpe!check_total_procs
        }
 
#the number of zombie processes . the remote host.
define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     Zombie Processes
        check_command           check_nrpe!check_zombie_procs
        }

define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     check-swap
        check_command           check_nrpe!check_swap
        }


#define service{
#        use                     os-service
#        host_name               #HOST_NAME#
#        service_description     check-Memory
#        check_command           check_nrpe!check_mem
#        }

