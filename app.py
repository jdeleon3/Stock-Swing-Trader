#!/usr/bin/env python3

import aws_cdk as cdk

from stock_swing_trader.stock_swing_trader_stack import StockSwingTraderStack


app = cdk.App()
StockSwingTraderStack(app, "StockSwingTraderStack")

app.synth()
