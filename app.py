import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px

app = Dash(__name__, use_pages= True, external_stylesheets=['game_style.css', dbc.themes.SPACELAB ])

links = []
for page in dash.page_registry.values():
    links.append( dcc.Link(page['name'] + "       ", href=page['path']))

# Layout goes here

app.layout = html.Div([
    html.H1(["Paris Olympics 2024" ]),
    html.Div( dbc.Row(links)),
    html.Hr(),

    # contents of each page goes here
    dash.page_container,
    html.Hr(),
    html.Footer( 'brought to you by Sports4ALL ')

])

if __name__ == '__main__':
    app.run(debug=True)