# stocks


## stocks analysis program

still in its initial state and under heavy construction.






* ` summary`
    lists all stocks in portfolio and number of shares

* `show <stock>`
    shows all the data available about this stock

* `sectors`
    presents all sectors and the percentage of the overall portfolio

* `sectors -v`
    same in verbose mode

*  `buy <stock> <quantity>`
    adds shares of stock to portfolio

* `sell <stock> <quantity>`
    sells shares of stock from portfolio

* `watch <stock>`
    adds all the info of aapl to portfolio without shares

* `remove <stock>`
    removes the stock from the portfolio

* `save`
    saves the current portfolio to a file

* `quit`
    quits the program, but without saving



## examples

`> buy ac.to 4`
    buys 4 shares of Air Canada
`> buy aapl 2`
    buys 2 shares of Apple
`> sectors -v`
    prints out detailed information about the sectors in your portfolio
`> show ac.to`
    prints out information just about the Air Canada stock
`> save`
    writes any changes to the file portfolio.json
`> quit`
    exits the program



## TODO

* fetch current stock prices from the web
* add some terminal gui
* add more commands
