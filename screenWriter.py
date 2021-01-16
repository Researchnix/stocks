# screenWriter

from abbreviations import *
import trader as tdr


def summary(data):
    if data.keys():
        for i in data.keys():
            print(i, ':', data[i][shr])
    else:
        print('portfolio is empty :(')


# displays all the data to one specific stock
def showStock(data, tkr):
    totalVal = data[tkr][shr] * data[tkr][val]
    print('-------- ', tkr.upper(), ' --------')
    print('Shares:        ', data[tkr][shr])
    print('Total Value:   ', totalVal, '$')
    print('Pctg:          ', round(100 * totalVal/tdr.netWorth(data), 2),'%')
    print('Sector:        ', data[tkr]['sector'])
    print('Industry:      ', data[tkr]['industry'])
    print('--------------------------')
