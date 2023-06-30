#!/bin/bash
# displays the body of the response
curl -sL -w "%{http_code}" -o /dev/null "$1" | [ "$(cat)" = "200" ] && curl -sL "$1"
