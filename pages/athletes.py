"""
Athletes Page
Author: Tia Day
This page shows a list of athletes
"""

# Import what we need
import dash
from dash import html, dcc, callback, Input, Output
import pandas as pd

# Tell Dash this is the athletes page
dash.register_page(__name__)

# Load athlete data
athletes_df = pd.read_csv('Paris_Olympics_dataset/athletes.csv')

# Pick only what we need
athletes_df = athletes_df[['name', 'country', 'gender']]
athletes_df = athletes_df.dropna()
athletes_df = athletes_df.head(50)  # Just show 50

# Make the page
layout = html.Div([
    
    html.H2("Olympic Athletes"),
    
    html.P(f"Showing {len(athletes_df)} athletes"),
    
    # Search box
    html.Label("Search:"),
    dcc.Input(id='search_box', type='text', placeholder='Type name or country'),
    
    # Results will show here
    html.Div(id='athlete_list')
])

# When user types, filter the list
@callback(
    Output('athlete_list', 'children'),
    Input('search_box', 'value')
)
def filter_athletes(search_text):
    # If nothing typed, show all
    if not search_text:
        filtered = athletes_df
    else:
        # Filter by name or country
        search_lower = search_text.lower()
        filtered = athletes_df[
            athletes_df['name'].str.lower().str.contains(search_lower, na=False) |
            athletes_df['country'].str.lower().str.contains(search_lower, na=False)
        ]
    
    # Make a list to display
    results = []
    for i, row in filtered.iterrows():
        text = f"{row['name']} - {row['country']} ({row['gender']})"
        results.append(html.P(text))
    
    # If no results
    if len(results) == 0:
        return html.P("No athletes found")
    
    return results