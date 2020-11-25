"""
© Copyright 2020 HP Development Company, L.P.
SPDX-License-Identifier: GPL-2.0-only
"""

import abc
import os


class Store(abc.ABC):
    def __init__(self):
        self.connect()
        if self._store is None:
            return None

    @abc.abstractmethod
    def connect(self):
        """
        Method to create a conection with the store.
        """
        pass

    @abc.abstractmethod
    def put(self, keypath, filepath):
        """
        Method to upload file to store.

        :param keypath: local file path.
        :param filepath: store file path.
        :return: boolean.
        """
        pass

    @abc.abstractmethod
    def get(self, filepath, reference):
        """
        Method to download file from the store.
        :param filepath: local file path.
        :param reference: file located in the store.
        :return: boolean.
        """
        pass

    def store(self, key, file, path, prefix=None):
        full_path = os.sep.join([path, file])
        return self.file_store(key, full_path, prefix)

    def file_store(self, key, filepath, prefix=None):
        keypath = key
        if prefix is not None:
            keypath = prefix + '/' + key

        uri = self.put(keypath, filepath)
        return {uri: key}

    def import_file_from_url(self, path_dst, url):
        """
        Method to  import files from store url to a destine path.
        """
        pass
