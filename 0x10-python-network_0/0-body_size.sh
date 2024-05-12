#!/bin/bash
# Curls request and display bytes received
curl -s "${1}" | wc -c
