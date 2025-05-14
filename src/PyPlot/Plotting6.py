import plotly.express as px
import numpy as np
from random import randint

xVals = np.arange(0,100,1)
yVals = []
for k in range(0,100):
    yVals.append(randint(0,100))
print(yVals)
print(xVals)
fig = px.scatter(x = xVals, y = yVals)
fig.show()
