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



