'''
	attridict.py:
		Alvin Shaita <alvinshaita@gmail.com>
'''

__author__	= "Alvin Shaita"
__email__	= "alvinshaita@gmail.com"


class AttriMapping():

	def assign_self(func):
		"""
		Set a new received object as the value to the key in the mapping container
		"""
		def wrapper(container, key):
			new_object = func(container, key)
			container[key] = new_object
			return container[key]
		
		return wrapper

	@assign_self
	def __getattr__(self, key):
		"""
		Accesss value via attribute
		"""
		if not self._valid_key(key):
			raise AttributeError(
				"invalid key, '{key}'".format(key=key)
			)

		return self._attrify(self[key])

	def __setattr__(self, key, value):
		if not self._valid_key(key):
			raise AttributeError(
				"invalid key, '{key}'".format(key=key)
			)

		self[key] = value

	def __delattr__(self, key):
		del self[key]

	@assign_self
	def __call__(self, key):
		"""
		Fetch value via object call
		eg. att(key)
		"""		
		return self._attrify(self[key])


	def __add__(self, other):
		"""
		Add a dict object, or its child object to an attridict object
		"""
		if not isinstance(other, dict):
			raise AttributeError(
				"'{other}' is not a mapping".format(other=other)
			)

		return AttriDict({**self, **other})

	def __radd__(self, other):
		"""
		Add an attridict object to a dict object, or its child object
		"""
		if not isinstance(other, dict):
			raise AttributeError(
				"'{other}' is not a mapping".format(other=other)
			)

		return type(self)({**other, **self})



class AttriDict(dict, AttriMapping):
	'''AttriDict'''

	__version__ = "0.0.5"

	def __init__(self, *args):
		if args and not isinstance(*args, dict):
			raise AttributeError(
				"non dict argument provided"
			)

		super(type(self), self).__init__(*args)

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
	


if __name__ == "attridict":
	import sys
	sys.modules[__name__] = AttriDict
