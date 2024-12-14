import plotly.graph_objects as go

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = 100,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "My first gauge chart"},
    gauge = {
        'axis': {'range': [None, 100]},
        'bar': {'color': "darkblue"},
        'bgcolor': "white",
        'bordercolor': "gray",
        'borderwidth': 2,
        'steps': [
            {'range': [0, 25], 'color': 'lightgray'},
            {'range': [25, 50], 'color': 'gray'},
            {'range': [50, 75], 'color': 'darkgray'},
            {'range': [75, 100], 'color': 'black'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 80
        }
    }
))
fig.show()