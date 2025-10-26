"""
Paris Olympics 2024 Dashboard
Author: Tia Day
This is the main file that starts the app
"""

# Import what we need
import dash
from dash import Dash, html, dcc

# Create the app
app = Dash(__name__, use_pages=True)

# Make the page layout
app.layout = html.Div([
    
    # Title at top
    html.H1("Paris 2024 Olympics Dashboard"),
    
    # Links to navigate between pages
    html.Div([
        dcc.Link("Home", href="/"),
        html.Span(" | "),
        dcc.Link("Events", href="/events"),
        html.Span(" | "),
        dcc.Link("Athletes", href="/athletes"),
        html.Span(" | "),
        dcc.Link("Venues", href="/venues")
    ]),
    
    html.Hr(),
    
    # This is where the page content shows
    dash.page_container,
    
    # Footer
    html.Footer("Sports4All Pvt Ltd")
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)