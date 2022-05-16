from console import *

printSplashText()
initializeAPI()

# 1. Buy if RSI is 30 or less and 24HR volume is 5 Mil. or greater
# 2. Sell if RSI is 70 or greater
# 3. Otherwise, cycle through list and look for trade

total = 1
while True:
    try:
        print('#########################################################\n')
        print(getTime() + 'Starting iteration #' + str(total) + '\n')
        printAccountBalances()
        tradingVal = getAmountPerTrade(getTotalAccountValue())
        printAccountValue(getTotalAccountValue(), tradingVal)
        for crypto in crypto_list:
            if ((getRSI(crypto) <= 30) and (calculate24HRVolume(crypto) >= 5000000)
                    and (isFiatAvailable(float(tradingVal)))):
                placeMarketOrder('buy', crypto, tradingVal)
                print(getTime() + 'Buying $' + str(tradingVal) + ' of ' + crypto.symbol + '\n')
                wait(5)
            elif getRSI(crypto) >= 70 and getCryptoBalanceUSD(crypto.symbol) > 0.00:
                balanceInUSD = getCryptoBalanceUSD(crypto.symbol)
                placeMarketOrder('sell', crypto, balanceInUSD)
                if float(balanceInUSD) > 0.00:
                    print(getTime() + 'Selling $' + balanceInUSD + ' of ' + crypto.symbol + '\n')
                wait(5)
            else:
                wait(8)
        total = total + 1
    except AttributeError:
        print(getTime() + 'Error: API information may be entered incorrectly.')
        sys.exit(1)
    except Exception:
        print(getTime() + 'Network error, reconnecting in 1 min.')
        wait(60)
        continue


