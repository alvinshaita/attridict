
def assign_self(func):
	"""
	Set a new received object as the value to the key in the mapping container
	"""
	def wrapper(container, key):
		new_object = func(container, key)
		container[key] = new_object
		return container[key]
	
	return wrapper


class Mapping():

	@assign_self
	def __getattr__(self, key):
		"""
		Accesss value via attribute
		"""
		if not self._valid_key(key):
			raise AttributeError(
				"invalid key, '{key}'".format(key=key)
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

	@assign_self
	def __call__(self, key):
		"""
		Fetch value via object call
		eg. att(key)
		"""
		obj = self[key]
		return self._attrify(obj)


	def __add__(self, other):
		"""
		Add a dict object, or its child object to an attridict object
		"""
		if not isinstance(other, dict):
			raise AttributeError(
				"'{other}' is not a mapping".format(other=other)
			)

		return type(self)({**self, **other})

	def __radd__(self, other):
		"""
		Add an attridict object to a dict object, or its child object
		"""
		if not isinstance(other, dict):
			raise AttributeError(
				"'{other}' is not a mapping".format(other=other)
			)

		return type(self)({**other, **self})
