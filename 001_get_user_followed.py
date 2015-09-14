from api import api
import codecs
import json

user_followed, _next = api.user_followed_by()
user_followed_list = []
count = 0
while _next:
    more_followed, _next = api.user_followed_by(with_next_url=_next)
    user_followed.extend(more_followed)
    count += 1
    print count

for u in user_followed:
    user_followed_list.append(u.id)

with codecs.open('data/user_followed.json', 'w') as f:
    f.write(json.dumps(user_followed_list))

