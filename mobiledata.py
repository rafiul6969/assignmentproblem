mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'}
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
import random

mobile_dict = mobile_data['data'][2]
name = mobile_dict['name']
origin = mobile_dict['made']
usd_price = float(mobile_dict['price'].split(' ')[0])
exchange_rate = mobile_data['exchnage_rate']
bdt_price = round(usd_price*exchange_rate)

sentence_one = [f'Introducing the latest featured {name}. ']
sentence_two = [f'It is from the tech land {origin}. ']
sentence_three = [f'Grab it soon only on {usd_price} USD which is almost equal to {bdt_price} BDT. ']

templete_list = random.choice(sentence_one) + random.choice(sentence_two) + random.choice(sentence_three)
print(templete_list)