#!/usr/bin/env python3

'''
python -m unittest tests.py
'''

import unittest

import attridict


class TestAttriDict(unittest.TestCase):
	def test_attridict(self):
		att = attridict()
		self.assertEqual(att, {})

		att.one = 111
		self.assertEqual(att.one, 111)
		self.assertEqual(att, {"one": 111})

		att.two = {"three": 333}
		self.assertEqual(att.two, {"three": 333})
		self.assertEqual(att, {"one": 111, "two": {"three": 333}})

		att.two.four = {"five": 555, "six": 666}
		self.assertEqual(att.two.four.five, 555)
		self.assertEqual(att.two.four.six, 666)

		self.assertEqual(att, {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}})


	def test_attridict2(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		self.assertEqual(att.one, 111)
		self.assertEqual(att.two, {"three": 333, "four": {"five": 555, "six": 666}})
		self.assertEqual(att.two.three, 333)
		self.assertEqual(att.two.four, {"five": 555, "six": 666})
		self.assertEqual(att.two.four.five, 555)
		self.assertEqual(att.two.four.six, 666)

		att.two = 222
		self.assertEqual(att.two, 222)

		att.three = {"four": 444, "five": 555}
		self.assertEqual(att.three, {"four": 444, "five": 555})
		self.assertEqual(att, {"one": 111, "two": 222, "three": {"four": 444, "five": 555}})


	def test_attridict3(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		self.assertEqual(att, data)
		self.assertEqual(att.one, data["one"])
		self.assertEqual(att.two, data["two"])
		self.assertEqual(att.two.three, data["two"]["three"])
		self.assertEqual(att.two.four, data["two"]["four"])
		self.assertEqual(att.two.four.five, data["two"]["four"]["five"])
		self.assertEqual(att.two.four.six, data["two"]['four']["six"])


	def test_dir(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		for i in data.keys():
			self.assertIn(i, att.__dir__())

		for i in data["two"].keys():
			self.assertIn(i, att.two.__dir__())

		for i in data["two"]["four"].keys():
			self.assertIn(i, att.two.four.__dir__())


	def test_attridict5(self):
		# #############################################################################
		# # problem tests
		# #############################################################################

		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att.three = {"four": 444, "five": 565}

		del att

		# #############################################################################

		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		self.assertEqual(data.__len__(), att.__len__())
		self.assertEqual(data["two"].__len__(), att.two.__len__())
		self.assertEqual(data["two"]["four"].__len__(), att.two.four.__len__())

		# ################################################################################


	def test_attridict6(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		self.assertEqual(att, data)


	def test_mutable(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att_mutable = att
		att.two = 222
		self.assertEqual(att, att_mutable)
		self.assertIs(att, att_mutable)


	def test_copy(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att_copy = att.copy()
		
		self.assertIsNot(att, att_copy)

		att.two = 222
		self.assertNotEqual(att, att_copy)
		self.assertEqual(att_copy, data)


	def test_to_dict(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		att_dict = att.to_dict()
		self.assertEqual(data, att_dict)

		self.assertEqual(type(att_dict), dict)
		self.assertEqual(type(att_dict["two"]), dict)
		self.assertEqual(type(att_dict["two"]["four"]), dict)


	def test_attridict10(self):

		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		del att.two.four.six
		self.assertEqual(att, {"one": 111, "two": {"three": 333, "four": {"five": 555}}})


	def test_deep_true(self):
		data = {"one": 111, "two": [{"three": 333, "four": 444}]}
		att = attridict(data, True)
		
		self.assertEqual(type(att.two[0]), attridict)
		self.assertEqual(att.two[0], {"three": 333, "four": 444})
		self.assertEqual(att.two[0].three, 333)


	def test_deep_false(self):
		data = {"one": 111, "two": [{"three": 333, "four": 444}]}
		att = attridict(data, False)

		self.assertEqual(type(att.two[0]), dict)
		self.assertEqual(att.two[0], {"three": 333, "four": 444})

	def test_to_dict_deep_list(self):
		data = {"one": 111, "two": [{"three": 333, "four": 444}]}
		att = attridict(data, True)
	
		self.assertEqual(type(att.two[0]), attridict)
		self.assertEqual(att.two[0], {"three": 333, "four": 444})
		self.assertEqual(att.two[0].three, 333)

		d_attr = att.to_dict()

		with self.assertRaises(AttributeError) as ctx:
			d_attr["two"][0].three
		self.assertEqual(str(ctx.exception), "'dict' object has no attribute 'three'")


	def test_to_dict_deep_tuple(self):
		data = {"one": 111, "two": tuple(({"three": 333, "four": 444},))}
		att = attridict(data, True)
	
		self.assertEqual(type(att.two[0]), attridict)
		self.assertEqual(att.two[0], {"three": 333, "four": 444})
		self.assertEqual(att.two[0].three, 333)

		d_attr = att.to_dict()

		with self.assertRaises(AttributeError) as ctx:
			d_attr["two"][0].three
		self.assertEqual(str(ctx.exception), "'dict' object has no attribute 'three'")

	def test_to_string_dunder_method(self):
		data = {"one": 111, "two": 222}
		att = attridict(data)

		self.assertEqual(att.__to_string__(), "{@'one': 111, 'two': 222@}")

if __name__ == "__main__":
	unittest.main()
