# -*- coding: utf-8 -*-
## PACKAGE IMPORT ##
# Packages needed to run the code
import json, ast 		# Packages used for processing JSON file
import requests			# Package used to post and handle HTPP request and response

## DATASTREAMX KEY ##
# Keys from DataStreamX to authenticate the request
DataStreamXKey = "[INSERT YOUR DATASTREAMX KEY]"

## API URL ##
# URL to hit with HTTP request
apiURL = "http://api.datastreamx.com/1925/605/v1/odmatrix/v2/query"

## QUERY PARAMETER ##
# Query statement with all the parameters
queryBody = {
	"date": "2017-10-27",
	"timeSeriesReference": "origin",

	# Location to area to query and its granularity
	"location": {
		"locationType": "locationHierarchyLevel",
		"levelType": "origin_subzone",
		"id": "OTSZ02"
	},

	# Time granularity to query
	"queryGranularity": {
		"type": "period",
		"period": "P1D"
	},
	
	# Facet the result based on the following attribut
	"dimensionFacets": [
		"agent_nationality"
	],
	# Aggregation method used in the query
	"aggregations": [{
			"metric": "unique_agents",
			"type": "hyperUnique"
		},
		{
			"metric": "total_records",
			"type": "longSum"
		}
	]
}

## FIRING HTTP REQUEST ##
# Make a HTTP request using the requests package and save the result in a variable
queryResponse = requests.post(
	apiURL, 
	data = json.dumps(queryBody),
	headers = {
		'DataStreamX-Data-Key': DataStreamXKey, 
		'Content-Type': 'application/json'
	}
)

# Parsing the response and printing it
result = [ast.literal_eval(json.dumps(i)) for i in queryResponse.json()]
print result

## EXPORTING TO CSV ##
# Part of code to export the result of the query into CSV
output = './output.csv'		# Output directory

# Parsing JSON into CSV
with open(output, 'w') as wf:
	wf.write("timestamp,gender,race,origin subzone,total records,unique agents" + '\n')
	for record in result:
		times = record['timestamp']
		event = record['event']
		agent_nationality = event['agent_nationality']
		origin_subzone = event['origin_subzone']
		longSum_total_records = event['longSum_total_records']
		hyperUnique_unique_agents = event['hyperUnique_unique_agents']
		output_line = [times, agent_nationality, origin_subzone, longSum_total_records, hyperUnique_unique_agents]
		output_line = ','.join(map(str, output_line))
		wf.write(output_line + '\n')