import time
import requests
import threading
import concurrent.futures as cf
from requests.adapters import HTTPAdapter

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def make_request(obj):
    session = get_session()
    session.mount(obj['url'], HTTPAdapter(max_retries=obj['max_retries']))

    data = {
        'method': obj['method'],
        'url': obj['url'],
        'timeout': obj['timeout'],
        'allow_redirects': obj['allow_redirects'],
    }
    
    data.update({'headers': obj['headers']}) if obj['headers'] else None
    data.update({'params': obj['data']}) if obj['data'] and obj['method'] == 'GET' else None
    data.update({'data': obj['data']}) if obj['data'] and obj['method'] != 'GET' else None
    data.update({'files': obj['files']}) if obj['files'] else None
    
    try:
        res = session.request(**data)
    except Exception as e:
        res = None
        
    return res

def build(url_list=[], headers=None, data=None, method='GET', files=None, worker=40, timeout=3, max_retries=1, allow_redirects=True, custom_request=False, show_execution_time=False):
    
    if custom_request:
        pass
    else:
        start_time = time.time()

        sites = [{'url': url, 'method': method, 'headers': headers, 'data': data, 'files': files, 'timeout': timeout, 'max_retries': max_retries, 'allow_redirects': allow_redirects} for url in url_list]
    
        response_list = []
        with cf.ThreadPoolExecutor(max_workers=worker) as executor:
            response_list  = list(executor.map(make_request, sites))

        duration = time.time() - start_time

        if show_execution_time:
            return {
                'response_list': response_list,
                'execution_time': round(duration, 3)
            }
        return response_list