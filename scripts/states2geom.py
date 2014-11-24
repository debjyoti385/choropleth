import json
import sys
import csv
import glob
import os

with open('../input/data.csv', mode='rU') as infile:
    reader = csv.reader(infile)
    data_dict = dict((rows[2],rows[1]) for rows in reader)

with open('../input/data.csv', mode='rU') as infile:
    reader = csv.reader(infile)
    name_dict = dict((rows[2],rows[0]) for rows in reader)

    

os.chdir("../input")
features = []
for file in glob.glob("*.txt"):
    filename = file 
    print "input : "+filename
    lines = [line.strip('\n') for line in open(file)]
    data = [line.split('|') for line in lines]
    data = lines[0].split('|')
    coordinates = [ map(float,d.split(','))  for d in data]
    try:
        value = data_dict[filename[:-4]] 
        name = name_dict[filename[:-4]] 
    except KeyError:
        value = 5
        name = filename[:-4]
    data = {"type":"Feature","id":filename[:-4],"properties":{"name":name,"density":value},"geometry":{"type":"Polygon","coordinates":[[ c for c in coordinates]]}}

    features.append(data)
#    with open("output/"+file+".js",'wb') as outfile:
#        json.dump(data,outfile)
final_data= {"type": "FeatureCollection","features":features}

with open("../output/final.js","wb") as outfile:
    outfile.write(" var statesData = ")

#with open("../output/final.js","ab") as outfile:
    json.dump(final_data,outfile)
