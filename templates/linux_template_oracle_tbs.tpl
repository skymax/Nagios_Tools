
define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     #TBS_DESC#
        check_command           check_nrpe!#TBS_CMD#
        }
