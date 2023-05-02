name = input()
search_query = name.replace(' ', '+')
# base_url = 'https://www.amazon.com/s?k={0}'.format(search_query)
base_url = "https://www.flipkart.com/search?q={0}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off".format(
    search_query)
print(search_query)
print(base_url)
