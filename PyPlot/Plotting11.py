import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Scatter(
    y = np.random.randn(500),
    mode = 'markers',
    marker = dict(
    size = 16,
    color = np.random.randn(500),
    colorscale = 'Viridis',
    showscale = True
    )
))

fig.show()
