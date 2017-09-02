import discord

class E:
    def __init__(self, embed):
        self.embed = embed

        if hasattr(embed, '__call__'):
            self.isCallable = True
        else:
            self.isCallable = False

    def __call__(self, *args):
        if self.isCallable:
            return self.embed(*args)
        else:
            return self.embed

class Map(dict):
    """
    Example:
    m = Map()
    m.cheese = "good"
    """

    def __init__(self):
        pass

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Map, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Map, self).__delitem__(key)
        del self.__dict__[key]

class EMap(Map):
    def __setattr__(self, key, value):
        self.__setitem__(key, E(value))

    def __setitem__(self, key, value):
        v = E(value)
        super(Map, self).__setitem__(key, v)
        self.__dict__.update({key: v})


def createEmbed(ecolor, names, values):
    e = discord.Embed(color=ecolor)
    for _name, _value in zip(names, values):
        e.add_field(name=_name, value=_value)

    return e



class ArgumentError(Exception):
    pass

class PermissionError(Exception):
    pass

class Unimplemented(Exception):
    pass
