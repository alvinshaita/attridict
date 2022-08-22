import attridict


att = attridict()
assert(att == {})

att.one = 111
assert(att.one == 111)
assert(att == {"one": 111})

att.two = {"three": 333}
assert(att.two == {"three": 333})
assert(att == {"one": 111, "two": {"three": 333}})

att.two.four = {"five": 555, "six": 666}
assert(att.two.four.five == 555)
assert(att.two.four.six == 666)

assert(att == {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}})

del att

# # #############################################

data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)

assert(att.one == 111)
assert(att.two == {"three": 333, "four": {"five": 555, "six": 666}})
assert(att.two.three == 333)
assert(att.two.four == {"five": 555, "six": 666})
assert(att.two.four.five == 555)
assert(att.two.four.six == 666)

att.two = 222
assert(att.two == 222)

att.three = {"four": 444, "five": 555}
assert(att.three == {"four": 444, "five": 555})
assert(att == {"one": 111, "two": 222, "three": {"four": 444, "five": 555}})

del att


# __dir__
# #############################################
data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)
assert(all(i in att.__dir__() for i in ["one", "two"]))
assert(all(i in att.two.__dir__() for i in ["three", "four"]))
assert(all(i in att.two.four.__dir__() for i in ["five", "six"]))

del att


# #############################################





#############################################################################
# problem tests
#############################################################################

data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)
att.three = {"four": 444, "five": 565}

del att

#############################################################################


data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)

assert(data.__len__() == att.__len__())
assert(data["two"].__len__() == att.two.__len__())
assert(data["two"]["four"].__len__() == att.two.four.__len__())

del att
#############################################################################



##########################################################################################################
##########################################################################################################


data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)
assert(att == data)

del att

#######################################

data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)
att_mutable = att
att.two = 222
assert(att == att_mutable)

del att

#######################################

data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)
att_copy = att.copy()
att.two = 222
assert(att != att_copy)
assert(att_copy == data)

del att
#######################################

data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)

att_dict = att.to_dict()
assert(type(att_dict) == dict)
assert(type(att_dict["two"]) == dict)
assert(type(att_dict["two"]["four"]) == dict)

del att_dict

#######################################


data = {"one": 111, "two": {"three": 333, "four": {"five": 555, "six": 666}}}
att = attridict(data)

del att.two.four.six
assert(att == {"one": 111, "two": {"three": 333, "four": {"five": 555}}})

del att


#####################################################


print("Test End!!")
