# to run this code, yfinance and pandas libraries are required
# install yfinance by running "pip install yfinance"
# install pandas by running "pip install pandas"

# version
# versions are as follows
# pip 23.2.1
# yfinance 0.2.37
# pandas 2.0.3

# As an example, we will download the stock price data of the TOPIX Core 30 stocks from Yahoo Finance.
# Stock codes comprising TOPIX Core 30

# 3382.T = "Seven & i Holdings Co., Ltd."
# 4063.T = "Shin-Etsu Chemical Co., Ltd."
# 4502.T = "Takeda Pharmaceutical Company Limited"
# 4503.T = "Astellas Pharma Inc."
# 4568.T = "Daiichi Sankyo Company, Limited"
# 6098.T = "Recruit Holdings Co.,Ltd."
# 6273.T = "SMC Corporation"
# 6367.T = "DAIKIN INDUSTRIES, Ltd."
# 6501.T = "Hitachi, Ltd."
# 6594.T = "Nidec Corporation"
# 6758.T = "SONY CORPORATION"
# 6861.T = "KEYENCE CORPORATION"
# 6954.T = "FANUC CORPORATION"
# 6981.T = "Murata Manufacturing Co., Ltd."
# 7203.T = "TOYOTA MOTOR CORPORATION"
# 7267.T = "HONDA MOTOR CO., LTD."
# 7741.T = "HOYA CORPORATION"
# 7974.T = "Nintendo Co., Ltd."
# 8001.T = "ITOCHU Corporation"
# 8031.T = "MITSUI & CO., LTD."
# 8035.T = "TOKYO ELECTRON LIMITED"
# 8058.T = "Mitsubishi Corporation"
# 8306.T = "Mitsubishi UFJ Financial Group, Inc."
# 8316.T = "Sumitomo Mitsui Financial Group, Inc."
# 8411.T = "Mizuho Financial Group, Inc."
# 8766.T = "Tokio Marine Holdings, Inc."
# 9432.T = "Nippon Telegraph and Telephone Corporation"
# 9433.T = "KDDI CORPORATION"
# 9434.T = "SOFTBANK CORP."
# 9984.T = "SOFTBANK GROUP CORP."

# import libraries
import yfinance as yf
import pandas as pd

# enter the stock codes or ticker you want
stock_codes = [
    "3382.T", "4063.T", "4502.T", "4503.T", "4568.T", "6098.T",
    "6273.T", "6367.T", "6501.T", "6594.T", "6758.T", "6861.T",
    "6954.T", "6981.T", "7203.T", "7267.T", "7741.T", "7974.T",
    "8001.T", "8031.T", "8035.T", "8058.T", "8306.T", "8316.T",
    "8411.T", "8766.T", "9432.T", "9433.T", "9434.T", "9984.T"
]

# download data
start_date = "2019-01-01"    # start date
end_date = "2024-02-29"      # end date
# if you need hourly, daily or weekly data, change interval to '1h', '1d' or '1wk' respectively.
interval = "1m"             # monthly data
# fetch data
data = yf.download(stock_codes, start=start_date, end=end_date, interval=interval)

# pick closing price up
data = data["Close"]

# print data for checking
print(data)

# Write data to CSV file
file_name = "output.csv"
data.to_csv(file_name)
