define service{
        use                     os-service
        host_name               #HOST_NAME#
        service_description     #DISK_DESC# Free Space
        check_command           check_nrpe!#DISK_CMD#
        }



