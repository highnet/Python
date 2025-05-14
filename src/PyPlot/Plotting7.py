import plotly.express as px
import numpy as np

xVals = np.linspace(0,2*np.pi,100)
fig = px.line(x=xVals, y=np.cos(xVals), labels={'x':'t', 'y':'cos(t)'})
fig.show()
