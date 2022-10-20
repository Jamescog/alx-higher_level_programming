#!/bin/bash
# sends the reqeusted header using curl
curl -sLH "X-School-User-Id: 98" "$1"