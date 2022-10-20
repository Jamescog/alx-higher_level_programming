#!/bin/bash
# Displays allowed HTTP request methods on given URL
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-
