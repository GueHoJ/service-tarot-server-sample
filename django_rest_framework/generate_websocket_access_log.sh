#!/bin/bash

# Log file path
LOGFILE="web_socket_access.log"

# Remove non-log lines
sed -i.bak '1d' $LOGFILE

# Run GoAccess
goaccess $LOGFILE \
    --log-format='%h:%^ - - [%d:%t] "%r" %s %b' \
    --date-format='%d/%b/%Y' \
    --time-format='%H:%M:%S' \
    -o ./templates/web_socket_access_report.html

