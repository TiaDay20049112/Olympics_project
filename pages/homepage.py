"""
Homepage
Author: Tia Day
This page shows Olympic statistics
"""

# Import what we need
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.graph_objects as go

# Tell Dash this is the homepage
dash.register_page(__name__, path='/')

# Load the data
medals_df = pd.read_csv('Paris_Olympics_dataset/medals_total.csv')

# Count how many countries
country_count = len(medals_df)

# Make the page
layout = html.Div([
    
    html.H2("Paris Olympics 2024"),
    
    # Add the Paris 2024 image
    html.Div([
        html.Img(src='/assets/paris.jpeg', style={'width': '100%', 'maxWidth': '800px', 'height': 'auto'})
    ], style={'textAlign': 'center', 'margin': '20px 0'}),
    
    # Show number of countries
    html.Div([
        html.H3(str(country_count)),
        html.P("Countries Participating")
    ], style={'textAlign': 'center', 'padding': '20px', 'backgroundColor': '#f0f0f0'}),
    
    # Games info
    html.Div([
        html.H3("Games Overview"),
        html.P("Dates: July 26 - August 11, 2024"),
        html.P("Location: Paris, France"),
        html.P("Total Events: 329"),
        html.P("Opening Ceremony: July 26, 2024 on the Seine River"),
    ], style={'padding': '20px'}),
    
    # Medal chart
    html.Div([
        html.H3("Top 10 Countries by Medals"),
        dcc.Graph(id='medal_chart')
    ], style={'padding': '20px'})
])

# Make the medal chart
@callback(
    Output('medal_chart', 'figure'),
    Input('medal_chart', 'id')
)
def make_chart(_):
    # Get top 10 countries
    top10 = medals_df.head(10)
    
    # Make a simple bar chart
    fig = go.Figure()
    
    # Add gold medals
    fig.add_trace(go.Bar(
        name='Gold',
        x=top10['country'],
        y=top10['Gold Medal'],
        marker_color='gold'
    ))
    
    # Add silver medals
    fig.add_trace(go.Bar(
        name='Silver',
        x=top10['country'],
        y=top10['Silver Medal'],
        marker_color='silver'
    ))
    
    # Add bronze medals
    fig.add_trace(go.Bar(
        name='Bronze',
        x=top10['country'],
        y=top10['Bronze Medal'],
        marker_color='#CD7F32'
    ))
    
    # Stack the bars
    fig.update_layout(barmode='stack')
    
    return fig