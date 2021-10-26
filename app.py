#!/usr/bin/env python3
from api.route import home_api, drivers, constructors


def main():
    home_api.run(host='0.0.0.0', port=105)


if __name__ == '__main__':
    main()
