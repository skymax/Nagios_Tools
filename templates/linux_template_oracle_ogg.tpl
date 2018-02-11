
define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     #OGG_DESC#
        check_command           check_nrpe!#OGG_CMD#
        }
