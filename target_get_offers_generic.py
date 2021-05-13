import json
import requests
import secrets

#dict of test users
user_dict = {
	"gabe": '123',
	"paul": '456',
	"adam": '789'
	}

#select which user you want to run
test_user = user_dict.get("paul")

#generate a random session id
session = secrets.token_urlsafe(16)

#test urls
playball 	= 'https://beta-gcp.xzy.com/?playball'
umpire 		= 'https://beta-gcp.xzy.com/?umpire'
strikezone 	= 'https://beta-gcp.xzy.com/?strikezone'
beta_home 	= 'https://beta-gcp.xzy.com/homepage/test'

#mboxes
gtm = 'global-target-mbox'
tgm = 'target-global-mbox'

#entities
old = '724a7668-3452-46fd-b143-9e5c528f85a9'
yanks = '13de9407-92c3-41a6-a51a-95ea96207698'
spanish_cubs = '5720954a-953d-4305-973b-ea45d03bb3b0'

# setup delivery call
headers = {
	'Accept': 'application/json'
}

url_base = "https://xzy.tt.omtrdc.net/rest/v1/delivery"

params = {
  "client": "xzy",
  "sessionId": session
}

body = {
	"environmentId": 1358,
	"id": {
		"thirdPartyId": test_user
	},
	"context": {
		"channel": "web",
		"address": {
			"url": playball
		},
		"screen": {
			"width": 1200,
			"height": 1400
		}
	},
	"prefetch": {
		"mboxes": [{
			"name": gtm,
			"index": 0,
			"parameters": {
				"entityId": '724a7668-3452-46fd-b143-9e5c528f85a9',
				"entityLanguage": "en-us"
			}
		}]
	}
}

# make the request
res = requests.post(url_base, headers=headers, params=params, json=body)
res_json = res.json()
print(res_json)

# check the request
print ("the raw json is: \n\n", res.json()['prefetch']['mboxes'][0]['options'][0]['content'])
print ("the raw json is: \n\n", res.json()['prefetch']['mboxes'][0]['options'][0]['responseTokens'])
print ("the raw json is: \n\n", res.json()['prefetch'])

# fetch the json and transform it inside python json.loads

print ("\nLet's fetch some recs...\n\n")
recs = res.json()['prefetch']['mboxes'][0]['options'][0]['content']
user = res.json()['prefetch']['mboxes'][0]['options'][0]['responseTokens']
recs = json.loads(recs)


# try traversing the JSON

"""
print("the notes are: \n\n", recs['adobeRecommendations']['notes'], "\n\n")
print("the items are: \n\n", recs['adobeRecommendations']['recommendedItems'], "\n\n")
print("the details are: \n\n", recs['adobeRecommendations']['activityDetails'], "\n\n")
print("the visitor is: \n\n", recs['adobeRecommendations']['visitorProfile'], "\n\n")
print("the recKey is: \n\n", recs['adobeRecommendations']['recKey'], "\n\n")
print("the details recs are: \n\n", recs['adobeRecommendations']['recDetailedResults'], "\n\n")
"""

# turn each blob into it's own variable
notes   = recs['adobeRecommendations']['notes']
items   = recs['adobeRecommendations']['recommendedItems']
details = recs['adobeRecommendations']['activityDetails']
visitor = recs['adobeRecommendations']['visitorProfile']
#recKey  = recs['adobeRecommendations']['recKey']
results = recs['adobeRecommendations']['recDetailedResults']

### all of the variables are dictionoaries

"""
print (type(notes))
print (type(items))
print (type(details))
print (type(visitor))
print (type(recKey))
print (type(results))
"""

# begin accessing values inside the blobs
print ("your user info:\n")
print ("Your test user was: ", list(user_dict.keys())[list(user_dict.values()).index(test_user)])
print ("The okta ID is: ", user['profile.thirdPartyId'])
#print ("The preferred team ID is: ", user['profile.preferredTeamId'])
#print ("The already-seen-entities are: ", user['profile.alreadySeenEntities'])
print ("your geo-location is: ", user['geo.dma'], " | ", user['geo.state'], " | ", user['geo.country'], " | ", user['geo.zip'])
print ("your session ID was: ", session)
print ("\n")

print ("your Adobe Target info:\n")
print ("The Campaign Name is: ", details['campaign.name'])
print ("The Recipe is: ", details['campaign.recipe.name'])
print ("The Criteria title is: ", details['criteria.title'])
print ("The Algorithm name is: ", details['algorithm.name'])
print ("The Activity ID is: ", details['x'], ":", details['campaign.recipe.id'])
print ("\n")

### the list of keys
#print (list(results.keys()))
#print (list(results.items()))

### naive way of fetching results
#print (results['recEntity1Details']['slug'])
#print (results['recEntity2Details']['slug'])
#print (results['recEntity3Details']['slug'])
#print (results['recEntity4Details']['slug'])
#print (results['recEntity5Details']['slug'])

### use a for loop to determine number of non-null recs
store = 0

for x in items.values():
	if len(x) == 36:
		store = store + 1

print ("There were", store, "recommended items for this request\n\n")

### use for loop to fetch results
print ("your recs are:\n")

#print(recs)
#print(items)

for key in results.keys():
	print(key, '|', results[key]['slug'], '|', results[key]['teamId'], '|', results[key]['contentDate'])
