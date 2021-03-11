import altair as alt
from vega_datasets import data

# alt.renderers.enable('altair_viewer')
# cars = data.cars()

# print(cars)


# cars.describe()

# charts = alt.Chart(cars).mark_point().encode(
#     x='Horsepower',
#     y='Miles_per_Gallon',
#     color='Origin',
#     shape='Origin'
# ).interactive()

# alt.Chart.show(charts)

import pandas as pd

d = {'year': ['2019','2020','2021'], 'Glucose': [94,94,96], 'Hemoglobin_A1c': [5.1,5.4,5.2], 'PSA': [0.7,0.9,0.6], 'Total_Chorlesterol': [208,185,178], 'Triglycerides': [104,81,85], 'HDL': [53,48,49], 'LDL': [134,121,113], 'Cholesterol_Ratio': [3.9,3.9,3.6]}
df1 = pd.DataFrame(data=d)
print(df1)

# chart = alt.Chart(df1).mark_line().encode(
#     y='year',
#     x='Total_Chorlesterol',
#     color='year'
# ).interactive()

# alt.Chart.show(chart)

df2 = pd.pivot_table(df1,values=['Glucose','Hemoglobin_A1c','PSA','Total_Chorlesterol','Triglycerides','HDL','LDL','Cholesterol_Ratio'],columns=['year'],index=[])
print(df2)