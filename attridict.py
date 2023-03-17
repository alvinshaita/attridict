'''
	attridict.py:
		Alvin Shaita <alvinshaita@gmail.com>
'''

__author__	= "Alvin Shaita"
__email__	= "alvinshaita@gmail.com"


class AttriDict(dict):
	'''AttriDict'''

	__version__ = "0.0.4"

	def __init__(self, data = {}):
		super(type(self), self).__init__(data)

	def __getattr__(self, key):
		self[key] = self._attrify(self[key])
		return self[key]

	def __setattr__(self, key, value):
		if not self._valid_key(key):
			raise AttributeError(
				"invalid key, '{key}'".format(key=key)
			)
		self[key] = value

	def __delattr__(self, key):
		del self[key]

	def __call__(self, key):
		"""
		Attribute fetch via object call
		eg. att(key)
		"""
		self[key] = self._attrify(self[key])
		return self[key]


	def _attrify(self, obj):
		if isinstance(obj, dict):
			obj = type(self)(obj)
		elif isinstance(obj, (list, set, tuple)):
			obj = type(obj)(self._attrify(i) for i in obj)
		return obj

	def _valid_key(self, word):
		if word in dir(dict):
			return False
		return True


	def to_dict(self):
		return dict(self)


if __name__ == "attridict":
	import sys
	sys.modules[__name__] = AttriDict
