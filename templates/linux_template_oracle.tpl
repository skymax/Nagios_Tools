 
define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     check-oracle-tns
        check_command           check_nrpe!check_oracle_tns
        }

define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     check-oracle-login
        check_command           check_nrpe!check_oracle_login
        }

define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     check-oracle-db
        check_command           check_nrpe!check_oracle_db
        }

define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     check-oracle-jobs
        check_command           check_nrpe!check_oracle_jobs
        }



define service{
        use                     db-service
        host_name               #HOST_NAME#
        service_description     check-oracle-cache
        check_command           check_nrpe!check_oracle_cache
        }
