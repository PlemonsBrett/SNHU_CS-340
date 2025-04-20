"""
Map component for the Grazioso Salvare dashboard.

This module provides a function to create the map component for the dashboard.
"""

from typing import Tuple

import dash_bootstrap_components as dbc
import dash_leaflet as dl
from dash import html


def create_map(default_center: Tuple[float, float], default_zoom: int) -> html.Div:
    """
    Create the map component for the dashboard.
    
    Args:
        default_center: Default map center coordinates (lat, lon)
        default_zoom: Default zoom level
        
    Returns:
        Map component
    """
    map_component = dbc.Card(
        [
            dbc.CardHeader("Animal Location", className="bg-primary text-white"),
            dbc.CardBody(
                [
                    html.Div(
                        id="map-id",
                        children=[
                            dl.Map(
                                style={"width": "100%", "height": "400px"},
                                center=default_center,
                                zoom=default_zoom,
                                children=[
                                    dl.TileLayer(id="base-layer-id"),
                                ],
                            )
                        ],
                    ),
                    html.Div(
                        [
                            html.Small(
                                "Map displays the location where the selected animal was found.",
                                className="text-muted mt-2",
                            ),
                        ]
                    ),
                ],
                className="px-0",
            ),
        ],
        className="mb-4 h-100",
    )

    return map_component