import fgrequests

arr = ['https://google.com']

response = fgrequests.build(arr, method='POST')
assert type(response) == list