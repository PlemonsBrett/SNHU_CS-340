"""
Data table component for the Grazioso Salvare dashboard.

This module provides a function to create the data table component for the dashboard.
"""

import dash_bootstrap_components as dbc
import pandas as pd
from dash import dash_table, html


def create_data_table(df: pd.DataFrame) -> dbc.Card:
    """
    Create the data table component for the dashboard.
    
    Args:
        df: Initial data for the table
        
    Returns:
        Data table component
    """
    data_table = dbc.Card(
        [
            dbc.CardHeader("Dog Records", className="bg-primary text-white"),
            dbc.CardBody(
                [
                    dash_table.DataTable(
                        id="datatable-id",
                        columns=[
                            {"name": i, "id": i, "deletable": False, "selectable": True}
                            for i in df.columns
                        ],
                        data=df.to_dict("records"),
                        # Interactive features to make it user-friendly
                        editable=False,  # Don't allow editing
                        filter_action="native",  # Allow filtering of data by user
                        sort_action="native",  # Allow sorting of data by user
                        sort_mode="multi",  # Sort across multiple columns
                        column_selectable="single",  # Allow selecting columns
                        row_selectable="single",  # Allow selecting rows
                        row_deletable=False,  # Prevent row deletion
                        selected_columns=[],  # Initially, no columns are selected
                        selected_rows=[],  # Initially, no rows are selected
                        page_action="native",  # All data is passed to the table up-front
                        page_current=0,  # Start on first page
                        page_size=10,  # Show 10 rows per page
                        style_cell={  # Style cells
                            "font-size": "12px",
                            "text-align": "left",
                            "padding": "5px",
                            "maxWidth": "180px",
                            "whiteSpace": "normal",
                            "height": "auto",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                        },
                        style_header={  # Style header cells
                            "backgroundColor": "rgb(30, 30, 30)",
                            "color": "white",
                            "fontWeight": "bold",
                        },
                        style_data_conditional=[  # Highlight selected rows
                            {
                                "if": {"row_index": "odd"},
                                "backgroundColor": "rgb(248, 248, 248)",
                            }
                        ],
                        tooltip_delay=0,
                        tooltip_duration=None,
                    ),
                    html.Div(
                        [
                            html.Small(
                                "Click on a row to view the animal's location on the map.",
                                className="text-muted mt-2",
                            ),
                        ]
                    ),
                ],
                className="px-0",
            ),
        ],
        className="mb-4",
    )

    return data_table