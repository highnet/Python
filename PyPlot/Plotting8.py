import plotly.express as px

gapminder = px.data.gapminder().query("continent == 'Oceania'")
fig = px.line(gapminder, x = 'year',y = 'lifeExp', color='country')
fig.show()
