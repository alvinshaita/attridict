import sys

class AttriDict(dict):

	def __init__(self, data = {}):
		# print("__init__")
		super().__init__(data)

		attridicts = []


		wanna = self.type_verification(data)
		if self.type_verification(data):
			data = wanna

		for key, value in data.items():
			if type(value) == dict:
				attri = AttriDict(value)
				self.__dict__[key] = attri
				# self.attridicts.append(attri)
			else:
				self.__dict__[key] = value

		dict.__init__(self, self.__dict__)

		# print(self)


	def __call__(self, data = {}):
		# print("__call__\n")
		print("self", self)

		self = AttriDict(data)
		# print("bbb")

		wanna = self.type_verification(data)
		if self.type_verification(data):
			data = wanna


		for key, value in data.items():
			if type(value) == dict:
				attri = AttriDict(value)
				self.__dict__[key] = attri
				# self.attridicts.append(attri)
			else:
				self.__dict__[key] = value
		
		dict.__init__(self, self.__dict__)

		# print("=", self, "\n")
		return self

	def __del__(self):

		pass


	def type_verification(self, data):

		if type(data) != dict:
			data = self.try_dict_convertion(data)
			return data
	

	def try_dict_convertion(self, wannabe_dict):
		try:
			return dict(wannabe_dict)
		except Exception as err:
			raise AttributeError(err)



	def __setattr__(self, key, value):

		if type(value) == dict:
			value = AttriDict(value)
			# self.attridicts.append(value)
		self.__dict__.__setitem__(key, value)
		dict.__init__(self, self.__dict__)

	def __getattr__(self, key):
		print(key)


sys.modules[__name__] = AttriDict()
