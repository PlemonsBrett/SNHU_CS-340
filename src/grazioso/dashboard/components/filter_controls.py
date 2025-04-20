"""
Filter controls component for the Grazioso Salvare dashboard.

This module provides a function to create the filter controls component for the dashboard.
"""

import dash_bootstrap_components as dbc
from dash import html


def create_filter_controls() -> dbc.Card:
    """
    Create the filter controls component for the dashboard.

    Returns:
        Filter controls component
    """
    filter_controls = dbc.Card(
        [
            dbc.CardHeader("Filter Options", className="bg-primary text-white"),
            dbc.CardBody(
                [
                    html.H5("Filter by Rescue Type:", className="card-title"),
                    dbc.RadioItems(
                        id="filter-type",
                        options=[
                            {"label": "All Dogs", "value": "all"},
                            {"label": "Water Rescue", "value": "water"},
                            {"label": "Mountain or Wilderness Rescue", "value": "mountain"},
                            {
                                "label": "Disaster Rescue or Individual Tracking",
                                "value": "disaster",
                            },
                        ],
                        value="all",
                        inline=True,
                        className="mb-2",
                    ),
                    html.Hr(className="my-2"),
                    html.Div(
                        [
                            dbc.Badge("Water Rescue: Labrador, Chesapeake Bay Retriever, Newfoundland (Female, 26-156 weeks)", 
                                     color="info", className="me-1 mb-1"),
                            dbc.Badge("Mountain Rescue: German Shepherd, Malamute, Old English Sheepdog, Husky, Rottweiler (Male, 26-156 weeks)", 
                                     color="success", className="me-1 mb-1"),
                            dbc.Badge("Disaster Rescue: Doberman, German Shepherd, Golden Retriever, Bloodhound, Rottweiler (Male, 20-300 weeks)", 
                                     color="warning", className="me-1 mb-1"),
                        ],
                        className="d-flex flex-wrap",
                    ),
                ]
            ),
        ],
        className="mb-4",
    )

    return filter_controls