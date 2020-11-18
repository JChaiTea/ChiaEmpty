from USER import *
from ADVISOR import *
from ALLTD import *
from EMAIL import *

currentUser = users()
email = currentUser.getEmail()

print('''
                                    Welcome to the Chia Stock Advisor
                                    
                                    We currently have the following tools
                                                  Momentum
                                                Correlation
                          (Note that correlation can only be used with two equities)
                                                 Volatility
''')
watchlist = []

while True:
    ticker = input('Please continue to enter your tickers or hit enter to stop: ')
    if len(ticker) == 0:
        break
    else:
        watchlist.append(ticker)

tdInfo = tdAction()
quotes = tdInfo.quote(tickerList=watchlist)
volatilitys = tdInfo.quoteVolatility(tickerList=watchlist)
historicalData = tdInfo.history(tickerList=watchlist)
historicalDataDF = tdInfo.historyDF(tickerList=watchlist)
print('\n')

userStrats = []

print('Please choose one or more strategies to get a report on or hit enter to stop')
while True:
    strat = input('Enter here: ')
    print('\n')

    if len(strat) > 0:
        userStrats.append(strat.lower())
    else:
        break

adviseeData = advisor(dataset=historicalData, tickers=watchlist, dataFrames=historicalDataDF, volatilities=volatilitys)

emailMSG = f'Heres your stock Advice {currentUser.cUser}!\n\n'

if 'momentum' in userStrats:
    userMomentum = adviseeData.momentum()
    emailMSG = emailMSG + 'Momentum Advice:\n\n'
    momentumAdvice = {}
    for item in userMomentum:
        emailMSG = emailMSG + f'{userMomentum[item]}\n\n'
        momentumAdvice[item] = userMomentum[item]

if 'correlation' in userStrats:
    userCorrelation = adviseeData.correlation()
    emailResponseCorr = userCorrelation
    emailMSG = emailMSG + 'Correlation Advice:\n\n'
    emailMSG = emailMSG + f'{emailResponseCorr}\n\n'

if 'volatility' in userStrats:
    userVolatility = adviseeData.volatility()
    volatilityAdvice = {}
    emailMSG = emailMSG + 'Volatility Advice:\n\n'
    for item in userVolatility:
        emailMSG = emailMSG + f'{userVolatility[item]}\n\n'
        volatilityAdvice[item] = userVolatility[item]

sendAdvice = sendInfo(email=email, msg=emailMSG)
sendAdvice.sendIt()

