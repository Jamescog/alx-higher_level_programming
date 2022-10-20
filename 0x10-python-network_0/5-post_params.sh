#!/bin/bash
# sends a POST request to passed URL
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
