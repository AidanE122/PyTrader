import sys
import os
from Console import *
import cbpro
import time

userData = open(os.path.join(sys.path[0], 'Passphrase'), 'r').read().splitlines()

passphrase = userData[7]
secret = userData[10]
public = userData[13]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)


def calculateVolume(thisCoin):
    tickerOfCoin = auth_client.get_product_ticker(formatSymbol(thisCoin))
    currentPriceOfCoin = (tickerOfCoin['price'])
    currentVolumeOfCoin = (tickerOfCoin['volume'])
    thisVolume = int((float(currentVolumeOfCoin)) * (float(currentPriceOfCoin)))
    return thisVolume


printSplashText()
time.sleep(4)

tradeVal = calculateAmountPerTrade(getAccountValue())
time.sleep(1)
print('\nProcessing request...')
time.sleep(4)

print('\n'
      'Please wait, getting average RSI of market...\n')
print('Average crypto market RSI is ' + str(getAverageRSIOfMarket()) + ' for '
      + str(crypto_list.__len__()) + ' total cryptocurrencies\n')
time.sleep(4)
print('Initializing crypto market scan...\n')
time.sleep(3)
print('Connection to Coinbase API successful. Market scanning will now begin.\n')
time.sleep(3)

"""
1. Buy if RSI is 30 or less and 24HR volume is 5 Mil. or greater
2. Sell if RSI is 70 or greater
3. Otherwise, cycle through list and look for trade
"""

while True:
    try:
        for crypto in crypto_list:
            if (extractRSI(crypto) <= 30) and (calculateVolume(crypto) >= 5000000):
                auth_client.place_market_order(product_id=formatSymbol(crypto),
                                               side='buy',
                                               funds=formatAmountPerTrade(tradeVal))
                print(getTime() + '\nAttempting to buy $' + str(tradeVal) + ' of ' + crypto.symbol + '\n')
                time.sleep(5)
            elif extractRSI(crypto) >= 70:
                auth_client.place_market_order(product_id=formatSymbol(crypto),
                                               side='sell',
                                               funds=(formatAmountPerTrade(tradeVal)))
                print(getTime() + '\nAttempting to sell $' + str(tradeVal) + ' of ' + crypto.symbol + '\n')
                time.sleep(5)
            else:
                time.sleep(8)
    except:
        print(getTime() + 'Network error, reconnecting in 1 min.')
        time.sleep(60)
        continue

# """
# 1. Cycle through list and look for trade
# 2. Sell if RSI is 70 or greater
# 3. Buy if RSI is 30 or less
# """
#
# while True:
#     try:
#         for crypto in crypto_list:
#             if 30 < extractRSI(crypto) < 70:
#                 print('Waiting...')
#                 time.sleep(8)
#             elif extractRSI(crypto) >= 70:
#                 auth_client.place_market_order(product_id=formatSymbol(crypto),
#                                                side='sell',
#                                                funds='50.00')
#                 print('\nAttempting to sell $50 of ' + crypto.symbol + '\n')
#                 time.sleep(5)
#             else:
#                 auth_client.place_market_order(product_id=formatSymbol(crypto),
#                                                side='buy',
#                                                funds='50.00')
#                 print('\nAttempting to buy $50 of ' + crypto.symbol + '\n')
#                 time.sleep(5)
#     except:
#         print('Network error, reconnecting in 1 min.')
#         time.sleep(60)
#         continue

