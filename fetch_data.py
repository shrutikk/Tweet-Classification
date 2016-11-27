import twitter
import pymongo
from pymongo import MongoClient

api = twitter.Api(consumer_key='SemVlbW0aFK0w1Lo87wuWLlwz',consumer_secret='3WaRdtbdNvLVtfu1NaN0ZmWrZzagvHtqrlLukfRXNFE5wHHxvc',access_token_key='784482147981819904-BqjQkaHrVVgC6APGf7y7WOOz799GPNa',access_token_secret='0N1pWYMO9n0tevN5LzRsIC43luylwp503xrrjHtWJpGk0')
statuses = api.GetUserTimeline(screen_name='@enews', count=200)

f = open('entertainmentnews','w')


for s in statuses:
   f.write(s.text.encode('utf-8').replace('\n','')+'\n')

maxid = statuses[199].id
statuses = api.GetUserTimeline(screen_name='@NBCSN', count=200, max_id=maxid)

for s in statuses:
   f.write(s.text.encode('utf-8').replace('\n','')+'\n')

maxid = statuses[199].id
statuses = api.GetUserTimeline(screen_name='@NBCSN', count=200, max_id=maxid)

for s in statuses:
   f.write(s.text.encode('utf-8').replace('\n','')+'\n')

maxid = statuses[199].id
statuses = api.GetUserTimeline(screen_name='@NBCSN', count=200, max_id=maxid)

for s in statuses:
   f.write(s.text.encode('utf-8').replace('\n','')+'\n')

maxid = statuses[199].id
statuses = api.GetUserTimeline(screen_name='@NBCSN', count=200, max_id=maxid)

for s in statuses:
   f.write(s.text.encode('utf-8').replace('\n','')+'\n')
