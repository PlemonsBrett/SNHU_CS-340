"""
Main application module for Grazioso Salvare dashboard.

This module provides the main Dash application for the dashboard,
configuring the layout, callbacks, and server initialization.
"""

from __future__ import annotations

from typing import Optional

import dash_bootstrap_components as dbc
from dash import Dash

from grazioso.dashboard.callbacks import register_callbacks
from grazioso.dashboard.layouts import create_layout
from grazioso.dashboard.settings import DashboardSettings


def create_app(settings: Optional[DashboardSettings] = None) -> Dash:
    """
    Create and configure the Dash application
    
    Args:
        settings: Optional dashboard settings, if None, default settings will be used

    Returns:
        Configured Dash application
    """
    # Use default settings if none provided
    if settings is None:
        settings = DashboardSettings()
    
    # Initialize the Dash application with Bootstrap theme
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP], # type: ignore
        suppress_callback_exceptions=True,
        title="Grazioso Salvare Dashboard",
        update_title="Loading...",
    )

    # Set the application layout
    app.layout = create_layout(settings)

    # Register all callbacks
    register_callbacks(app, settings)

    return app

def run_server(host: str = "0.0.0.0", port: int = 8050, debug: bool = False) -> None:
    """
    Create and run the dashboard server.

    Args:
        host: Host address to bind server to (default: "0.0.0.0" - all interfaces)
        port: Port to run server on (default: 8050)
        debug: Whetehr to run in debug mode (default: False)
    """
    # Create application with default settings
    app = create_app()

    # Run the server
    app.run(host=host, port=port, debug=debug) # type: ignore

if __name__ == "__main__":
    # When run directly, start the server
    run_server(debug=True)
