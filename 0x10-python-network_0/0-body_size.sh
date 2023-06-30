#!/bin/bash
# displays the size of the body of the response
curl -sI "$1" | grep -iF 'content-length' | cut -b 17-
