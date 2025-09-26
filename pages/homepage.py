import dash
from dash import Dash, html, dcc
import plotly.express as px

dash.register_page(__name__, path = '/')

layout = html.Div([
    html.H1("This is the homepage")
])
