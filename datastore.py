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
        if self.__class__.__singleton_instance is not None:
            with self.__class__.__singleton_lock:
                if self.__class__.__singleton_instance is not None:
                    raise Exception("You have to use instance method")
        print 'Inside %s' % self.__class__.__name__
        self.filename = filename
        self.__class__.__singleton_instance = self

    def save(self):
        f = open(self.filename, 'wb')
        pickle.dump(self.__dict__, f, -1)
        f.close()

    @classmethod
    def instance(cls, filename):
        print cls.__name__
        if not cls.__singleton_instance:
            with cls.__singleton_lock:
                if not cls.__singleton_instance:
                    cls.__singleton_instance = cls._loader(filename)
        return cls.__singleton_instance

    @classmethod
    def _loader(cls, filename):
        data_store = cls(filename)
        if not os.path.exists(filename):
            print "Inside Loader: File doesn't exist, creating it.."
            data_store.save()
            return data_store
        print "Inside Loader: File exists"
        f = open(filename, 'rb')
        data_store.__dict__.update(pickle.load(f))
        f.close()
        return data_store
