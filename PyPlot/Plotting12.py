import plotly.express as px

gapminder = px.data.gapminder().query("continent == 'Europe'")
fig = px.line(gapminder, x='year',y="lifeExp",color="country")
fig.show()
