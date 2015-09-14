from api import api
import codecs
import json

user_follows, _next = api.user_follows()
user_follows_list = []
count = 0
while _next:
    more_follows, _next = api.user_follows(with_next_url=_next)
    user_follows.extend(more_follows)
    count += 1
    print count

for u in user_follows:
    user_follows_list.append(u.id)

with codecs.open('data/user_follows.json', 'w') as f:
    f.write(json.dumps(user_follows_list))

