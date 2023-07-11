from abc import ABC, abstractmethod


def assign_self(func):
    """
    Set the received object the value of the key in the mapping container
    """

    def wrapper(container, key):
        new_object = func(container, key)
        container[key] = new_object
        return container[key]

    return wrapper


__all__ = ["MapMixin"]


class MapMixin(ABC):

    @abstractmethod
    def _valid_key(self, key):
        pass

    @abstractmethod
    def _attrify(self, key):
        pass

    @assign_self
    def __call__(self, key):
        """
        Access value through object call
            eg. att(key)
        """
        obj = self[key]
        return self._attrify(obj)

    @assign_self
    def __getattr__(self, key):
        """
        Accesss value via attribute
        """
        if not self._valid_key(key):
            raise AttributeError(
                "invalid key, '{key}'".format(key=key)
            )

        if key not in self:
            raise AttributeError(
                "key does not exist, '{key}'".format(key=key)
            )

        obj = self[key]
        return self._attrify(obj)

    def __setattr__(self, key, value):
        if not self._valid_key(key):
            raise AttributeError(
                "invalid key, '{key}'".format(key=key)
            )

        self[key] = value

    def __delattr__(self, key):
        del self[key]

    def __add__(self, other):
        """
        Add a dict, or its child to an attridict object
        """
        if not isinstance(other, dict):
            raise TypeError(
                "'{other}' is not a mapping object".format(other=other)
            )

        return type(self)({**self, **other})

    def __radd__(self, other):
        """
        Add an attridict object to a dict, or its child
        """
        if not isinstance(other, dict):
            raise TypeError(
                "'{other}' is not a mapping object".format(other=other)
            )

        return type(self)({**other, **self})
