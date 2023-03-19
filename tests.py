#!/usr/bin/env python3

'''
python -m unittest tests.py
'''

import unittest

import attridict


class TestAttriDict(unittest.TestCase):
	def test_attridict(self):
		# test growth through assignment
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
		# test conversion from dict
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		self.assertEqual(att.one, 111)
		self.assertEqual(att.two, {"three": 333, "four": {"five": 555, "six": 666}})
		self.assertEqual(att.two.three, 333)
		self.assertEqual(att.two.four, {"five": 555, "six": 666})
		self.assertEqual(att.two.four.five, 555)
		self.assertEqual(att.two.four.six, 666)

		# test reassignment of assigned values
		att.two = 222
		self.assertEqual(att.two, 222)

		att.three = {"four": 444, "five": 555}
		self.assertEqual(att.three, {"four": 444, "five": 555})
		self.assertEqual(att, {"one": 111, "two": 222, "three": {"four": 444, "five": 555}})


	def test_attridict3(self):
		# test value conservativity of converted dict
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		self.assertEqual(att, data)
		self.assertEqual(att.one, data["one"])
		self.assertEqual(att.two, data["two"])
		self.assertEqual(att.two.three, data["two"]["three"])
		self.assertEqual(att.two.four, data["two"]["four"])
		self.assertEqual(att.two.four.five, data["two"]["four"]["five"])
		self.assertEqual(att.two.four.six, data["two"]['four']["six"])


	def test_attridict5(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att.three = {"four": 444, "five": 565}

		del att

		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		self.assertEqual(data.__len__(), att.__len__())
		self.assertEqual(data["two"].__len__(), att.two.__len__())
		self.assertEqual(data["two"]["four"].__len__(), att.two.four.__len__())


	def test_attridict6(self):
		# test equality of attridict and initialized dict
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		self.assertEqual(att, data)


	def test_mutable(self):
		# test mutability of an attridict object
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att_mutable = att
		att.two = 222
		self.assertEqual(att, att_mutable)
		self.assertIs(att, att_mutable)


	def test_copy(self):
		# test attridict copy is not equal to original
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att_copy = att.copy()
		
		self.assertIsNot(att, att_copy)

		att.two = 222
		self.assertNotEqual(att, att_copy)
		self.assertEqual(att_copy, data)


	def test_to_dict(self):
		# test to_dict() returns dict
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		att_dict = att.to_dict()
		self.assertEqual(data, att_dict)

		self.assertEqual(type(att_dict), dict)
		self.assertEqual(type(att_dict["two"]), dict)
		self.assertEqual(type(att_dict["two"]["four"]), dict)


	def test_attridict10(self):
		# test del deletes attribute
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		del att.two.four.six
		self.assertEqual(att, {"one": 111, "two": {"three": 333, "four": {"five": 555}}})



	def test_attridict11(self):
		data = {}
		data["me"] = data

		att = attridict(data)

		self.assertEqual(att, data)
		self.assertEqual(att.me, data)
		self.assertEqual(att.me.me, data)


	def test_attridict12(self):
		one = {"one": "me"}
		two = {"two": "me"}

		one["two"] = two
		two["one"] = one

		att_one = attridict(one)
		att_two = attridict(two)

		self.assertEqual(att_one.one, "me")
		self.assertEqual(att_one.two, two)
		self.assertEqual(att_one.two, att_two)

		self.assertEqual(att_two.two, "me")
		self.assertEqual(att_two.one, one)
		self.assertEqual(att_two.one, att_one)


	def test_attridict14(self):
		data = {"one": 111, "two": [1,2,3], "three": {4,5,6}, "four": (7,8,9)}

		att = attridict(data)

		self.assertEqual(att, data)
		self.assertEqual(att.two, [1,2,3])
		self.assertEqual(att.three, {4,5,6})
		self.assertEqual(att.four, (7,8,9))


	def test_call(self):
		# test object call with key argument returns corresponding value
		data = {"one": 111, "two": {"three": 333}}

		att = attridict(data)

		self.assertEqual(att("one"), 111)
		self.assertEqual(att("two"), {"three": 333})
		self.assertEqual(att.two("three"), 333)


	def test_add(self):
		# test adding dict object and attridict object together
		data1 = {"one": 111, "two": 222}
		att1 = attridict(data1)

		data2 = {"three": 333, "four": 444}
		att2 = attridict(data2)
		
		self.assertEqual(att1 + data2, {"one": 111, "two": 222, "three": 333, "four": 444})
		self.assertEqual(data1 + att2, {"one": 111, "two": 222, "three": 333, "four": 444})
		self.assertEqual(att1 + att2, {"one": 111, "two": 222, "three": 333, "four": 444})


	def test_kwargs(self):
		data = {"one": 111, "two": 222}

		att = attridict(data, three=333, four=444)
		self.assertEqual(att, {"one":111, "two":222, "three": 333, "four": 444})


	def test_kwargs_overwrite(self):
		# test keyword argument overwrites original argument
		data = {"one": 111, "two": 222}

		att = attridict(data, two=333)
		self.assertEqual(att, {"one": 111, "two": 333})


if __name__ == "__main__":
	unittest.main()
