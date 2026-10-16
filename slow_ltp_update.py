import yfinance as yf
from xlsx import xlsx_update

try:
    nifty = yf.Ticker("^NSEI")
    price = float(nifty.fast_info["last_price"])
    if price > 0:
        xlsx_update('c8', price, 'main.xlsx')
except Exception:
    pass