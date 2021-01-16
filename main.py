# TODO

# show vti all
# show vti sector
# show all sector
# show [vti,ac,qqc.f] sector

# the first word determines the action
# the second word the stocks or list of stocks
# the third word the property in question.


# also important to have is:
# info ac percentage        fraction of my portfolio
# info ac shares
# info enb return           today's, this week's, month's, year's & totdal return
# info pfe cap              market capital
# info vdy summary

# history pfe 1w            I will need some terminal graphics and numpy here
# history enb 1d

import sys
import simplejson as json
import fileWriter as fw
import webScraper as ws
import trader as tdr
import screenWriter as sw
from abbreviations import *


def main():

    data = fw.loadData(fle)
    print(fle, 'loaded.')

    ans = ''
    while not ans == 'quit':
        ans = input('> ')
        an = ans.split()

        # empty argument
        if not ans:
            pass

        # buy
        elif an[0] == 'buy':
            ticker = an[1]
            number = int(an[2])
            if not ticker in data.keys():
                data[an[1]] = tdr.initialize(an[1])
            data[ticker][shr] += number
            print(ticker, 'shares:', data[ticker][shr])

        # sell
        elif an[0] == 'sell':
            ticker = an[1]
            number = int(an[2])
            if ticker in data.keys():
                if data[ticker][shr] >= number:
                    data[ticker][shr] -= number
                    print(ticker, 'shares:', data[ticker][shr])
                else:
                    print('Only', data[ticker][shr], 'shares in portfolio')

        # remove
        elif an[0] == 'remove':
            if an[1] in data.keys():
                del data[an[1]]
                print(an[1], 'removed')

        # watch
        elif an[0] == 'watch':
            if not an[1] in data.keys():
                data[an[1]] = tdr.initialize(an[1])
                print(an[1], 'added to your portfolio.')
            else:
                print('Warning:', an[1], 'already in your portfolio.')


        # summary
        elif ans == 'summary':
            sw.summary(data)

        # sector energy         shows details about the energy sector

        # sectors
        elif an[0] == 'sectors':
            tdr.sectors(data, an[-1])


        # show ac.to
        elif an[0] == 'show':
            sw.showStock(data, an[1])


        # save
        # save as
        elif ans == 'save':
            fw.dumpData(fle, data)
            print('data saved to', fle)

        # quit
        # check if changes have been saved
        elif ans == 'quit':
            break

if __name__ == "__main__":
    main()
