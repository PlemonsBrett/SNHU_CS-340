"""
Header component for the Grazioso Salvare dashboard.

This module provides a function to create the header component for the dashboard.
"""

import base64
import importlib.resources as pkg_resources
from pathlib import Path

import dash_bootstrap_components as dbc
from dash import html

from grazioso.dashboard import assets


def create_header(author_name: str) -> dbc.Row:
    """
    Create the header component for the dashboard.

    Args:
        author_name: Name of the dashboard author

    Returns:
        Header component
    """
    # Try to load the logo
    try:
        logo_path = str(Path(pkg_resources.files(assets) / "grazioso_salvare_logo.png"))
        with open(logo_path, "rb") as logo_file:
            encoded_logo = base64.b64encode(logo_file.read()).decode("ascii")
    except (FileNotFoundError, IsADirectoryError, ValueError):
        encoded_logo = None

    header = dbc.Row(
        [
            # Logo with URL anchor to SNHU (client requirement)
            dbc.Col(
                html.A(
                    html.Img(
                        src=f"data:image/png;base64,{encoded_logo}" if encoded_logo else None,
                        style={"height": "100px", "max-width": "100%"},
                        className="img-fluid",
                    ),
                    href="https://www.snhu.edu",
                    target="_blank",
                ),
                width="auto",
                className="d-flex align-items-center" if encoded_logo else "d-none",
            ),
            
            # Title and author info
            dbc.Col(
                [
                    html.H1("Grazioso Salvare", className="mb-0"),
                    html.H4("Search and Rescue Dog Finder", className="text-muted mt-0"),
                    html.Div(
                        f"Dashboard created by {author_name}",
                        className="text-muted fst-italic",
                    ),
                ],
                className="d-flex flex-column justify-content-center",
            ),
        ],
        className="align-items-center mb-4 border-bottom pb-3",
    )

    return header