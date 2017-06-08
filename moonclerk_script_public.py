import urllib.request
import urllib.parse
import json
import pprint 
import re

count = 100
offset = 0


"""
Loops and gets 700 entries. Change range to bigger numbers to get a higher number of plans 
"""
for index in range(0,8):
#    
#    print(offset)
#    print(index)
#    
    #headers for the API request
    params = urllib.parse.urlencode({"count": count, "offset": offset})
    
    #print("params is", params)
    
    #API call, returns data in JSON format. Insert your API key on the Token token field
    opener = urllib.request.build_opener()
    opener.addheaders = [('Authorization','Token token='), ('Accept','application/vnd.moonclerk+json;version=1')]
    response = opener.open('https://api.moonclerk.com/customers?%s' % params)
    html = response.read()
    customers = html.decode("utf-8")
    
    #PrettyPrint the JSON 
    pp = pprint.PrettyPrinter(indent=4)
    customers_parsed = pp.pformat(customers)
    
    #eliminates single quote and double spacing from the JSON

    customers_parsed2 = re.sub("'", ' ', customers_parsed)

    customers_parsed3 = " ".join(customers_parsed2.split())
        
    #set filename  
    filename = "customer_json%s.txt" % index
    
    #Saves the JSON data onto a text file
    f = open(filename, "a+")
    f.write(customers_parsed3)
    
    offset += 100
    index += 1

f.close()
