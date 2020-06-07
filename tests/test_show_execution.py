import fgrequests

arr = ['https://google.com']

response = fgrequests.build(arr, method='POST', show_execution_time=True)
assert type(response) == dict
assert type(response['response_list']) == list