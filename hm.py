import requests
import pytest

#
#
# def get_response_in_json():
#     words = {'name': 'nicole'}
#     response = requests.post('https://httpbin.org/post', params=words)
#     # print(response.text)
#     print(response.json()['args'])
#     print(words)
#     json_response = response.json()
#     return json_response
#
#
# def test_compare_strings():
#     expected = {'name': 'nicole'}
#     json_res = get_response_in_json()  # the value of args key
#     actual = json_res['args']
#     assert actual == expected
#
#
# @pytest.mark.parametrize("username, password, response_code", [
#     ('bar', 12345, True), ('moshe', 12345, False), ('koshe', 12345, False)
# ])
# def test_auth(username, password, response_code):
#     url = 'https://httpbin.org/basic-auth/bar/12345'
#     assert response.ok == response_code
#     response = requests.get(url, auth=(username, password))
#
#
url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)
print(type(response.json()))
posts = response.json()
print(posts[2])