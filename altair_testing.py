import altair as alt
from vega_datasets import data

alt.renderers.enable('altair_viewer')
cars = data.cars()

print(cars)
cars.describe()

charts = alt.Chart(cars).mark_point().encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    shape='Origin'
).interactive()

alt.Chart.show(charts)