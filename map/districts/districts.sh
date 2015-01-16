#!/bin/bash
pat1="\\\"ID_1\\\": "
pat2=","
header="{\"type\": \"FeatureCollection\",\"crs\": { \"type\": \"name\", \"properties\": { \"name\": \"urn:ogc:def:crs:OGC:1.3:CRS84\" } },\"features\": ["
for (( i = 1 ; i <= 35; i++ ))
do
    pattern=\"$pat1$i$pat2\"
    echo $pattern
    echo $header > $i.geojson
    command="grep $pattern india_district.geojson >> $i.geojson"
    echo "grep $pattern india_district.geojson >> $i.geojson"
    eval $command
    echo "]}" >> $i.geojson
done

