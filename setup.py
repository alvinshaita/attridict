'''
python setup.py install
'''

from setuptools import setup

with open("README.md", 'r') as readme:
	long_description = readme.read()

setup(
	name="attridict",
	version="1.0",
	author="Alvin Shaita",
	author_email="alvinshaita@gmail.com",
	url="https://github.com/alvinshaita/attridict",
	license="MIT License",
	packages=["."],
	keywords="dict, attridict, attrdict, attribute, attributes, dictionary, attr, dot, struct",
	description="A dict object with support for easy access via attributes",
	long_description=long_description
)
