import fgrequests

arr = ['https://google.com']

response = fgrequests.build(arr, method='DELETE')
assert type(response) == list