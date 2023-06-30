#!/bin/bash
# URL and displays all HTTP methods the server will accept.
curl -sIL -X OPTIONS "$1" | grep -iF "allow" | cut -b 8-
