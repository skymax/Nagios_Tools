#################################################################
# #HOST_IP#
# HOST DEFINITION
#
#################################################################
 
# Define a host for the local machine
 
define host{
        use                     linux-server            ; Name of host template to use
              ; This host definition will inherit all variables that are defined
              ; in (or inherited by) the linux-server host template definition.
        host_name               #HOST_NAME#
        alias                   #HOST_NAME#(#MACHINE_NAME#)
        hostgroups              #HOST_GROUPS#
        address                 #HOST_IP#
        }
 
