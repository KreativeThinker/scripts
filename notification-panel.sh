#!/bin/bash

FILE=~/.scripts/notification_history.py
echo "S = \\" > $FILE
dunstctl history >> $FILE
cat ~/.scripts/output_function.py >> $FILE
