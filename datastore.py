#!usr/bin/env python
#-*-coding:utf8-*-

__doc__  =  """
    * A Singleton data store class
"""

import os
import pickle
import threading

class SingletonDataStore(object):

    __singleton_lock = threading.Lock()
    __singleton_instance = None

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
        self.__class__.__singleton_instance.__dict__.update(pickle.load(f))
        f.close()

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = object.__new__(cls, *args, **kwargs)
                    cls.__singleton_instance.initialized = False
        return cls.__singleton_instance