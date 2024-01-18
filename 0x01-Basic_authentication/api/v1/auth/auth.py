#!/usr/bin/env python3
"""Authentication module.
"""
from flask import request
from typing import List, TypeVar
import fnmatch


def compare_strings(str1, str2):
    # Add a trailing backslash to str1 if it doesn't have one
    if str1[-1] != '/':
        str1 += '/'

    # Compare the modified str1 with str2
    return str1 == str2


class Auth:
    """ authentication Class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method to check if auth is required.
        """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for excluded_path in excluded_paths:
            compare_result = compare_strings(path, excluded_path)
            if compare_result:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method to get authorization header.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method to get user from request.
        """
        return None
