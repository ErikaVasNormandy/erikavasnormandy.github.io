#!/bin/bash

max_size_mb=1

for file in *.{png,jpg,jpeg,gif}; do
    if [ -e "$file" ]; then
        file_size=$(wc -c < "$file")
        file_size_mb=$(echo "scale=2; $file_size / 1024 / 1024" | bc)

        while (( $(echo "$file_size_mb >= $max_size_mb" | bc -l) )); do
            convert "$file" -resize "90%" "$file"
            file_size=$(wc -c < "$file")
            file_size_mb=$(echo "scale=2; $file_size / 1024 / 1024" | bc)
        done

        echo "File: $file | Size: $file_size_mb MB"
    fi
done
