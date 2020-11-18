from config import CONSUMER_KEY, REDIRECT_URL, ACCT_NUM
from td.client import TDClient
from pandas import *


class tdAction(object):
    """Main action class for all td functions"""

    def __init__(self):
        """Constructor"""
        self.conKey = CONSUMER_KEY
        self.redirect = REDIRECT_URL
        self.acct = ACCT_NUM
        self.tdClient = TDClient(client_id=self.conKey, redirect_uri=self.redirect)
        self.tdClient.login()

    def quote(self, tickerList):
        """Grab quotes"""
        retDict = {}
        quotes = self.tdClient.get_quotes(instruments=tickerList)
        for key in quotes:
            if type(quotes[key]['lastPrice']) is not None:
                retDict[key] = quotes[key]['lastPrice']
        return retDict

    def history(self, tickerList):
        """Create real time data for a given list of tickers"""
        retDict = {}
        for item in tickerList:
            tickerHistory = self.tdClient.get_price_history(symbol=item, period_type='year')
            priceHistory = []
            for data in tickerHistory['candles']:
                priceHistory.append(data['close'])
            retDict[item] = priceHistory
        return retDict

    def historyDF(self, tickerList):
        """Create real time data for a given list of tickers"""
        retDict = {}
        counter = 0
        for item in tickerList:
            counter += 1
            tickerHistory = self.tdClient.get_price_history(symbol=item, period_type='year')
            priceHistory = []
            for data in tickerHistory['candles']:
                priceHistory.append(data['close'])
            df = pandas.DataFrame(priceHistory)
            retDict[counter] = df
        return retDict

    def quoteVolatility(self, tickerList):
        """Grab quotes"""
        retDict = {}
        quotes = self.tdClient.get_quotes(instruments=tickerList)
        for key in quotes:
            if type(quotes[key]['volatility']) is not None:
                retDict[key] = quotes[key]['volatility']
        return retDict
