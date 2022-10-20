#!/bin/bash
# Displays allowed HTTP request methods on given URL
curl -sX OPTIONS "$1"
