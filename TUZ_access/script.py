import json
import requests
import urllib3
import argparse

def token(metabase_user, metabase_pass):
    headers = {'Content-Type': 'application/json'}
    json_data = {'username': metabase_user, 'password': metabase_pass}
    response = requests.post('https://ссылка.ru/api/session', headers=headers, json=json_data,
                             verify=False)
    token = json.loads(response.text)
    token = token['id']
    return token


def getMetabaseSqlTemplate(token, questionId):
    headers = {'X-Metabase-Session': token}
    url = 'https://ссылка.ru/api/card/' + questionId + '/query/json'
    response = requests.post(url, headers=headers, verify=False)
    response = json.loads(response.text)
    return response


def checkRepo(USERNAME, PASSWORD):
    error = []
    done = []
    for i in range(len(getMetabase)):
        name = getMetabase[i]["name"]
        url = getMetabase[i]["url"]
        branch = getMetabase[i]["version"]
        updated_dt = getMetabase[i]["updated_dt"]
        url_row = url.split("/")
        if url_row[2] == "ссылка.ru":
            url = "https://ссылка.ru/" + str(url_row[4]) + "/repos/" + str(
                url_row[5][0:-4]) + "/archive?format=zip"
            params = {'at': f'{branch}'}
            response = requests.get(url, verify=False, params=params, auth=(f'{USERNAME}', f'{PASSWORD}'))
            if response.status_code == 200:
                tmp = f'Доступ есть; {response.status_code}; {name}; {updated_dt}; {url}'
                done.append(tmp)
            else:
                tmp = f'Доступа нет; {response.status_code}; {name}; {updated_dt}; {url}'
                error.append(tmp)
        elif url_row[2] == "ссылка.ru":
            product = str(url_row[5])
            product = product[int(0): int(-4)]
            url = "https://ссылка.ru/" + str(url_row[4]) + "/repos/" + str(
                product) + "/archive?format=zip"
            params = {'at': f'{branch}'}
            response = requests.get(url, verify=False, params=params, auth=(f'{USERNAME}', f'{PASSWORD}'))
            if response.status_code == 200:
                tmp = f'Доступ есть; {response.status_code}; {name}; {updated_dt}; {url}'
                done.append(tmp)
            else:
                tmp = f'Доступа нет; {response.status_code}; {name}; {updated_dt}; {url}'
                error.append(tmp)

    print(
        "==============================================================================================================================")
    for i in range(len(error)):
        print(error[i])
    print(
        "==============================================================================================================================")
    for i in range(len(done)):
        print(done[i])
    print(
        "==============================================================================================================================")


parser = argparse.ArgumentParser()
parser.add_argument('--metabase_user', help='username for metabase', type=str)
parser.add_argument('--metabase_pass', help='password for metabase', type=str)
args = parser.parse_args()
metabase_user = args.metabase_user
metabase_pass = args.metabase_pass

USERNAME = '3333333'
PASSWORD = '333'
questionId = '3568'

urllib3.disable_warnings()
token = token(metabase_user, metabase_pass)
getMetabase = getMetabaseSqlTemplate(token, questionId)
result = checkRepo(USERNAME, PASSWORD)
