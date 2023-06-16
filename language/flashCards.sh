#!/bin/bash

echo "https://www.polishpod101.com/polish-word-lists/?list=1"
echo "https://www.polonista.pl/jutro"
read

LOOP=""
PREVIOUS=0
FILE="${1:-flashCards.csv}"
ORDER="${2:-r}"
LANGUAGE_DIR="${3:-italian}"

IFS=$'\n'
while [ "$LOOP" == "" ]; do
  for i in $(shuf "$LANGUAGE_DIR/$FILE"); do
    LANGUAGE=$(echo "$i" | cut -d ',' -f1)
    ENGLISH=$(echo "$i" | cut -d ',' -f2)
    printf '\n%.0s' $(seq 1 $(tput lines))
    if [ "$ORDER" = "e" ]; then
      printf "%s" "$ENGLISH"
      read
      printf "%s" "$LANGUAGE"
      read
    elif [ "$ORDER" = "p" ]; then
      printf "%s" "$LANGUAGE"
      read
      printf "%s" "$ENGLISH"
      read
    elif [ "$ORDER" = "r" ]; then
      CHOICE=$((1 + $RANDOM % 100))
      if [ "$CHOICE" -gt 50 ]; then
        printf "%s" "$ENGLISH"
        read
        printf "%s" "$LANGUAGE"
        read
      else
        printf "%s" "$LANGUAGE"
        read
        printf "%s" "$ENGLISH"
        read
      fi
    fi
  done
done

