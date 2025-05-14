import plotly.graph_objects as go
fig = go.Figure(
    data = [go.Bar(x=[1,2,3],y=[2,1,3])],
    layout_title_text="Graph Title")
fig.show()
