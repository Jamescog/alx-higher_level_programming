#!/bin/bash
# sends a POST request to passed URL
curl -s -d email=test@gmail.com -d subject=I will always be here for PLD "$1"
