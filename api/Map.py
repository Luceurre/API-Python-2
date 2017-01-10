import pickle

from api.Logger import *


class Map(Logger):
    def __init__(self):
        self.name = ""
        self.actors = {}

    def save(self):
        # Sauvegarde la Map dans le fichier 'name' + .map
        file = open(self.name + ".map", mode='b')

        pickle.Pickler(self, file)

    def __iter__(self):
        return self.actors

    @classmethod
    def load(cls, name):
        # Charge la Map 'name' avec Pickle, renvoie une instance de Map
        file = open(name + ".map", mode='b')

        return pickle.Unpickler(file).load()
