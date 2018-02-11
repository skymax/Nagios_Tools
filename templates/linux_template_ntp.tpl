define service{ 
        use                     ntp-service
        host_name               #HOST_NAME#
        service_description     #NTP_DESC#
        check_command           check_nrpe!#NTP_CMD#
        }

