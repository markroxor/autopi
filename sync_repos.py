import os
import requests

user_name = 'markroxor'
local_user = os.popen('whoami').read()[:-1]

os.popen('mkdir -p /home/' + local_user +'/Documents/repos')
os.chdir('/home/' + local_user +'/Documents/repos')
access_token = os.environ['PAT']

private_repos = requests.get(headers={"Authorization": "token " + access_token}, url="https://api.github.com/user/repos?visibility=private").json()
public_repos = requests.get(url="https://api.github.com/users/" + user_name + "/repos").json()

repos = private_repos + public_repos
for d in repos:
    if 'permissions' in d.keys():
        if not d['permissions']['admin']:
          continue
    elif d['fork']:
        continue

    try:
        os.popen('git clone '+ d['ssh_url'])
    except Exception as e:
        pass
    finally:
        print('syncing')
        os.popen('cd ' + d['name'] + ' && git pull --all && cd ..')
