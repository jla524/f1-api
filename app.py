#!/usr/bin/env python3
from api.route import api, circuits, constructors, drivers, races


def main():
    api.run(host='0.0.0.0', port=105)


if __name__ == '__main__':
    main()
