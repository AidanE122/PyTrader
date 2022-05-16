import cbpro, math, os, sys, time
from datetime import datetime
import tradingview_ta
from crypto_data import *


userData = open(os.path.join(sys.path[0], 'passphrase'), 'r').read().splitlines()
passphrase = userData[6]
secret = userData[9]
public = userData[12]
auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)


def printSplashText():
    print('\n\t\t\t\t\t ______________________________________' +
          '\n\t\t\t\t\t|                                      |'
          '\n\t\t\t\t\t|        PyTrader Version 1.2.3        |' +
          '\n\t\t\t\t\t|                  ***                 |'
          '\n\t\t\t\t\t|              Powered by:             |'
          '\n\t\t\t\t\t|       TradingView (Ver. ' + tradingview_ta.__version__ + ')      |'
          '\n\t\t\t\t\t|           CBPro (Ver. 1.1.4)         |'
          '\n\t\t\t\t\t|______________________________________|')


def initializeAPI():
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


def printAccountBalances():
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
                print('\t' + addPeriods(symbol) + '$' + str(thisBalance))


def getTotalAccountValue():
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


def calculate24HRVolume(thisCoin):
    tickerOfCoin = auth_client.get_product_ticker(addHyphenToSymbol(thisCoin))
    currentPriceOfCoin = (tickerOfCoin['price'])
    currentVolumeOfCoin = (tickerOfCoin['volume'])
    thisVolume = int((float(currentVolumeOfCoin)) * (float(currentPriceOfCoin)))
    return thisVolume


def placeMarketOrder(side, crypto, fiat):
    auth_client.place_market_order(product_id=addHyphenToSymbol(crypto),
                                   side=side,
                                   funds=fiat)


def getRSI(thisCoin):
    currentCoin = thisCoin.get_indicators()
    extractedRSI = currentCoin.get('RSI')
    return extractedRSI


def addHyphenToSymbol(thisCoin):
    symbol = thisCoin.symbol
    formattedSymbol = ''.join((symbol[0:-3], '-', symbol[-3:]))
    return formattedSymbol


def addSuffixToSymbol(currencyName):
    formattedString = currencyName + '-USD'
    return formattedString


def getAverageRSIOfMarket():
    runningTotal = 0.0
    for crypto in crypto_list:
        runningTotal += getRSI(crypto)
    result = runningTotal / crypto_list.__len__()
    result = str(round(result, 2))
    return result


def getAmountPerTrade(fiat):
    formattedAmount = str(round((math.floor(float(fiat) * 0.1)), 2))
    return formattedAmount


def getTime():
    now = datetime.now()
    current_time = now.strftime("[%H:%M:%S] ")
    return current_time


def wait(secs):
    time.sleep(secs)


def addPeriods(string):
    if len(string) == 7:
        return string + '.......'
    elif len(string) == 8:
        return string + '......'
    else:
        return string + '.....'


def printAccountValue(num1, num2):
    print('\nYour Coinbase Pro account value.................$' + str(num1))
    print('Market buys will be placed in increments of.....$' + str(num2) + '.00\n')
    print('#########################################################\n')
    time.sleep(4)


def isFiatAvailable(fiat):
    USDBalance = 0.0
    for currency in auth_client.get_accounts():
        if currency.get('currency') == 'USD':
            USDBalance = (round(float(currency.get('balance')), 2))
    if USDBalance >= fiat:
        return True
    else:
        return False


def getCryptoBalanceUSD(crypto):
    global USDBalance
    formattedSymbol = ''.join((crypto[0:-3], '-', crypto[-3:]))
    for currency in auth_client.get_accounts():
        if currency.get('currency') == crypto.removesuffix('USD'):
            currentBalance = currency.get('balance')
            currentPrice = auth_client.get_product_ticker(formattedSymbol).get('price')
            USDBalance = (round((float(currentBalance) * float(currentPrice)), 2))
    return str(USDBalance)

