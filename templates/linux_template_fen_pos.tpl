define service{ 
        use                     fenpos-service
        host_name               #HOST_NAME#
        service_description     #URL_DESC#
        check_command           check_nrpe!#URL_CMD#
        }

