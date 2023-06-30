#!/bin/bash
# post request with json data
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
