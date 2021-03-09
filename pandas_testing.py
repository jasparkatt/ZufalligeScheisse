import pandas as pd
import requests

api_key = 'LAJBI8EN52GC18OY'
base_url = 'https://www.alphavantage.co/query?'
params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
          'symbol': 'CYDY',
          'apikey': api_key}

# get response from api and format it a bit and put it into a dict
# this helps with the mulit level nested json by 'stripping' metadata header info
response = requests.get(base_url, params=params)
response_dict = response.json()
_, header = response.json()

# create a pandas dataframe from response_dict
df = pd.DataFrame.from_dict(response_dict[header], orient='index')
print(df)
# strip the cols names down to bare bones header
df_cols = [i.split(' ')[1] for i in df.columns]
df.columns = df_cols




# get that index col into its own col(eventually change to a true date string)
# df.set_index(df.index, inplace=True)
# print(df)
# df.index.rename('date', inplace=True)
df.index = pd.to_datetime(df.index)
print(df)
print(df.dtypes)
# all cols are an 'object' will need to convert to floats and 'date' in pandas
# dfn = df.apply(pd.to_numeric)

