#!/bin/bash
#script that takes in a URL and displays all HTTP methods
curl -o /dev/null -sw "%{http_code}" $1
