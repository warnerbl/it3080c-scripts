#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
PENDING=$(echo $DATA | jq '.[0].pending')
HOSPITALIZEDNOW=$(echo $DATA | jq '.[0].hospitalizedCurrently')
DEATHS=$(echo $DATA | jq '.[0].death' )
ONVENTILATORNOW=$(echo $DATA | jq '.[0].onVentilatorCurrently')

echo "On $TODAY, there were $POSITIVE positive COVID cases, $PENDING pending tests, $HOSPITALIZEDNOW currently hospitalized, $DEATHS deaths, $ONVENTILATORNOW on ventilator currently."
