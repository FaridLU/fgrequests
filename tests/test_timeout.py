import fgrequests

arr = ['https://wrongdomain.com']

response = fgrequests.build(arr, timeout=3)
assert type(response) == list
