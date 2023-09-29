# HEXAGON Test Task
***

## Repository content
    
- ./requirements.txt - a set of modules required for the application
- ./simple_tests/ - directory containing simplified tests to check the basic functionality of the application
- ./src/ - source directory
- ./app.py - application startup script, add the '-h' switch to get the startup parameters

***
## Startup Examples
#### To run UDP-server on 50102 port with web-interface on 8000.
    ./app.py UDPS 8000 50102 

#### To run TCP-server on 50103 port with web-interface on 8090.
    ./app.py TCPS 8090 50103 

### API endpoints
#### GET-request to get all received messages
    <host_ipv4>/api/v1/stat/received

#### GET-request to get all sent messages
    <host_ipv4>/api/v1/stat/sent

#### POST-request to send message to another copy of application
    <host_ipv4>/api/v1/send

### POST-request format
#### * Text, surrounded by asterisks is explaining syntax and the idea of value *
    {
        "receiver": {
            "ipv4": * String, represents the delivery endpoint (UDP/TCP-server) IPv4 *, 
            "port": * Integer, represents the delivery endpoint (UDP/TCP-server) port *
        }, 
        "data": {
            "int_value" *Integer(<=4 bytes), Some useful load *,
            "string": * String(<=10 bytes), Some useful load *,
            "short_value" * Integer (<=2 bytes), Some useful load *
        }
    }
