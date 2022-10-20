#!/bin/bash
# Displays allowed HTTP request methods on given URL
curl -sI "$1" | grep "Allow" | cut -d " "-f 2-