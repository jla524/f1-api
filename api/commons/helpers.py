"""
Define helper functions
"""
from pathlib import Path

from api.commons.data_routes import DataRoutes


def get_file_name(stem) -> Path:
    """
    @description: getter for a specific data file
    """
    return DataRoutes().get_file_map().get(stem)


def get_route(stem) -> str:
    """
    @description: getter for a specific route name
    """
    return DataRoutes().get_route_map().get(stem)
