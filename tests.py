import unittest

import attridict


class TestAttriDict(unittest.TestCase):
	def test_attridict(self):
		att = attridict()
		# self.assertTrue(att == {})
		self.assertEqual(att, {})

		att.one = 111
		# self.assertTrue(att.one == 111)
		self.assertEqual(att.one, 111)
		# self.assertTrue(att == {"one": 111})
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


	def test_attridict4(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		self.assertTrue(all(i in att.__dir__() for i in ["one", "two"]))
		self.assertTrue(all(i in att.two.__dir__() for i in ["three", "four"]))
		self.assertTrue(all(i in att.two.four.__dir__() for i in ["five", "six"]))



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


	def test_attridict7(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att_mutable = att
		att.two = 222
		self.assertEqual(att, att_mutable)


	def test_attridict8(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)
		att_copy = att.copy()
		att.two = 222
		self.assertNotEqual(att, att_copy)
		self.assertEqual(att_copy, data)


	def test_attridict9(self):
		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		att_dict = att.to_dict()
		self.assertEqual(type(att_dict), dict)
		self.assertEqual(type(att_dict["two"]), dict)
		self.assertEqual(type(att_dict["two"]["four"]), dict)



	def test_attridict10(self):

		data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
		att = attridict(data)

		del att.two.four.six
		self.assertEqual(att, {"one": 111, "two": {"three": 333, "four": {"five": 555}}})


unittest.main()
