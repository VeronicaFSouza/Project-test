# Retrieving datasets from Kaggle and importing into Pandas
import pandas as pd

AFL_bank = pd.read_csv("AFL.csv")

print(AFL_bank.head())
print(AFL_bank.info())
print(AFL_bank.describe)
print(AFL_bank.columns)
print(AFL_bank.values)

JPMorgan = pd.read_csv("JPM.csv")
print(JPMorgan.head())
print(JPMorgan.columns)
print(JPMorgan.info())

# Analyzing Data

# Sorting AFL Bank by descending Volume
AFL_bank_vol = AFL_bank.sort_values("Volume", ascending=False)
print(AFL_bank_vol.head())

# Sorting AFL Bank by date, then descending Close Values
AFL_bank_date_close = AFL_bank.sort_values(["Date", "Close"], ascending=[True, False])
print(AFL_bank_date_close.head())

# Selecting High and Low Columns
AFL_bank_high_low = AFL_bank[["High", "Low"]]
print(AFL_bank_high_low.head())

# Filtering for rows where Open Value is less than 10
AFL_bank_vol_open = AFL_bank[(AFL_bank["Open"] < 10)]
print(AFL_bank_vol_open)

# Indexing AFL Bank by Date
AFL_bank_ind = AFL_bank.set_index("Date")
print(AFL_bank_ind)

# Using Slicing to get columns 3 to 4
print(JPMorgan.iloc[0:, 2:4])

# Adding a Column Open minus Close for JPMorgan
JPMorgan["JPMorgan_minus"] = JPMorgan["Open"] - JPMorgan["Close"]
print(JPMorgan)

# Printing the median of Adj Close for JPMorgan
print(JPMorgan["Adj Close"].median())

# Grouping JPMorgan by Date
JPMorgan_by_date = JPMorgan.groupby("Date")["High"].agg([min, max, sum])
print(JPMorgan_by_date)


