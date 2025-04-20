"""
Grazioso Salvare Animal Shelter Database Package.

This package provides tools for interfacing with the animal shelter database used by
Grazioso Salvare to identify dogs that are good candidates for search-and-rescue
training.
"""

from .crud import AnimalShelter
from .models import Animal, AnimalType, OutcomeType, SexType

__all__ = ["AnimalShelter", "Animal", "AnimalType", "OutcomeType", "SexType"]