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

    def __call__(cls, *args, **kwargs):
        with cls.lock:
            if cls not in cls.instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=ThreadSafeMeta):
    """
    @description: global program configuration
    """
    __version = '0.1.0'
    __package = __package__

    __base_dir = Path(__file__).resolve(strict=True).parent.parent
    __data_dir = __base_dir / 'data'
    __circuits_file = __data_dir / 'circuits.csv'
    __constructors_file = __data_dir / 'constructors.csv'
    __drivers_file = __data_dir / 'drivers.csv'
    __races_file = __data_dir / 'races.csv'

    __orient = 'records'

    __api_route = '/api'
    __resources_route = '/'.join([__api_route, 'v1', 'resources'])
    __circuits_route = '/'.join([__resources_route, 'circuits'])
    __constructors_route = '/'.join([__resources_route, 'constructors'])
    __drivers_route = '/'.join([__resources_route, 'drivers'])
    __races_route = '/'.join([__resources_route, 'races'])

    @classmethod
    def version(cls):
        """
        @description: getter for version of package
        """
        return cls.__version

    @classmethod
    def package(cls):
        """
        @description: getter for package name
        """
        return cls.__package

    @classmethod
    def base_dir(cls):
        """
        @description: getter for base directory
        """
        return cls.__base_dir

    @classmethod
    def data_dir(cls):
        """
        @description: getter for data directory
        """
        return cls.__data_dir

    @classmethod
    def circuits_file(cls):
        """
        @description: getter for circuits file
        """
        return cls.__circuits_file

    @classmethod
    def constructors_file(cls):
        """
        @description: getter for constructors file
        """
        return cls.__constructors_file

    @classmethod
    def drivers_file(cls):
        """
        @description: getter for drivers file
        """
        return cls.__drivers_file

    @classmethod
    def races_file(cls):
        """
        @description: getter for races file
        """
        return cls.__races_file

    @classmethod
    def orient(cls):
        """
        @description: getter for JSON format
        """
        return cls.__orient

    @classmethod
    def api_route(cls):
        """
        @description: getter for api route
        """
        return cls.__api_route

    @classmethod
    def circuits_route(cls):
        """
        @description: getter for circuits route
        """
        return cls.__circuits_route

    @classmethod
    def constructors_route(cls):
        """
        @description: getter for constructors route
        """
        return cls.__constructors_route

    @classmethod
    def drivers_route(cls):
        """
        @description: getter for drivers route
        """
        return cls.__drivers_route

    @classmethod
    def races_route(cls):
        """
        @description: getter for races route
        """
        return cls.__races_route
