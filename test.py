import requests, json, pprint

url = 'http://127.0.0.1:5000/r270/update';
headers = {'Content-Type': 'application/json'}
data = requests.get(url, headers=headers)

'''
# Convert bytes to string type and string type to dict
string = response.read().decode('utf-8')
json_obj = json.loads(string)

print(json_obj['source_name']) # prints the string with 'source_name' key
'''

#binary = data.content
#output = json.loads(data.text)
print (data.content)
output = json.loads(data.content)
print "%s\n\n" % data.json() 

print output
print "======> id: %s" % (output['id'])
print "======> error: %s" % (output['error'])

#pprint.pprint(output)

"""
import json, requests, pprint

url = 'http://maps.googleapis.com/maps/api/directions/json?'

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)


data = requests.get(url=url, params=params)
print "%s\n\n" % data.json() 

binary = data.content
output = json.loads(binary)

# test to see if the request was valid
#print output['status']

# output all of the results
#pprint.pprint(output)

# step-by-step directions
for route in output['routes']:
        for leg in route['legs']:
            for step in leg['steps']:
                print step['html_instructions']

"""
