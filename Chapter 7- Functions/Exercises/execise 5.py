def describe_city(city, country='Morocco'):
    ("Describe a city.")
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Zagora')
describe_city('Abu hail', 'Dubai')
describe_city('Meknes')