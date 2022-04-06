from tradingview_ta import *

currentExchange = "COINBASE"
currentScreener = "crypto"
currentTimeInterval = Interval.INTERVAL_15_MINUTES
currentTimeoutValue = None

crypto_symbols = ['BTCUSD', 'ETHUSD', 'ADAUSD', 'DOGEUSD', 'AVAXUSD', 'DOTUSD', 'SHIBUSD', 'XTZUSD',
                  'SOLUSD', 'ICPUSD', 'LTCUSD', 'BCHUSD', 'EOSUSD', 'DASHUSD', 'OXTUSD', 'MKRUSD',
                  'XLMUSD', 'ENJUSD', 'ATOMUSD', 'AXSUSD', 'ETCUSD', 'OMGUSD', 'AMPUSD', 'ZECUSD',
                  'LINKUSD', 'BATUSD', 'CHZUSD', 'STXUSD', 'CROUSD', 'PAXUSD', 'QNTUSD', 'REPUSD',
                  'ZRXUSD', 'ALGOUSD', 'ZENUSD', 'LPTUSD', '1INCHUSD', 'MANAUSD', 'LOOMUSD',
                  'IMXUSD', 'KNCUSD', 'PERPUSD', 'CVCUSD', 'VGXUSD', 'ENSUSD', 'DNTUSD', 'DESOUSD',
                  'SPELLUSD', 'COMPUSD', 'MIRUSD', 'BANDUSD', 'OGNUSD', 'GALAUSD', 'NMRUSD',
                  'TRIBEUSD', 'IOTXUSD', 'SUPERUSD', 'CGLDUSD', 'FETUSD', 'UMAUSD', 'FORTHUSD',
                  'LRCUSD', 'CLVUSD', 'FXUSD', 'YFIUSD', 'FIDAUSD', 'POLYUSD', 'COTIUSD', 'UNIUSD',
                  'RENUSD', 'ORNUSD', 'WBTCUSD', 'BALUSD', 'NUUSD', 'RADUSD', 'ALCXUSD', 'YFIIUSD',
                  'TRUUSD', 'FILUSD', 'BONDUSD', 'CTSIUSD', 'KEEPUSD', 'AAVEUSD', 'TRACUSD', 'RLCUSD',
                  'BADGERUSD', 'GRTUSD', 'BNTUSD', 'AUCTIONUSD', 'RLYUSD', 'AGLDUSD', 'NKNUSD',
                  'POLSUSD', 'MLNUSD', 'SNXUSD', 'GODSUSD', 'API3USD', 'IDEXUSD', 'SUSHIUSD',
                  'MATICUSD', 'WCFGUSD', 'SKLUSD', 'GTCUSD', 'DDXUSD', 'PROUSD', 'TRBUSD', 'ERNUSD',
                  'MASKUSD', 'POWRUSD', 'RARIUSD', 'ANKRUSD', 'XYOUSD', 'CRVUSD', 'BTRSTUSD', 'RGTUSD',
                  'STORJUSD', 'MUSDUSD', 'ORCAUSD', 'QUICKUSD', 'REQUSD', 'LQTYUSD', 'ARPAUSD',
                  'HIGHUSD', 'ALICEUSD', 'AERGOUSD', 'SNTUSD', 'SYNUSD', 'BICOUSD', 'GLMUSD', 'AIOZUSD',
                  'RNDRUSD', 'QSPUSD', 'GFIUSD', 'LCXUSD', 'FARMUSD', 'BLZUSD', 'JASMYUSD', 'MPLUSD',
                  'DIAUSD', 'RBNUSD', 'SUKUUSD', 'RAIUSD', 'WLUNAUSD', 'CTXUSD', 'ASMUSD', 'FOXUSD',
                  'UNFIUSD', 'INVUSD', 'KRLUSD', 'MDTUSD', 'COVALUSD', 'AVTUSD', 'GYENUSD', 'NCTUSD',
                  'PLUUSD', 'ACHUSD', 'UPIUSD', 'SHPINGUSD', 'PLAUSD', 'MCO2USD', 'APEUSD', 'CRPTUSD', ]

# Adding soon : MINAUSD
# Last date checked : Mar. 24

crypto_list = []


def createCrypto(symbol):
    newCrypto = TA_Handler(
        symbol=symbol,
        exchange=currentExchange,
        screener=currentScreener,
        interval=currentTimeInterval,
        timeout=currentTimeoutValue
    )
    crypto_list.append(newCrypto)


for cryptoSymbol in crypto_symbols:
    createCrypto(cryptoSymbol)
