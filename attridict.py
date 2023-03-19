'''
	attridict.py:
		Alvin Shaita <alvinshaita@gmail.com>
'''

__author__	= "Alvin Shaita"
__email__	= "alvinshaita@gmail.com"

from mapping import Mapping

class AttriDict(dict, Mapping):
	'''AttriDict'''

	__version__ = "0.0.6"

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
	


if __name__ == "attridict":
	import sys
	sys.modules[__name__] = AttriDict
