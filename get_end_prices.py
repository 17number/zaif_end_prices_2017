from zaifdata.data.prices import DataReader
from datetime import datetime, timedelta
import time

# 通貨ペア(JPY建)
currency_pairs = [
  "mosaic.cms_jpy",
  "xem_jpy",
  "jpyz_jpy",
  "zaif_jpy",
  "mona_jpy",
  "bch_jpy",
  "fscc_jpy",
  "xcp_jpy",
  "cicc_jpy",
  "pepecash_jpy",
  "erc20.cms_jpy",
  "ncxc_jpy",
  "btc_jpy",
  "eth_jpy",
  "bitcrystals_jpy",
  "sjcx_jpy",
]

# 取得開始日
start_str = "2017-01-01 00:00:00"
start_date = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
start = int(time.mktime(start_date.timetuple()))

# 取得終了日
end_str = "2017-12-31 00:00:00"
end_date = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
end = int(time.mktime(end_date.timetuple()))

# 初期化
end_prices = {}
header = "Date"
for pair in currency_pairs:
  currency = pair.replace("_jpy", "").upper()
  header += "\t" + currency
  end_prices[currency] = {}
header += "\n"

# データ取得
for pair in currency_pairs:
  currency = pair.replace("_jpy", "").upper()
  data = DataReader(currency_pair=pair, period='1d', start=start, end=end)
  for d in data:
    date  = datetime.fromtimestamp(int(d['time'])).strftime("%Y/%m/%d")
    price = d['close']
    end_prices[currency][date] = price

# ファイル出力
f = open("ref_zaif_prices.tsv", "w")
f.write(header)
current_date = start_date
while current_date <= end_date:
  date = current_date.strftime("%Y/%m/%d")
  str = date
  for pair in currency_pairs:
    currency = pair.replace("_jpy", "").upper()
    str += "\t"
    if date in end_prices[currency]:
      str += end_prices[currency][date]
  str += "\n"
  f.write(str)
  current_date += timedelta(days=1)
f.close
  
