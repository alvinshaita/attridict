'''
	attridict.py:
		Alvin Shaita <alvinshaita@gmail.com>
'''

__author__	= "Alvin Shaita"
__email__	= "alvinshaita@gmail.com"



class AttriDict(dict):
	def __init__(self, data = {}):
		'''
			setup everything with the data given,
			or with a blank dict
		'''
		verified_dict = self.__type_verification(data)

		if verified_dict != None:
			data = verified_dict
		else:
			raise AttributeError("argument not valid")

		super(AttriDict, self).__init__(data)

		self.__to_attridict(data)

		self.__reset()


	def __setattr__(self, key, value):
		'''
			called whenever there is an assignment
		'''
		if type(value) == dict:
			value = AttriDict(value)
		
		self.__dict__.__setitem__(key, value)

		self.__reset()



	def __contains__(self):
		return self.__dict__.__contains__(key)

	def __dir__(self):
		return dir(self.__class__) + list(self.__dict__.keys())

	def __eq__(self, other):
		return self.__dict__.__eq__(other)

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

	def __str__(self):
		return str(self.__dict__)



	def __reset(self):
		'''reset dict'''
		dict.__init__(self, self.__dict__)
		# super(AttriDict, self).__init__(self.__dict__)


	def __type_verification(self, data):
		'''verify input is actually of type dict'''

		if type(data) != dict or type(data) != AttriDict:
			return self.__try_dict_convertion(data)
		return data


	def __try_dict_convertion(self, wannabe_dict):
		''''
			if input is not of type dict, 
			try to convert to dict,
			if it cannot be converted to dict,
			return an error
		'''

		try:
			return dict(wannabe_dict)
		except Exception as err:
			raise AttributeError(err)


	def __to_attridict(self, data):
		for key, value in data.items():
			if type(value) == dict:
				self.__dict__[key] = AttriDict(value)
			else:
				self.__dict__[key] = value

	def __to_dict(self):
		for key, value in self.__dict__.items():
			if type(value) == AttriDict:
				self.__dict__[key] = value.to_dict()
			else:
				self.__dict__[key] = value


	def to_dict(self):
		self.__to_dict()
		return self.__dict__


	'''Typical stuff'''

	def copy(self):
		return self.__class__(self)

	def get(self, key, default = None):
		return self.__dict__.get(key, default)

	def items(self, *args, **kwargs):
		return self.__dict__.items(*args, **kwargs)

	def keys(self):
		return self.__dict__.keys()

	def pop(self, key, value = None):
		return self.__dict__.pop(key, value)

	def setdefault(self, key, default=None):
		return self.__dict__.setdefault(key, default)

	def values(self):
		return self.__dict__.values()
