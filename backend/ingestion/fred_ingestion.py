from fredapi import Fred

fred = Fred(api_key="b214f48d6675f2a08e6de108659b44d8")

inflation = fred.get_series('CPIAUCSL')

print(inflation.tail())