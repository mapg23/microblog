#!/bin/bash

NUM_REQUESTS=10
URL="https://mapg23.me"

echo "Sending $NUM_REQUESTS requests to $URL..."

for i in $(seq 1 $NUM_REQUESTS); do
    curl -s -o /dev/null -w "%{http_code}\n" -k -L "$URL"
done

echo "Done."
