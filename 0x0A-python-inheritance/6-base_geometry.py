#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception("area() is not implemented")
