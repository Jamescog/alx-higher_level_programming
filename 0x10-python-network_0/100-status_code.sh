#!/bin/bash
# Gets only the status code of reques
curl -so /dev/null -w "%{http_code}" "$1"
