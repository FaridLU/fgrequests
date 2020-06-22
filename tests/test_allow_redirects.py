import fgrequests

arr = ['https://gitlab.com/FaridLU/fgrequests']

response = fgrequests.build(arr, allow_redirects=True)
assert response[0].status_code == 200

response = fgrequests.build(arr, allow_redirects=False)
assert response[0].status_code != 200

response = fgrequests.build(arr)
assert response[0].status_code == 200
