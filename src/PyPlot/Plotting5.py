import plotly.graph_objects as go
from plotly.subplots import make_subplots
from random import randint

rows = randint(1,5)
cols = randint(1,5)

fig = make_subplots(rows=rows, cols=cols)

for i in range(1,rows+1):
    for j in range(1,cols+1):
        yVals = []
        for k in range(1,randint(1,100)):
            yVals.append(randint(0,100))
        fig.add_trace(go.Bar(y=yVals), row=i, col=j)

fig.show()
