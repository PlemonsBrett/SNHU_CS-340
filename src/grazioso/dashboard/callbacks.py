"""
Callback definitions for the Grazioso Salvare dashboard.

This module registers all the callbacks for the dashboard application,
handling the interactions between components.
"""

from __future__ import annotations

from typing import Any, Dict, List, cast

import dash_leaflet as dl
import pandas as pd
import plotly.express as px
from dash import Dash, html
from dash.dependencies import Input, Output

from grazioso.crud import AnimalShelter
from grazioso.dashboard.settings import DashboardSettings


def register_callbacks(app: Dash, settings: DashboardSettings) -> None:
    """
    Register all callbacks for the dashboard application.

    Args:
        app: Dash application
        settings: Dashboard settings
    """
    # Create a database connection for callbacks to use
    db = AnimalShelter(
        settings.mongodb.username,
        settings.mongodb.password,
        settings.mongodb.host,
        settings.mongodb.port,
        settings.mongodb.db_name,
        settings.mongodb.collection_name,
    )

    @app.callback(Output("datatable-id", "data"), [Input("filter-type", "value")]) # type: ignore
    def update_dashboard(filter_type: str) -> List[Dict[str, Any]]:
        """
        Update the dashboard data based on the selected filter type.

        Args:
            filter_type: The selected filter type ('all', 'water', 'mountain', 'disaster')

        Returns:
            Updated data for the data table
        """
        # Get the filter based on the selected value
        selected_filter = settings.rescue_filters[filter_type]

        # Query the database with the selected filter
        filtered_results = db.read(selected_filter)

        # Convert results to DataFrame
        df_filtered = pd.DataFrame.from_records(filtered_results) # type: ignore

        # Drop the _id column if it exists
        if "_id" in df_filtered.columns:
            df_filtered.drop(columns=["_id"], inplace=True)

        # If visible_columns is specified, filter to only those columns
        if settings.visible_columns:
            visible_cols = [
                col for col in settings.visible_columns if col in df_filtered.columns
            ]
            df_filtered = df_filtered[visible_cols]

        # Return the filtered data, cast to ensure correct type
        return cast(List[Dict[str, Any]], df_filtered.to_dict("records")) # type: ignore

    @app.callback( # type: ignore
        Output("pie-chart", "figure"), [Input("datatable-id", "derived_virtual_data")]
    )
    def update_pie_chart(view_data: List[Dict[str, Any]]) -> html.Figure:
        """
        Update the pie chart based on the filtered data.

        Args:
            view_data: The data from the data table

        Returns:
            Updated pie chart figure
        """
        if not view_data:
            # Return an empty figure for no data
            return px.pie(names=["No Data"], values=[1], title="No Data Available")

        # Convert the data to a DataFrame
        dff = pd.DataFrame.from_dict(view_data)

        # Create a pie chart showing breed distribution
        if "breed" in dff.columns and len(dff) > 0:
            # Group by breed and count occurrences
            breed_counts = dff["breed"].value_counts().nlargest(10)  # Top 10 breeds

            fig = px.pie(
                names=breed_counts.index,
                values=breed_counts.values,
            )

            # Update layout for better appearance
            fig.update_layout(
                # Increase right margin to make more space for the legend
                margin=dict(l=20, r=120, t=30, b=20),
                legend=dict(
                    # Position legend to the right of the chart instead of below
                    orientation="v",  # vertical orientation
                    yanchor="middle",  # anchor at middle of legend
                    y=0.5,  # center vertically
                    xanchor="left",  # anchor at left side of legend
                    x=1.1,  # position legend outside the plot area
                ),
            )

            # Return the figure directly
            return fig
        else:
            # Return an empty figure with a message
            return px.pie(
                names=["No Breed Data"], values=[1], title="No Breed Data Available"
            )

    @app.callback(
        Output("datatable-id", "style_data_conditional"),
        [
            Input("datatable-id", "selected_columns"),
            Input("datatable-id", "selected_rows"),
        ],
    )
    def update_styles(
        selected_columns: List[str], selected_rows: List[int]
    ) -> List[Dict[str, Any]]:
        """
        Highlight selected columns and rows in the data table.

        Args:
            selected_columns: List of selected column IDs
            selected_rows: List of indices of selected rows

        Returns:
            Style data for conditional formatting
        """
        styles: List[Dict[str, Any]] = []

        # Style for odd rows (striped table)
        styles.append(
            {"if": {"row_index": "odd"}, "backgroundColor": "rgb(248, 248, 248)"}
        )

        # Highlight selected columns
        if selected_columns:
            styles.extend(
                [
                    {"if": {"column_id": i}, "background_color": "#D2F3FF"}
                    for i in selected_columns
                ]
            )

        # Highlight selected rows
        if selected_rows:
            styles.extend(
                [
                    {"if": {"row_index": i}, "background_color": "#FFFFCC"}
                    for i in selected_rows
                ]
            )

        return styles

    @app.callback(
        Output("map-id", "children"),
        [
            Input("datatable-id", "derived_virtual_data"),
            Input("datatable-id", "derived_virtual_selected_rows"),
        ],
    )
    def update_map(
        viewData: List[Dict[str, Any]], selected_rows: List[int]
    ) -> List[Any]:
        """
        Update the geolocation map based on the selected animal.

        Args:
            viewData: The data from the data table
            selected_rows: List of indices of selected rows

        Returns:
            Updated map component
        """
        if not viewData:
            return [
                dl.Map(
                    style={"width": "100%", "height": "500px"},
                    center=settings.map_default_center,
                    zoom=settings.map_default_zoom,
                    children=[dl.TileLayer(id="base-layer-id")],
                )
            ]

        dff = pd.DataFrame.from_dict(viewData)

        # Default to first row if no row is selected
        if selected_rows is None or len(selected_rows) == 0:
            row = 0
        else:
            row = selected_rows[0]

        # Check if we have enough rows to display
        if len(dff) <= row:
            # Default to settings default coordinates if no data
            return [
                dl.Map(
                    style={"width": "100%", "height": "500px"},
                    center=settings.map_default_center,
                    zoom=settings.map_default_zoom,
                    children=[dl.TileLayer(id="base-layer-id")],
                )
            ]

        # Extract latitude and longitude for the selected animal
        # Default to settings default coordinates if the location is missing
        lat = (
            dff.iloc[row]["location_lat"]
            if "location_lat" in dff.columns
            and not pd.isna(dff.iloc[row]["location_lat"])
            else settings.map_default_center[0]
        )
        lon = (
            dff.iloc[row]["location_long"]
            if "location_long" in dff.columns
            and not pd.isna(dff.iloc[row]["location_long"])
            else settings.map_default_center[1]
        )

        # Get animal details for tooltip and popup
        breed = dff.iloc[row]["breed"] if "breed" in dff.columns else "Unknown"
        name = (
            dff.iloc[row]["name"]
            if "name" in dff.columns and not pd.isna(dff.iloc[row]["name"])
            else "Unnamed"
        )
        animal_id = (
            dff.iloc[row]["animal_id"] if "animal_id" in dff.columns else "Unknown ID"
        )
        outcome_type = (
            dff.iloc[row]["outcome_type"]
            if "outcome_type" in dff.columns
            and not pd.isna(dff.iloc[row]["outcome_type"])
            else "Unknown"
        )

        return [
            dl.Map(
                style={"width": "100%", "height": "500px"},
                center=[lat, lon],
                zoom=settings.map_default_zoom,
                children=[
                    dl.TileLayer(id="base-layer-id"),
                    # Marker with tooltip and popup
                    dl.Marker(
                        position=[lat, lon],
                        children=[
                            dl.Tooltip(breed),
                            dl.Popup(
                                [
                                    html.H4("Animal Details"),
                                    html.P(f"ID: {animal_id}"),
                                    html.P(f"Name: {name}"),
                                    html.P(f"Breed: {breed}"),
                                    html.P(f"Outcome: {outcome_type}"),
                                ]
                            ),
                        ],
                    ),
                ],
            )
        ]
