
<img src="https://github.com/AidanE122/PyTrader/blob/main/PyTrader.png" width="557" height="163">

Welcome, and thank you for using PyTrader!

Please make sure you read all the way through this document as well as 
'packages.txt' before starting PyTrader. This will help to reduce potential
errors when setting up the bot.

Please make sure you have the newest version of Python installed before
proceeding any further through the instructions...
(Latest Python version can be downloaded from https://www.python.org/downloads/)

Before you start up the "start_PyTrader.bat" file, you will need to make sure 
your Coinbase Pro API information is entered correctly in the "passphrase" file. 
This can be done through the Notepad app that comes installed on Windows. API 
information should be entered as shown below in order for the program to connect
to your Coinbase Pro account and compile correctly. Please make sure that you give
your Coinbase Pro API permission to view and trade in order for PyTrader to be 
able to place trades.

Example:

Enter your API credentials in the space below each question:
-----------------------------------------------
Nickname:                 
Name that you would like to give this API
-----------------------------------------------
Passphrase:               
Your passphrase here
-----------------------------------------------
API Secret Key:               
Your API Secret Key here
-----------------------------------------------
API Public Key:               
Your API Public Key here
-----------------------------------------------

NOTE: The "nickname" field does not have to be the same as the one you gave to
your API on your Coinbase Pro account, you can enter whatever name you would like. 
This is only included so you can more easily remember which API you have linked 
to PyTrader.

Once your API information has been entered, simply double-click "start_PyTrader.bat"
in order to start the trader. If you wish to disable PyTrader, just exit out of the 
program and all trades will be halted until you choose to run the program again.

Just a reminder, PyTrader is still a very new program, and there is still an enormous
amount of features and tweaks that I would like to make to it before I am somewhat
satisfied with it. As for now, RSI-based indicator trading is the only option that I 
have implemented, but I plan on adding many more forms of indicators within the future.
Please feel free to send me an email at aidaneicholz@gmail.com or reach out to me on 
GitHub if you notice any bugs or errors. I would be happy to sort them out and find the
best solutions that I can.

Big thanks to Dan Paquin, creator of the Coinbase Pro API for Python, as well 
as Brian The Dev, who created TradingView-TA for Python.
