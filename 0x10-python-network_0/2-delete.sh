#!/usr/bin/env bash
# Sends a DELETE request to URL passed as first argumet
# and displays the body of the response
curl -X DELETE http://$1
