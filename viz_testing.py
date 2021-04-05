# imports
import pandas as pd
import requests
import altair as alt

alt.renderers.enable('altair_viewer')

# set up alphavantage api stuff
# symbol = input()
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
print(df)

# get that index col into its own col(eventually change to a true date string)
df.set_index(df.index, inplace=True)
print(df)
df.index.rename('date', inplace=True)

# all cols are an 'object' will need to convert to floats and 'date' in pandas
dfn = df.apply(pd.to_numeric)

df.index = pd.to_datetime(df.index)

print(df)
chart = alt.Chart(df).mark_circle(size=50).encode(
    x='df.index:T',
    y='open:Q',
    color='volume',
    tooltip=['open','close','high','low']
).interactive()
chart.show()

jt -t grade3 -f droidmono -fs 9 -nf sourcesans  -nfs 95 -T -N -altp -cursc o -cursw 5
