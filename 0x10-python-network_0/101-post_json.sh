#!/bin/bash
# sends file as post data
curl -X POST -d @"$2" -H "Content-Type: application/json" "$1"
