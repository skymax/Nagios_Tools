define service{ 
        use                     tcp-service
        host_name               #HOST_NAME#
        service_description     #CHECK_DESC#
        check_command           check_nrpe!#CHECK_CMD#
        }

