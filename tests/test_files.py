import fgrequests


# Send file through request
urls = ['https://httpbin.org/post']
files = {'file': open('requirements.txt', 'rb')}

response = fgrequests.build(urls, method='POST', files=files)
assert type(response) == list

'''
print(response[0].text)
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
'''

urls = ['https://httpbin.org/post']
files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

response = fgrequests.build(urls, method='POST', files=files)
assert type(response) == list
'''
print(response[0].text)
{
  ...
  "files": {
    "file": "some,data,to,send\nanother,row,to,send\n"
  }, 
  ...
}
'''

