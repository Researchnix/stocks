# trader
# all algorithms that handle the portfolio

from abbreviations import *
import webScraper as ws




# initialize a stock and add it with zero shares to the portfolio
def initialize(ticker):
    print('adding ', ticker, 'to the portfolio')
    asset = {}
    asset[tkr] = ticker
    asset['industry'] = ws.getIndustry(ticker)
    asset['sector'] = ws.getSector(ticker)
    asset['value'] = 10         # TODO
    asset[shr] = 0
    return asset








# computes the portion of the networth that is
# given by the list of stocks given in the list of tickers
def subWorth(data, tkrs):
    ans = 0
    for t in tkrs:
        ans += data[t][shr] * data[t][val]
    return ans





# computes the net worth based on number of shares in the portfolio
# and the current price of the stocks
def netWorth(data):
    ans = 0
    for k in data.keys():
        ans += data[k][shr] * data[k][val]
    if not ans == 0:
        return ans
    else:
        print('zero net worth!!')
        return 1



def sectors(data, flag):
    sec = {}
    for v in data.values():
        if not v[sct] in sec.keys():
            sec[v[sct]] = [v[tkr]]
        else:
            sec[v[sct]].append(v[tkr])

    print('')
    for s in sec.keys():
        print('###   ', s, ':  ', round(100 * subWorth(data,sec[s]) / netWorth(data), 2), '%')

        if flag == '-v':
            print('|')
            for t in sec[s]:
                print('*-', t, ':  ', round(100 * data[t][shr] * data[t][val] / netWorth(data), 2),'%')
            print('\n')
