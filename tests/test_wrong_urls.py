import fgrequests

arr = ['https://googl.com'] * 5

response = fgrequests.build(arr)
assert type(response) == list