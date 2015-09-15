#!usr/bin/env python
# -*-coding:utf8-*-

import os
import pickle
import threading

__doc__ = """
    * A Singleton data store class
"""


class SingletonDataStore(object):

    _singleton_lock = threading.Lock()
    _singleton_instance = None

    def __init__(self, filename):
        self.filename = filename

    def init(self):
        self.load()
        self.save()

    def save(self):
        f = open(self.filename, 'wb')
        pickle.dump(self.__dict__, f, -1)
        f.close()

    def load(self):
        if not os.path.exists(self.filename):
            return
        f = open(self.filename, 'rb')
        self.__class__._singleton_instance.__dict__.update(pickle.load(f))
        f.close()

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls._singleton_instance:
            with cls._singleton_lock:
                if not cls._singleton_instance:
                    cls._singleton_instance = object.__new__(cls, *args,
                                                             **kwargs)
                    cls._singleton_instance.initialized = False
        return cls._singleton_instance
