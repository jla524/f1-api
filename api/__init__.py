"""
Package wide configurations

Adapted from:
https://github.com/mattcoding4days/kickstart/blob/main/src/kickstart
"""
from pathlib import Path
from threading import Lock


class ThreadSafeMeta(type):
    """
    @description: a thread-safe implementation of Singleton
    """
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs) -> any:
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=ThreadSafeMeta):
    """
    @description: global program configuration
    """
    __version = '0.1.0'
    __package = __package__
    __default_env = 'dev'

    __base_dir = Path(__file__).resolve(strict=True).parent.parent
    __data_dir = __base_dir / 'data'

    __api_route = '/api'
    __resources_route = '/'.join([__api_route, 'v1', 'resources'])
    __orient = 'records'

    @classmethod
    def version(cls) -> str:
        """
        @description: getter for version of the package
        """
        return cls.__version

    @classmethod
    def package(cls) -> str:
        """
        @description: getter for the package name
        """
        return cls.__package

    @classmethod
    def default_env(cls) -> str:
        """
        @description: getter for the default env
        """
        return cls.__default_env

    @classmethod
    def base_dir(cls) -> Path:
        """
        @description: getter for the base directory
        """
        return cls.__base_dir

    @classmethod
    def data_dir(cls) -> Path:
        """
        @description: getter for the data directory
        """
        return cls.__data_dir

    @classmethod
    def api_route(cls) -> str:
        """
        @description: getter for the api route
        """
        return cls.__api_route

    @classmethod
    def resources_route(cls) -> str:
        """
        @description: getter for the resources route
        """
        return cls.__resources_route

    @classmethod
    def orient(cls) -> str:
        """
        @description: getter for the expected JSON string format
        """
        return cls.__orient
