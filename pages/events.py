"""
Events Page
Author: Tia Day
Date: October 2025
This page shows event results by sport
"""

# Import what we need
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd
import plotly.graph_objects as go

# Tell Dash this is the events page
dash.register_page(__name__)

# Load the data
medallists_df = pd.read_csv('Paris_Olympics_dataset/medallists.csv')

# Get list of sports
sports_list = list(medallists_df['discipline'].unique())
sports_list.sort()

# Make the page
layout = html.Div([
    
    html.H2("Event Results"),
    
    html.P("Select a sport to see medal winners"),
    
    # Sport selector
    html.Div([
        html.Label("Pick a sport:"),
        dcc.Dropdown(
            id='sport_dropdown',
            options=[{'label': s, 'value': s} for s in sports_list],
            value='Athletics'
        )
    ]),
    
    # Medal chart for this sport
    html.Div([
        dcc.Graph(id='sport_medal_chart')
    ], style={'marginTop': '20px'}),
    
    # Results will show here
    html.Div(id='results_output', style={'marginTop': '20px'})
])

# When user picks a sport, show medal chart
@callback(
    Output('sport_medal_chart', 'figure'),
    Input('sport_dropdown', 'value')
)
def show_medal_chart(sport):
    # Filter for this sport
    sport_df = medallists_df[medallists_df['discipline'] == sport]
    
    # Count medals by type
    medal_counts = sport_df['medal_type'].value_counts()
    
    # Make pie chart
    fig = go.Figure(data=[go.Pie(
        labels=medal_counts.index,
        values=medal_counts.values,
        marker=dict(colors=['gold', 'silver', '#CD7F32'])
    )])
    
    fig.update_layout(title=f"{sport} - Medal Distribution")
    
    return fig

# When user picks a sport, show results
@callback(
    Output('results_output', 'children'),
    Input('sport_dropdown', 'value')
)
def show_results(sport):
    # Filter for this sport
    sport_df = medallists_df[medallists_df['discipline'] == sport]
    
    # Get first 10 results
    sport_df = sport_df.head(10)
    
    # Make a simple list
    results = []
    results.append(html.H3(f"{sport} Results (Top 10)"))
    
    for i, row in sport_df.iterrows():
        text = f"{row['name']} ({row['country']}) - {row['medal_type']} - {row['event']}"
        results.append(html.P(text))
    
    return results
