import requests
post_data= {
    'option': 'dl-1',
    'pid': '142638',
    'ceck': 'sec',
    }



get_response = requests.get(url='http://google.com')
post_data = {'username':'joeb', 'password':'foobar'}
# POST some form-encoded data:
post_response = requests.get(url='http://warez-world.org/include/load.php', data=post_data)

print post_response.text