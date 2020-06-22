# FGrequests: Fastest Asynchronous Group Requests

[![PyPI version fury.io](https://badge.fury.io/py/fgrequests.svg)](https://pypi.org/project/fgrequests/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/fgrequests.svg)](https://pypi.python.org/pypi/fgrequests/)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)

# Installation

Install using pip:

```bash
pip install fgrequests
```

# Documentation

Pretty easy to use.

```python
import fgrequests

urls = [
    'https://google.com',
    'https://facebook.com',
    'https://twitter.com',
    'https://linkedin.com',
    'https://fakedomain.com'
]
```

Now lets make requests at the same time to the list of URLs (`urls`)

```python
>>> response = fgreuests.build(urls)
>>> print(response)
[<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, None]

```

By default `fgrequests.build()` returns a list of responses. If there have any invalid URL, the response will be `None`.

## Method

By default this `build()` using `GET` method. There is a parameter which accepts methods named `method`. You can change this according to your need. `method` will accept these: `GET`, `POST`, `PUT`, `DELETE`, `PATCH`.

Lets send `POST` request in all of the `urls`

```python
>>> response = fgreuests.build(urls, method='POST')
>>> print(response)
[<Response [405]>, <Response [200]>, <Response [200]>, <Response [200]>, None]
```

## Headers

If you want to pass any `headers` you can simply pass your `headers` object (which may contain the authentication information) if you do like this:

```python
>>> headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    "Authorization": "Bearer XXXXXXXXXXXXXXXTOKEN"
}
>>> response = fgreuests.build(urls, headers=headers)
```

## Params/Payload

If you want to pass additional information while making requests, just pass your `params` / `payload` by following way:

```python
>>> data = {
    'username': 'farid'
    'password': 'password123'
}
>>> response = fgreuests.build(urls, data=data)
```

## Worker

It has another parameter `worker`. By default the value of `worker` is `40`. If you increase this it will work more faster. But there is a problem if you increase this too much, this will make a lot of pressure in your `CPU` cores which may freeze your system. If you reduce the value of `worker` you this will take more time to return responses. You can change the value of worker like this:

```python
>>> response = fgreuests.build(urls, worker=70)
```

## POST a Multipart-Encoded File

You can simply to upload Multipart-encoded files by using `files` parameter:

```python
>>> urls = ['https://httpbin.org/post']
>>> files = {'file': open('report.xls', 'rb')}

>>> response = fgrequests.build(urls, method='POST', files=files)
>>> response[0].text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

You can set the filename, content_type and headers explicitly:
```python
>>> urls = ['https://httpbin.org/post']
>>> files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

>>> response = fgrequests.build(urls, method='POST', files=files)
>>> response[0].text
{
  ...
  "files": {
    "file": "<censored...binary...data>"
  },
  ...
}
```

If you want, you can send strings to be received as files:

```python
>>> urls = ['https://httpbin.org/post']
>>> files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}

>>> response = fgrequests.build(urls, method='POST', files=files)
>>> response[0].text
{
  ...
  "files": {
    "file": "some,data,to,send\\nanother,row,to,send\\n"
  },
  ...
}
```

## Timeout

You can set timeout for the group request by using another parameter `timeout`. By default the value of `timeout` is `3` which is in seconds. You can change the value of `timeout` like this:

```python
>>> response = fgreuests.build(urls, timeout=5)
```

## Max Retries

You can put the count of maximum retries (to handle worst scenario) by using `max_retries` parameter. By default the value of `max_retries` is `1`. You can change the value of `max_retries` like this:

```python
>>> response = fgreuests.build(urls, max_retries=3)
```

## Allow Redirects

You can disable redirection handling with the `allow_redirects` parameter. It only accepts `Boolean`, either `True` or `False`. By default it is `True`. You can change this by following way:

```python
>>> response = fgreuests.build(urls, allow_redirects=False)
```

## Execution Time

There have another parameter named `show_execution_time`. It returns the execution time (in sec). It accepts `Boolean`, either `True` or `False`. By default it is `False`. If you change this to `True` then `fgrequests.build()` will return an `object`. Lets check the output by making `show_execution_time` to `True`:

```python
>>> response = fgrequests.build(urls, show_execution_time=True)
>>> print(response)
{
    'response_list': [<Response [200]>, <Response [200]>, <Response [200]>, <Response [200]>, None],
    'execution_time': 1.677
}
```


# Support

You may report bugs, ask for help, and discuss various other issues on the [bug tracker][].

[bug tracker]: https://github.com/faridlu/fgrequests/issues
