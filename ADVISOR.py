import pandas


class advisor(object):
    """The advisor for the client"""

    def __init__(self, dataset, tickers, dataFrames, volatilities):
        """Constructor"""
        self.data = dataset
        self.watchlist = tickers
        self.dataFrames = dataFrames
        self.volatilies = volatilities

    def momentum(self):
        """Check the momentum of an equity"""
        highMomentum = {}
        for item in self.data:
            highMomentum[item] = []
            df = pandas.DataFrame(data=self.data[item])
            average = int(df.mean())
            for num in self.data[item]:
                if type(num) != None:
                    if num > average:
                        highMomentum[item].append(num)
        retMomentum = {}
        for key in highMomentum:
            if len(highMomentum[key]) >= 5:
                retMomentum[key] = f'{key}\'s Momentum is great. This year is looking good for {key}, add it to the ' \
                                   f'portfolio and watch the capital roll in '
            elif 5 < len(highMomentum[key]) >= 3:
                retMomentum[key] = f'{key}\'s Momentum is okay. This might be the beginning of a great ' \
                                         f'momentum run though, I would advise checking how the equity has ' \
                                         f'performed against the broader sector, then deciding whether or not to ' \
                                         f'add it to your portfolio.'
            elif 3 > len(highMomentum[key]) >= 1:
                retMomentum[key] = f'{key}\'s Momentum is not there. It doesnt seem to be {key}\'s time ' \
                                         f'to shine right now, but watch it for the next month and see if it ' \
                                         f'starts to perform.'
            else:
                retMomentum[key] = f'{key} does not currently hold any momentum. {key} is really not ' \
                                         f'performing, do your research on why that is, knowing this may ' \
                                         f'prove more useful than you know'
        return retMomentum

    def correlation(self):
        """Check the Correlation of equities"""

        correlation = float(self.dataFrames[1].corrwith(self.dataFrames[2]))
        ticks = []
        elab = ''
        for item in self.data:
            ticks.append(item)
        response = f'The correlation between {ticks[0]} and {ticks[1]} is {correlation:.2f}. '
        if -0.5 < correlation < 0:
            elab = 'This would suggest a somewhat inverse correlation. You might see potential opportunities for ' \
                   'swings in these equities\' prices.'
        if -1 <= correlation < -0.5:
            elab = 'This would suggest a strong inverse correlation. You should definitely take advantage of the ' \
                   'swings present in these equities\' prices, if one goes down look to check the momentum of the ' \
                   'other and take action.'
        if 0 < correlation < 0.5:
            elab = 'This would suggest a somewhat positive correlation. These stocks can be paired together in a ' \
                   'portfolio, but make sure to balance their weights since one may not bring up the other all the ' \
                   'time.'
        if 0.5 < correlation <= 1:
            elab = 'This would suggest a strong positive correlation. Definitely pair these two together when the ' \
                   'momentum calls for it, these two performing in tandem within your portfolio, suggests prime ' \
                   'opportunity.'
        return response + elab

    def volatility(self):
        """Get the volatility recommendation for equities"""
        retDict = {}
        for item in self.volatilies:
            if (self.volatilies[item] * 1000) < 10:
                retDict[item] = f'{item}\'s volatility of {int(self.volatilies[item] * 1000)}% is very low. A ' \
                                      f'very low volatility would suggest that the equity is not going to move ' \
                                      f'sporadically, this is a good equity for long term holding. '
            if 35 > (self.volatilies[item] * 1000) > 10:
                retDict[item] = f'{item}\'s volatility of {int(self.volatilies[item] * 1000)}% is low. A low ' \
                                      f'volatility would suggest that selected equity is probably a growth company ' \
                                      f'with a relatively high price, though its expensive this is a great equity for ' \
                                      f'long term portfolio growth. '
            if 60 > (self.volatilies[item] * 1000) > 35:
                retDict[item] = f'{item}\'s volatility of {int(self.volatilies[item] * 1000)}% is somewhat ' \
                                      f'high. A somewhat high volatility implies general concern for sporadic price ' \
                                      f'movements in the equity, I would advise monitoring and balancing your ' \
                                      f'portfolio with respect to this equities movement. '
            if 100 > (self.volatilies[item] * 1000) > 60:
                retDict[item] = f'{item}\'s volatility of {int(self.volatilies[item] * 1000)}% is very high. A ' \
                                      f'very high volatility is cause for concern, I would really suggest closely ' \
                                      f'watching this equities movements while in your portfolio, think about ' \
                                      f'implementing a stop loss order, or adding price alerts. But if you plan on ' \
                                      f'trading on big swings here, its a recipe for potential gain.'
        return retDict
