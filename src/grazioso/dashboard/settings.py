"""
Settings for the Grazioso Salvare dashboard.

This module defines the settings used by the dashboard application,
including MongoDB connection details and filters for different rescue types.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class MongoDBSettings:
    """MongoDB connection settings"""

    username: str = "aacuser"
    password: str = "SNHU1234"
    host: str = "localhost"
    port: int = 27017
    db_name: str = "AAC"
    collection_name: str = "animals"


@dataclass
class DashboardSettings:
    """Settings for the dashboard application"""

    # MongoDB connection settings
    mongodb: MongoDBSettings = field(default_factory=MongoDBSettings)

    # Author information for branding
    author_name: str = "Brett Plemons"

    # default page size for data table
    page_size: int = 10

    # Filter definitions for different rescue types
    rescue_filters: Dict[str, Dict[str, Any]] = field(default_factory=lambda: {
        "all": {
            "animal_type": "Dog"
        },
        "water": {
            "animal_type": "Dog",
            "breed": {"$in": [
                "Labrador Retriever Mix",
                "Chesapeake Bay Retriever",
                "Newfoundland",
            ]},
            "sex_upon_outcome": "Intact Female",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156},
        },
        "mountain": {
            "animal_type": "Dog",
            "breed": {"$in": [
                "German Shepherd",
                "Alaskan Malamute",
                "Old English Sheepdog",
                "Siberian Husky",
                "Rottweiler",
            ]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156},
        },
        "disaster": {
            "animal_type": "Dog",
            "breed": {"$in": [
                "Doberman Pinscher",
                "German Shepherd",
                "Golden Retriever",
                "Bloodhound",
                "Rottweiler",
            ]},
            "sex_upon_outcome": "Intact Male",
            "age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300},
        },
    })

    # Column visibility settins - which columns to display by default
    # Empty list means all columns will be shown
    visible_columns: list[str] = field(default_factory=list)

    # Map default center (Austin, TX)
    map_default_center: tuple[float, float] = (30.2672, -97.7431)
    map_default_zoom: int = 10