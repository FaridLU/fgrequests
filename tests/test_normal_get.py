import fgrequests

arr = ['https://google.com']

response = fgrequests.build(arr)
assert type(response) == list