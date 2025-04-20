"""
Utility functions for the Grazioso Salvare dashboard.

This module provides utility functions used by the dashboard application.
"""

from __future__ import annotations

import base64
from pathlib import Path
from typing import Any, Optional, Union

import pandas as pd
from dash import html


def encode_image(image_path: Union[str, Path]) -> Optional[str]:
    """
    Encode an image file as base64.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Base64 encoded image or None if the file cannot be read
    """
    try:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("ascii")
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        return None


def format_breed_name(breed: str) -> str:
    """
    Format a breed name for display.
    
    Args:
        breed: Breed name
        
    Returns:
        Formatted breed name
    """
    # Limit to first part if there are multiple breeds listed
    if "/" in breed:
        breed = breed.split("/")[0].strip()
    
    # Remove "Mix" or "mix" suffix
    if " Mix" in breed:
        breed = breed.replace(" Mix", "")
    elif " mix" in breed:
        breed = breed.replace(" mix", "")
    
    return breed


def prepare_animal_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepare animal data for display.
    
    Args:
        df: DataFrame with animal data
        
    Returns:
        Processed DataFrame
    """
    # Create a copy to avoid modifying the original
    processed_df = df.copy()
    
    # Convert datetime columns to more readable format
    if "datetime" in processed_df.columns:
        processed_df["datetime"] = pd.to_datetime(processed_df["datetime"]).dt.strftime("%Y-%m-%d")
    
    # Convert age to more readable format
    if "age_upon_outcome_in_weeks" in processed_df.columns:
        processed_df["age_in_years"] = (processed_df["age_upon_outcome_in_weeks"] / 52).round(1)
    
    # Format breed names
    if "breed" in processed_df.columns:
        processed_df["breed_display"] = processed_df["breed"].apply(format_breed_name)
    
    return processed_df


def create_info_card(title: str, content: Any) -> html.Div:
    """
    Create an info card with title and content.
    
    Args:
        title: Card title
        content: Card content
        
    Returns:
        Info card component
    """
    return html.Div(
        className="info-card",
        children=[
            html.Div(title, className="info-card-title"),
            html.Div(str(content), className="info-card-content"),
        ],
    )