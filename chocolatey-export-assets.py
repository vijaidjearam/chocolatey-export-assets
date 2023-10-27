import requests

url = 'http://choco.local.xxx.xxx.fr/service/rest/v1/assets'

def download(url,filename):
    filename = filename.replace('/','.')
    filename = filename+'.nupkg'
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

def getdatacontinuation(url,continuationToken):
    headers = {
    'accept': 'application/json',
    'X-Nexus-UI': 'true',
    }

    params = {
    'repository': 'chocolatey-hosted',
    'continuationToken': continuationToken
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json()
    
    
# Each request gives a page 10 items - The next page can be found if the response has continuationToken

headers = {
    'accept': 'application/json',
    'X-Nexus-UI': 'true',
}

params = {
    'repository': 'chocolatey-hosted',
}

response = requests.get(url, params=params, headers=headers)
resp = response.json()
list = resp['items']
for item in list:
    print(item['downloadUrl'])
    print(item['path'])
    download(item['downloadUrl'],item['path'])
    
#End of first page
    
#Loop until the end of the Page

while resp['continuationToken']:
    resp = getdatacontinuation(url,resp['continuationToken'])
    list = resp['items']
    for item in list:
        print(item['downloadUrl'])
        print(item['path'])
        download(item['downloadUrl'],item['path'])
    
