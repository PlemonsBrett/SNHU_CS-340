"""
Data models for the Grazioso Salvare animal shelter application.

This module defines Pydantic models for validating animal data
before it is inserted or updated in the MongoDB database.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class AnimalType(str, Enum):
    """Enumeration of valid animal types."""

    DOG = "Dog"
    CAT = "Cat"
    BIRD = "Bird"
    OTHER = "Other"


class SexType(str, Enum):
    """Enumeration of valid sex types."""

    INTACT_MALE = "Intact Male"
    INTACT_FEMALE = "Intact Female"
    NEUTERED_MALE = "Neutered Male"
    SPAYED_FEMALE = "Spayed Female"
    UNKNOWN = "Unknown"


class OutcomeType(str, Enum):
    """Enumeration of valid outcome types."""

    ADOPTION = "Adoption"
    TRANSFER = "Transfer"
    RETURN_TO_OWNER = "Return to owner"
    EUTHANASIA = "Euthanasia"
    DIED = "Died"
    DISPOSAL = "Disposal"
    MISSING = "Missing"
    RELOCATE = "Relocate"
    TREATMENT = "Treatment"
    BARN = "Barn"
    FOSTER = "Foster"
    OFFSITE = "Offsite"
    SNR = "SNR"


class Animal(BaseModel):
    """
    Pydantic model for animal data.

    This model defines the structure and validation rules for animal data
    used in the application.
    """

    animal_id: str = Field(..., description="Unique identifier for the animal")
    name: Optional[str] = Field(None, description="Name of the animal")
    date_of_birth: Optional[datetime] = Field(
        None, description="Date of birth of the animal"
    )
    animal_type: AnimalType = Field(..., description="Type of animal")
    breed: str = Field(..., description="Breed of the animal")
    color: str = Field(..., description="Color of the animal")
    sex_upon_outcome: SexType = Field(..., description="Sex of the animal at outcome")
    age_upon_outcome: str = Field(..., description="Age of the animal at outcome")
    age_upon_outcome_in_weeks: float = Field(..., description="Age in weeks at outcome")
    outcome_datetime: datetime = Field(..., description="Timestamp of the outcome")
    monthyear: str = Field(..., description="Month and year of the outcome")
    outcome_type: Optional[OutcomeType] = Field(None, description="Type of outcome")
    outcome_subtype: Optional[str] = Field(None, description="Subtype of outcome")
    location_lat: Optional[float] = Field(
        None, description="Latitude of the animal's location"
    )
    location_long: Optional[float] = Field(
        None, description="Longitude of the animal's location"
    )

    @field_validator("animal_id")
    def validate_animal_id(cls, v: str) -> str:
        """Validate the animal ID format."""
        if not v:
            raise ValueError("Animal ID must be a non-empty string")
        return v

    class Config:
        """Configuration for the Animal model."""

        schema_extra = {
            "example": {
                "animal_id": "A123456",
                "name": "Buddy",
                "date_of_birth": "2020-01-01T00:00:00",
                "animal_type": "Dog",
                "breed": "Labrador Retriever",
                "color": "Black",
                "sex_upon_outcome": "Neutered Male",
                "age_upon_outcome": "1 year",
                "age_upon_outcome_in_weeks": 52.0,
                "outcome_datetime": "2021-01-01T00:00:00",
                "monthyear": "January 2021",
                "outcome_type": "Adoption",
                "outcome_subtype": "Standard",
                "location_lat": 30.75,
                "location_long": -97.48,
            }
        }
