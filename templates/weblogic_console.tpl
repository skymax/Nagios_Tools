define service{
        use                     weblogic-service-jdbc
        host_name               #HOST_NAME#
        service_description     check-wls-console-#WLS_PORT#-JDBC
        check_command           check_nrpe!check_wls_console_#WLS_PORT#_JDBC
        }

define service{
        use                     weblogic-service-jvm
        host_name               #HOST_NAME#
        service_description     check-wls-console-#WLS_PORT#-JVM
        check_command           check_nrpe!check_wls_console_#WLS_PORT#_JVM
        }

define service{
        use                     weblogic-service-thread
        host_name               #HOST_NAME#
        service_description     check-wls-console-#WLS_PORT#-THREAD
        check_command           check_nrpe!check_wls_console_#WLS_PORT#_THREAD
        }
