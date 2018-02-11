###############################################################################
# WINDOWS.CFG - SAMPLE CONFIG FILE FOR MONITORING A WINDOWS MACHINE
#
# Last Modified: 06-13-2007
#
# NOTES: This config file assumes that you are using the sample configuration
#        files that get installed with the Nagios quickstart guide.
#
###############################################################################




###############################################################################
###############################################################################
#
# HOST DEFINITIONS
#
###############################################################################
###############################################################################

# Define a host for the Windows machine we'll be monitoring
# Change the host_name, alias, and address to fit your situation

define host{
        use             windows-server  ; Inherit default values from a template
        host_name               #HOST_NAME#
        alias                   #HOST_NAME#(#MACHINE_NAME#)
        hostgroups              #HOST_GROUPS#
        address                 #HOST_IP#
        }



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
