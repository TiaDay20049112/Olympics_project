"""
Venues Page
Author: Tia Day
Date: October 2025
This page shows Olympic venues
"""

# Import what we need
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.graph_objects as go

# Tell Dash this is the venues page
dash.register_page(__name__)

# Load venue data
venues_df = pd.read_csv('Paris_Olympics_dataset/venues.csv')
coords_df = pd.read_csv('Paris_Olympics_dataset/venue_coordinates.csv')

# Combine the data
venues_map = coords_df.merge(venues_df, on='venue')

# Make the page
layout = html.Div([
    
    html.H2("Olympic Venues"),
    
    html.P("Map of venues in Paris"),
    
    # The map
    dcc.Graph(id='venue_map'),
    
    # Venue list
    html.Div([
        html.H3("Venue List"),
        html.Div(id='venue_list')
    ])
])

# Make the map
@callback(
    Output('venue_map', 'figure'),
    Input('venue_map', 'id')
)
def make_map(_):
    # Create map
    fig = go.Figure()
    
    # Add markers
    fig.add_trace(go.Scattermapbox(
        lat=venues_map['latitude'],
        lon=venues_map['longitude'],
        mode='markers',
        marker=dict(size=10, color='blue'),
        text=venues_map['venue']
    ))
    
    # Center on Paris
    fig.update_layout(
        mapbox=dict(
            style='open-street-map',
            center=dict(lat=48.8566, lon=2.3522),
            zoom=11
        ),
        height=400
    )
    
    return fig

# Make the venue list
@callback(
    Output('venue_list', 'children'),
    Input('venue_list', 'id')
)
def make_list(_):
    # Make a simple list
    results = []
    for i, row in venues_map.iterrows():
        text = f"{row['venue']} - {row['sports']}"
        results.append(html.P(text))
    
    return results
