"""
Layout definitions for the Grazioso Salvare dashboard.

This module provides functions to create the layouts for different pages
and components of the dashboard.
"""

from __future__ import annotations

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dcc, html

from grazioso.crud import AnimalShelter
from grazioso.dashboard.components.data_table import create_data_table
from grazioso.dashboard.components.filter_controls import create_filter_controls
from grazioso.dashboard.components.header import create_header
from grazioso.dashboard.components.map_component import create_map
from grazioso.dashboard.components.pie_chart import create_pie_chart
from grazioso.dashboard.settings import DashboardSettings


def create_layout(settings: DashboardSettings) -> dbc.Container:
    """
    Create the main layout for the dashboard.

    Args:
        settings: Dashboard settings

    Returns:
        Main layout component
    """
    # Connect to the database
    db = AnimalShelter(
        settings.mongodb.username,
        settings.mongodb.password,
        settings.mongodb.host,
        settings.mongodb.port,
        settings.mongodb.db_name,
        settings.mongodb.collection_name,
    )

    # Initial data load - all animals (filtered to just dogs)
    initial_filter = settings.rescue_filters["all"]
    df = pd.DataFrame.from_records(db.read(initial_filter))  # type: ignore

    # MongoDB v5+ returns the '_id' column with an ObjectID type
    # Drop it to avoid issues with the data_table
    if "_id" in df.columns:
        df.drop(columns=["_id"], inplace=True)

    # If visible_columns is specified, filter to only those columns
    if settings.visible_columns:
        visible_cols = [col for col in settings.visible_columns if col in df.columns]
        df = df[visible_cols]

    # Create the main layout
    layout = dbc.Container(
        [
            # Header component
            create_header(settings.author_name),
            dbc.Row(
                [
                    # Filter controls
                    dbc.Col(
                        [create_filter_controls()],
                        width=12,
                        className="mb-4",
                    ),
                ]
            ),
            # Data table
            dbc.Row(
                [
                    dbc.Col(
                        [create_data_table(df)],
                        width=12,
                        className="mb-4",
                    ),
                ]
            ),
            # Visualizations - map and pie chart
            dbc.Row(
                [
                    # Map component
                    dbc.Col(
                        [
                            create_map(
                                settings.map_default_center, settings.map_default_zoom
                            ),
                        ],
                        md=6,
                        className="mb-4",
                    ),
                    # Pie chart
                    dbc.Col(
                        [create_pie_chart()],
                        md=6,
                        className="mb-4",
                    ),
                ]
            ),
            # Footer
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Hr(),
                            html.P(
                                (
                                    f"© 2025 Grazioso Salvare. Dashboard created by "
                                    f"{settings.author_name}"
                                ),
                                className="text-center text-muted",
                            ),
                        ],
                        width=12,
                    ),
                ]
            ),
        ],
        fluid=True,
        className="p-4",
    )

    return layout


def create_not_found_layout() -> html.Div:
    """
    Create the layout for the 404 not found page.

    Returns:
        404 page layout component
    """
    return html.Div(
        [
            html.H1("404 - Page Not Found", className="text-danger"),
            html.Hr(),
            html.P("The page you requested could not be found."),
            dcc.Link("Return to Home", href="/"),
        ],
        className="p-5",
    )
