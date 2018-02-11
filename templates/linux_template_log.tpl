define service{ 
        use                     log-service
        host_name               #HOST_NAME#
        service_description     #LOG_DESC#
        check_command           check_nrpe!#LOG_CMD#
        }

