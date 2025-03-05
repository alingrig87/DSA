#!/bin/bash

set -e

LANGUAGE=$1

if [ -z "$LANGUAGE" ]; then
    echo "Usage: $0 <language>"
    echo "Supported languages: cpp, java, js, python"
    exit 1
fi

install_dependencies() {
    case "$1" in
        cpp)
            sudo apt update && sudo apt install -y g++
            EXT="cpp"
            ;;
        java)
            sudo apt update && sudo apt install -y default-jdk
            EXT="java"
            ;;
        js)
            curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
            sudo apt install -y nodejs
            EXT="js"
            ;;
        python)
            sudo apt update && sudo apt install -y python3
            EXT="py"
            ;;
        *)
            echo "Unsupported language: $1"
            exit 1
            ;;
    esac
}

create_project_structure() {
    JSON_FILE="projectStructure.json"
    if [ ! -f "$JSON_FILE" ]; then
        echo "Error: $JSON_FILE not found!"
        exit 1
    fi

    while IFS= read -r line; do
        FOLDER=$(echo "$line" | jq -r '.folder')
        FILES=$(echo "$line" | jq -c '.files[]')

        mkdir -p "$FOLDER"
        for FILE in $FILES; do
            FILE_NAME=$(echo "$FILE" | jq -r '.name')
            echo "# $FILE_NAME" > "$FOLDER/$FILE_NAME.$EXT"
        done
    done < <(jq -c '.structure[]' "$JSON_FILE")
}

install_dependencies "$LANGUAGE"
create_project_structure

echo "Setup complete! Project structure created."
