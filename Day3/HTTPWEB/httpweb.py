"""REST API for retrieving the names of the repositories and their languages of a user's GitHub account """
import sys
import requests

response = requests.get('https://api.github.com/users/muhallan/repos')

if response.status_code != 200:
    print("error fetching repositories from https://api.github.com/users/muhallan/repos: {}".format(response.status_code),
          file=sys.stderr)
else: 
    for repo in response.json():
        print ('[{}] {}'.format(repo['language'], repo['name']))
