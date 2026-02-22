# Create a function named get_capital that takes two parameters: country_capitals (a dictionary) and country_name (a string). The function should return the capital city of the given country name using the country_capitals dictionary.

def get_capital(country_capitals, country_name):
    capital=country_capitals[country_name]
    print(capital)