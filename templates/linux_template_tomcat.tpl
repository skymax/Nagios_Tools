define service{
        use                     tomcat-service
        host_name               #HOST_NAME#
        service_description     check-wls-console-#WLS_PORT#-JDBC
        check_command           check_nrpe!check_tomcat_JDBC
        }

define service{
        use                     tomcat-service
        host_name               #HOST_NAME#
        service_description     check-wls-console-#WLS_PORT#-JVM
        check_command           check_nrpe!check_tomcat_JVM
        }

define service{
        use                     tomcat-service
        host_name               #HOST_NAME#
        service_description     check-wls-console-#WLS_PORT#-THREAD
        check_command           check_nrpe!check_tomcat_THREAD
        }

