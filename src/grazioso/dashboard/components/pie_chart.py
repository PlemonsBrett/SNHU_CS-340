"""
Pie chart component for the Grazioso Salvare dashboard.

This module provides a function to create the pie chart component for the dashboard.
"""

import dash_bootstrap_components as dbc
from dash import dcc, html


def create_pie_chart() -> dbc.Card:
    """
    Create the pie chart component for the dashboard.
    
    Returns:
        Pie chart component
    """
    pie_chart = dbc.Card(
        [
            dbc.CardHeader("Breed Distribution", className="bg-primary text-white"),
            dbc.CardBody(
                [
                    dcc.Graph(
                        id="pie-chart",
                        config={
                            "displayModeBar": True,
                            "displaylogo": False,
                            "modeBarButtonsToRemove": [
                                "pan2d",
                                "select2d",
                                "lasso2d",
                                "resetScale2d",
                            ],
                        },
                        style={"height": "400px"},
                        # Add figure layout options to control legend spacing
                        figure={
                            "layout": {
                                # Increase margin on the right side the legend
                                "margin": {"r": 120, "t": 30, "b": 30, "l": 30},
                                # Position the legend further to the right
                                "legend": {
                                    "x": 1.1,  # Position legend outside the plot area
                                    "y": 0.5,  # Center vertically
                                    "xanchor": "left",  # Anchor legend on its left side
                                    "yanchor": "middle"  # Anchor legend at its middle
                                }
                            }
                        }
                    ),
                    html.Div(
                        [
                            html.Small(
                                "Chart shows the distribution of top 10 breeds "
                                "in the current filter.",
                                className="text-muted mt-2",
                            ),
                        ]
                    ),
                ],
                className="px-2",
            ),
        ],
        className="mb-4 h-100",
    )

    return pie_chart