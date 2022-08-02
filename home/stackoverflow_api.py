import requests

"""Calling stackoverflow api"""
def stackoverflowapi(search: str = None):
    if search is None:
        # search='how to use stackoverflow api'
        search=''
    url=f'https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={search}&site=stackoverflow'
    result=requests.get(url=url)
    return result.content