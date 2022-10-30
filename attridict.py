'''
	attridict.py:
		Alvin Shaita <alvinshaita@gmail.com>
'''

__author__	= "Alvin Shaita"
__email__	= "alvinshaita@gmail.com"


class AttriDictAttributes:
	__version__ = "0.0.3"


class AttriDict(dict, AttriDictAttributes):

	'''AttriDict'''
	def __init__(self, data = {}, deep = True):
		verified_dict = self.__type_verification(data)
		if verified_dict != None:
			data = verified_dict
		else:
			raise AttributeError("argument not valid")

		super(type(self), self).__init__(data)

		self.__to_attridict(data, deep)

		self.__reset()

	def __call__(self, data = {}):
		self = AttriDict()
		verified_dict = self.__type_verification(data)

		if verified_dict != None:
			data = verified_dict
		else:
			raise AttributeError("argument not valid")

		super(AttriDict, self).__init__(data)

		self.__to_attridict(data, deep)

		self.__reset()
		return self

	def __contains__(self):
		return self.__dict__.__contains__(key)

	def __delitem__(self, key):
		self.__dict__.__delitem__(key)

	def __dir__(self):
		return dir(self.__class__) + list(self.__dict__.keys())

	def __eq__(self, other):
		return self.__dict__.__eq__(other)

	def __getitem__(self, key):
		return self.__dict__.__getitem__(key)

	def __iter__(self):
		return len(self.__dict__.keys())

	def __len__(self):
		return len(self.__dict__.keys())

	def __ne__(self, other):
		return self.__dict__.__ne__(other)

	def __reduce__(self):
		return self.__dict__.__reduce__()

	def __repr__(self):
		return str(self.__dict__)

	def __setattr__(self, key, value):
		if not self.__valid_key(key):
			raise AttributeError("invalid key, '{0}'".format(key))

		if type(value) == dict:
			value = type(self)(value)
		
		self.__dict__.__setitem__(key, value)

		self.__reset()

	def __setitem__(self, key, value):
		self.__dict__.__setitem__(key, value)

	def __str__(self):
		return str(self.__dict__)


	def __copy__(self):
		return self.__class__(self)

	def __to_string__(self):
		return f"{{@{str(self.__dict__)[1:-1]}@}}"		

	def __reset(self):
		'''reset dict'''
		dict.__init__(self, self.__dict__)
		# super(AttriDict, self).__init__(self.__dict__)


	def __to_attridict(self, data, deep):
		for key, value in data.items():
			if deep:
				typ = type(value)
				if typ == dict:
					self.__dict__[key] = type(self)(value, deep)

				elif typ in [list, tuple]:
					value = list(value)

					for i, val in enumerate(value):
						if type(val) == dict:
							value[i] = type(self)(val, deep)
					
					self.__dict__[key] = typ(value)
				else:
					self.__dict__[key] = value
			else:
				self.__dict__[key] = value

	def __to_dict(self):
		for key, value in self.__dict__.items():
			typ = type(value)
			if typ == type(self):
				self.__dict__[key] = value.to_dict()

			elif typ in [list, tuple]:
				value = list(value)

				for i, val in enumerate(value):
					if type(val) == type(self):
						value[i] = val.to_dict()

				self.__dict__[key] = typ(value)
			else:	
				self.__dict__[key] = value


	def __try_dict_convertion(self, wannabe_dict):
		try:
			return dict(wannabe_dict)
		except Exception as err:
			raise AttributeError(err)


	def __type_verification(self, data):
		if type(data) != dict or type(data) != AttriDict:
			return self.__try_dict_convertion(data)
		return data


	def __valid_key(self, word):
		if word in dir(dict):
			return False
		return True


	def to_dict(self):
		self.__to_dict()
		return self.__dict__



	def clear(self):
		'''D.clear() -> None. Remove all items from D'''
		self.__dict__.clear()

	def copy(self):
		'''D.copy() -> a shallow copy of D'''
		# return self.__class__(self)
		return self.__copy__()

	def get(self, key, default = None):
		'''Return the value for key if key is in the attribute dictionary, else default.'''
		return self.__dict__.get(key, default)

	def items(self, *args, **kwargs):
		'''D.items() -> a set-like object providing a view on D's items'''
		return self.__dict__.items(*args, **kwargs)

	def keys(self):
		'''D.keys() -> a set-like object providing a view on D's keys'''
		return self.__dict__.keys()

	def pop(self, key, value = None):
		'''D.pop(k[,d]) -> v, remove specified key and return the corresponding value.\
		\nIf key is not found, d is returned if given, otherwise KeyError is raised
		'''
		return self.__dict__.pop(key, value)

	def popitem(self):
		return self.__dict__.popitem()

	def setdefault(self, key, default=None):
		'''Insert key with a value of default if key is not in the dictionary.\
		\n\nReturn the value for key if key is in the dictionary, else default.'''
		return self.__dict__.setdefault(key, default)

	def update(self, *args, **kwargs):
		return self.__dict__.update(*args, **kwargs)

	def values(self):
		'''D.values() -> an object providing a view on D's values'''
		return self.__dict__.values()


if __name__ == "attridict":
	import sys
	sys.modules[__name__] = AttriDict
