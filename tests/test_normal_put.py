import fgrequests

arr = ['https://google.com']

response = fgrequests.build(arr, method='PUT')
assert type(response) == list