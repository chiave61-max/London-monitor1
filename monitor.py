import yfinance as yf
import pandas as pd

# 1. Scarica i dati della Sterlina
ticker = "GBPUSD=X"
data = yf.download(ticker, period="2d", interval="15m")

# 2. Filtra la sessione Asia (00:00 - 07:00 ora UTC)
asia_data = data.between_time('00:00', '07:00')

high_asia = float(asia_data['High'].max())
low_asia = float(asia_data['Low'].min())
range_pips = (high_asia - low_asia) * 10000

# 3. Calcolo Livelli (Buffer 2 pips)
buy_trigger = high_asia + 0.0002
sell_trigger = low_asia - 0.0002
tp_buy = buy_trigger + (range_pips * 0.0001)
tp_sell = sell_trigger - (range_pips * 0.0001)

# 4. Risultato finale stampato nei log di GitHub
print(f"--- REPORT LONDON BREAKOUT ---")
print(f"Massimo Asia: {high_asia:.5f}")
print(f"Minimo Asia: {low_asia:.5f}")
print(f"Range: {range_pips:.1f} pips")
print(f"-------------------------------")
print(f"🟢 BUY STOP: {buy_trigger:.5f} | TP: {tp_buy:.5f}")
print(f"🔴 SELL STOP: {sell_trigger:.5f} | TP: {tp_sell:.5f}")
print(f"-------------------------------")
