# zaif_end_prices_2017
Zaifの通貨ペアの終値取得

## 注意/免責事項
本コード、およびデータの利用は自己責任でお願いします。
本コード、およびデータを利用したことにより発生した不利益などに関しては、一切の保証は致しません。

## 使い方

### 事前準備
[zaifdata](https://github.com/techbureau/zaifdata)を使っているので、事前にインストールとかクローンしておいてください。

```
pip instal zaifdata
```

or

```
git clone https://github.com/techbureau/zaifdata.git
```

### 使い方

```
python get_end_prices.py
```

#### 細かい使い方
コードの変更箇所を示します。行数まで書かないので自分で探してください。

##### 取得期間を変更したい
```python
start_str = "2017-01-01 00:00:00"
```
```python
end_str = "2017-12-31 00:00:00"
```
を変更してください。

##### 取得間隔(分足、時間足、日足)を変更したい
```python
  data = DataReader(currency_pair=pair, period='1d', start=start, end=end)
```
上記の `period='1d'` を変更してください。[zaifdata のコード](https://github.com/techbureau/zaifdata/blob/b5693a7648d340338261742aa8d1063c27c51a72/zaifdata/data_source.py#L29)を見たところ、使えるのは以下と思われます。(未検証)

|period|単位|
|----|-----|
|1m|1分足|
|5m|5分足|
|15m|15分足|
|30m|30分足|
|1h|1時間足|
|4h|4時間足|
|8h|8時間足|
|12h|12時間足|
|1d|1日足|


##### 終値じゃない値が欲しい
```python
  for d in data:
    date  = datetime.fromtimestamp(int(d['time'])).strftime("%Y/%m/%d")
    price = d['close']
    end_prices[currency][date] = price
```
この辺とか
```python
  for pair in currency_pairs:
    currency = pair.replace("_jpy", "").upper()
    str += "\t"
    if date in end_prices[currency]:
      str += end_prices[currency][date]
  str += "\n"
  f.write(str)
```
この辺をいじってください。

なお `DataReader` で取れる情報は以下のフォーマットになっています。
```
{'volume': '0.0', 'average': '13.2', 'high': '13.2', 'low': '13.2', 'time': '1483196400', 'close': '13.2', 'open': '13.2'}
```
