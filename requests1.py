import requests

response = requests.get('https://v6.exchangerate-api.com/v6/2d5181a34075a821c4631a8b/latest/USD')

# code = response.status_code
# code = (code // 100 )
#
# if code == 4 :
#    print('something went wrong')
# else:
#    print('google is awesome')


if response.ok:
    print(response.status_code)
    data = response.json()
    print(data['conversion_rates']['ILS'])
else:
    print(response.status_code)
# with open('robot.png','wb') as im:
#    im.write(response.content)   # downloading pic from google