import tradingview_ta
from CryptoData import *
import time


def extractRSI(thisCoin):
    currentCoin = thisCoin.get_indicators()
    extractedRSI = currentCoin.get('RSI')
    return extractedRSI


def printAllRSIValues():
    for crypto in crypto_list:
        print(str(crypto.symbol) + ': 15 minute RSI is ' + str(extractRSI(crypto)))


def listRSIValues():
    RSIValues = []
    for crypto in crypto_list:
        thisRSI = (extractRSI(crypto))
        RSIValues.append(thisRSI)
    return RSIValues


def formatSymbol(thisCoin):
    symbol = thisCoin.symbol
    formattedSymbol = ''.join((symbol[0:-3], '-', symbol[-3:]))
    return formattedSymbol


def runNewReport():
    print('Running new report...')
    time.sleep(1)
    printAllRSIValues()
    print('')


def getAverageRSIOfMarket():
    runningTotal = 0.0
    for crypto in crypto_list:
        runningTotal += extractRSI(crypto)
    result = runningTotal / crypto_list.__len__()
    result = str(round(result, 2))
    return result


def printSplashText():
    print('\t\t\t\t\t ______________________________________' +
          '\n\t\t\t\t\t|                                      |'
          '\n\t\t\t\t\t|         PyTrader Version 1.1         |' +
          '\n\t\t\t\t\t|                 ***                  |'
          '\n\t\t\t\t\t|              Powered by:             |'
          '\n\t\t\t\t\t|       TradingView (Ver. ' + tradingview_ta.__version__ + ')      |'
          '\n\t\t\t\t\t|           CBPro (Ver. 1.1.4)         |'
          '\n\t\t\t\t\t|______________________________________|')