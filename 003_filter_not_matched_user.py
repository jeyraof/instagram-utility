from api import api
import codecs
import json

user_follows = []
user_followed = []

with codecs.open('data/user_follows.json', 'r') as f:
    user_follows = json.loads(f.read())

with codecs.open('data/user_followed.json', 'r') as f:
    user_followed = json.loads(f.read())
    
not_matched_user = [u for u in user_follows if u not in user_followed]
with codecs.open('data/not_matched_user.json', 'w') as f:
    f.write(json.dumps(not_matched_user))

