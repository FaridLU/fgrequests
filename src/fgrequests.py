import time
import concurrent.futures as cf
import requests
import threading

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def make_request(obj):
    session = get_session()

    data = {
        'method': obj['method'],
        'url': obj['url'],
    }
    
    data.update({'headers': obj['headers']}) if obj['headers'] else None
    data.update({'params': obj['data']}) if obj['data'] and obj['method'] == 'GET' else None
    data.update({'data': obj['data']}) if obj['data'] and obj['method'] != 'GET' else None
    
    try:
        res = session.request(**data)
    except Exception as e:
        res = None
        
    return res

def build(url_list=[], headers=None, data=None, method='GET', worker=40, custom_request=False, show_execution_time=False):
    
    if custom_request:
        pass
    else:
        start_time = time.time()

        sites = [{'url': url, 'method': method, 'headers': headers, 'data': data} for url in url_list]
    
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