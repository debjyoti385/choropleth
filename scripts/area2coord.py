import urllib, urllib2, json
import csv

def  getGeocode(address):
        param_address =  address + ", India"
        params = {
                'address' : param_address,
                'sensor' : 'false',
        }  
        url = 'http://maps.google.com/maps/api/geocode/json?' + urllib.urlencode(params)
#        print url
        response = urllib2.urlopen(url)
        result = json.load(response)
#        print result
        try:
            output ={ address : { "full_address":result['results'][0]['formatted_address'], "address_components":result['results'][0]['address_components'],"boundary":result['results'][0]['geometry']['bounds'], "location":result['results'][0]['geometry']['location']}}
            return output
        except:
            o = {}
            return o

final_data = []
with open('../input/city.csv', mode='rU') as infile:
    reader = csv.reader(infile)
    name_dict = dict((rows[0],rows[1]) for rows in reader)

for key in name_dict:
    d = getGeocode(key)
    print d
    final_data.append(d)

with open("../output/area2coord.js","wb") as outfile:
    json.dump(final_data,outfile)
