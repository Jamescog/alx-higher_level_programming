#!/bin/bash
# post with json file
curl -sd @"$2" "$1"
