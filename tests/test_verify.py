import fgrequests

urls = ['https://www.google.com']

response = fgrequests.build(urls, verify=False)

assert type(response) == list