from api import api
import codecs
import json
import time

def write_state(users):
    with codecs.open('data/not_matched_user.json', 'w') as f:
        f.write(json.dumps(users))

not_matched_user = []
with codecs.open('data/not_matched_user.json', 'r') as f:
    not_matched_user = json.loads(f.read())

count = 0
while not_matched_user:
    u = not_matched_user.pop()
    api.unfollow_user(user_id=u)
    count += 1
    print 'Unfollow {user}, iter: {iters}'.format(user=u, iters=count)
    
    write_state(not_matched_user)
    time.sleep(301)

