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


def printHolds():
    for currency in auth_client.get_accounts():
        if currency.get('currency') == 'USD':
            USDBalance = (round(float(currency.get('balance')), 2))
            print('\tUSD-USD.......' + '$' + str(USDBalance))
        elif float(currency.get('balance')) > 0.0:
            symbol = addSuffixToSymbol(currency.get('currency'))
            retrieveData = auth_client.get_product_ticker(symbol)
            price = retrieveData.get('price')
            thisBalance = (round((float(price) * float(currency.get('balance'))), 2))
            if thisBalance > 1.00:
                print('\t' + addDots(symbol) + '$' + str(thisBalance))


def getAccountTotal():
    accountTotal = 0
    balances = []
    for currency in auth_client.get_accounts():
        if currency.get('currency') == 'USD':
            USDBalance = (round(float(currency.get('balance')), 2))
            balances.append(USDBalance)
        elif float(currency.get('balance')) > 0.0:
            symbol = addSuffixToSymbol(currency.get('currency'))
            retrieveData = auth_client.get_product_ticker(symbol)
            price = retrieveData.get('price')
            thisBalance = (round((float(price) * float(currency.get('balance'))), 2))
            balances.append(thisBalance)
    for balance in balances:
        accountTotal = accountTotal + balance
    return round(accountTotal, 2)


def calculateVolume(thisCoin):
    tickerOfCoin = auth_client.get_product_ticker(formatSymbol(thisCoin))
    currentPriceOfCoin = (tickerOfCoin['price'])
    currentVolumeOfCoin = (tickerOfCoin['volume'])
    thisVolume = int((float(currentVolumeOfCoin)) * (float(currentPriceOfCoin)))
    return thisVolume


def printAccountValue(num1, num2):
    print('\nYour Coinbase Pro account value............$' + str(num1))
    print('Trades will be placed in increments of.....$' + str(num2) + '.00\n')
    print('###################################################\n')
    time.sleep(4)


printSplashText()
time.sleep(4)

print('\n\nConnecting to your Coinbase Pro API...')
time.sleep(3)
print('\nPlease wait, getting average RSI of market...\n')
print('Average crypto market RSI is ' + str(getAverageRSIOfMarket()) + ' for '
      + str(crypto_list.__len__()) + ' total cryptocurrencies.\n')
time.sleep(4)
print('Initializing crypto market scan...\n')
time.sleep(4)
print('Connection to Coinbase API successful. Market scanning will now begin.\n')
print('--------------------------------------------------------------------------\n')
time.sleep(3)

"""
1. Buy if RSI is 30 or less and 24HR volume is 5 Mil. or greater
2. Sell if RSI is 70 or greater
3. Otherwise, cycle through list and look for trade
"""

total = 1
while True:
    try:
        print('###################################################\n')
        print(getTime() + 'Starting iteration #' + str(total) + '\n')
        printHolds()
        tradingVal = calculateAmountPerTrade(getAccountTotal())
        printAccountValue(getAccountTotal(), tradingVal)
        for crypto in crypto_list:
            if (extractRSI(crypto) <= 30) and (calculateVolume(crypto) >= 5000000):
                auth_client.place_market_order(product_id=formatSymbol(crypto),
                                               side='buy',
                                               funds=formatAmountPerTrade(tradingVal))
                print(getTime() + 'Attempting to buy $' + str(tradingVal) + ' of ' + crypto.symbol + '\n')
                time.sleep(5)
            elif extractRSI(crypto) >= 70:
                auth_client.place_market_order(product_id=formatSymbol(crypto),
                                               side='sell',
                                               funds=(formatAmountPerTrade(tradingVal)))
                print(getTime() + 'Attempting to sell $' + str(tradingVal) + ' of ' + crypto.symbol + '\n')
                time.sleep(5)
            else:
                time.sleep(8)
        total = total + 1
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
