#!/bin/bash
# sends a POST request to passed URL
curl -s --data 'email=test@gmail.com&subject=I will always be here for PLD' "$1"