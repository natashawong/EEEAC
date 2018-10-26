import requests
from app.envirionments import ENVIRONMENTS

def tester(url):
    """tests a given URL to see if it is active and returns True or False"""
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    try:
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
            print("ok")
            return True
        else:
            print('did not connect: ' + str(r))
            return False
    except Exception as e:
        print('error encountered (' + str(e) + ')- check URL')
        return False


def refresh(tab):
    """takes an environment name and returns every entry in that environment after adding a 'status'
    entry based on if the connection was successful.
    Also returns data used to add extra blank tabs (count and a list of numbers for jinja to work through"""
    posts = ENVIRONMENTS[tab]
    count = 0
    for i in range(0, len(posts)):
        count += 1
        print("loading " + posts[i]['name'] + ' --- ' + str(count) + '/' + str(len(posts)))  # loading name --- 1/8
        posts[i]['test'] = tester(posts[i]['appLink'])
    return posts, count, list(range(0, 8-count))       # returns both the data and the value the count of boxes that need to be populated to (list is a workaround for jinja)
