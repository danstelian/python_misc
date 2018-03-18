# Calculating with dictionaries

prices = {
    'BTC': 7727.92,
    'ETH': 520.55,
    'XRP': 0.60,
    'BCH': 918.08,
    'LTC': 148.72,
    'NEO': 58.25,
    'ADA': 0.14
}

# method 1
mi = min(prices.items(), key=lambda t: t[1])
ma = max(prices.items(), key=lambda t: t[1])
so = sorted(prices.items(), key=lambda t: t[1])
# print(f'min: {mi}\nmax: {ma}\nsort: {so}')

# method 2
mi = min(prices, key=lambda x: prices[x])

# method 3
ma = max(zip(prices.values(), prices.keys()))
so = sorted(zip(prices.values(), prices.keys()), reverse=True)
print(f'min: {mi}, {prices[mi]}\nmax: {ma}\nsort: {so}')
