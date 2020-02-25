# -*- coding: UTF-8 -*-


class pandasesException(RuntimeError):
    def __init__(self, msg):
        super(pandasesException, self).__init__(msg)


class NoSuchDependencyException(pandasesException):
    pass


class ServerDefinedException(pandasesException):
    pass


class ParseResultException(pandasesException):
    pass


class DataFrameException(pandasesException):
    pass
