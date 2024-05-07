'''
    attridict.py:
        Alvin Shaita <alvinshaita@gmail.com>
'''

__author__  = "Alvin Shaita"
__email__   = "alvinshaita@gmail.com"


from mixins import MapMixin


__all__ = ["AttriDict"]

class AttriDict(dict, MapMixin):
    '''AttriDict'''

    __version__ = "0.0.9"

    __all__ = ["to_dict"]

    def __init__(self, *args, **kwargs):
        if args and not isinstance(*args, dict):
            raise AttributeError(
                "non dict argument provided"
            )

        super(type(self), self).__init__(*args, **kwargs)

    def _attrify(self, obj):
        """
        Convert dict instance objects to attridict
        """
        if isinstance(obj, dict):
            obj = type(self)(obj)
        elif isinstance(obj, (list, set, tuple)):
            obj = type(obj)(self._attrify(i) for i in obj)

        return obj

    def _valid_key(self, key):
        """
        Check if the key provided is a valid key
        """
        if key in dir(self):
            return False

        return True

    def to_dict(self):
        """
        Return a dict equivalent of the attridict object
        """
        return dict(self)

    def copy(self):
        new_obj = type(self)(self)
        return new_obj



try:
    import yaml

    # yaml serialization
    def represent_attridict(dumper, data):
        return dumper.represent_mapping("!attridict", data)

    yaml.representer.Representer.add_representer(AttriDict, represent_attridict)


    def represent_attridict_safe(dumper, data):
        return dumper.represent_dict(data)

    yaml.representer.SafeRepresenter.add_representer(AttriDict, represent_attridict_safe)


    def construct_attridict(loader, node):
        value = loader.construct_mapping(node)
        return AttriDict(value)

    yaml.add_constructor("!attridict", construct_attridict, Loader=yaml.BaseLoader)
    yaml.add_constructor("!attridict", construct_attridict, Loader=yaml.FullLoader)
    yaml.add_constructor("!attridict", construct_attridict, Loader=yaml.SafeLoader)
    yaml.add_constructor("!attridict", construct_attridict, Loader=yaml.Loader)
    yaml.add_constructor("!attridict", construct_attridict, Loader=yaml.UnsafeLoader)
except Exception as e:
    ...



if __name__ == "attridict":
    import sys
    AttriDict.AttriDict = AttriDict
    sys.modules[__name__] = AttriDict
