# Retrieving data from Kaggle 'Banks Historical Stock Price' and importing into Pandas
import pandas as pd

Historical_Stock_Price = pd.read_csv("AFL.csv")

print(Historical_Stock_Price.head())
print(Historical_Stock_Price.info())
print(Historical_Stock_Price.describe)
print(Historical_Stock_Price.columns)
print(Historical_Stock_Price.values)

# Analyzing Data
# Sort Historical_Stock_Price by descending Volume
Historical_Stock_Price_vol = Historical_Stock_Price.sort_values("Volume", ascending=False)
print(Historical_Stock_Price_vol.head())

# Sort Historical_Stock_Price by date, then descending Close Values
Historical_Stock_Price_date_close = Historical_Stock_Price.sort_values(["Date", "Close"], ascending=[True, False])
print(Historical_Stock_Price_date_close.head())

# Select High and Low Columns
Historical_Stock_Price_high_low = Historical_Stock_Price[["High", "Low"]]
print(Historical_Stock_Price_high_low.head())

# Filter for rows where Open Value is less than 10
Historical_Stock_Price_open = Historical_Stock_Price[(Historical_Stock_Price["Open"] < 10)]
print(Historical_Stock_Price_open)

# Index Historical_Stock_Price by Date
Historical_Stock_Price_ind = Historical_Stock_Price.set_index("Date")
print(Historical_Stock_Price_ind)
