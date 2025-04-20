"""
Dashboard module for Grazioso Salvare application.

This module provides a web-based dashboard for visualizing and interacting with
animal shelter data. It is built using Dash and implements the requirements
for the CS 340 Project Two assignment.
"""

from grazioso.dashboard.app import create_app, run_server
from grazioso.dashboard.settings import DashboardSettings, MongoDBSettings

__all__ = ["create_app", "run_server", "DashboardSettings", "MongoDBSettings"]