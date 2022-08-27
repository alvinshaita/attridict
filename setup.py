'''
python setup.py install
'''

from setuptools import setup

with open("README.md", 'r') as readme:
	long_description = readme.read()

setup(
	name="attridict",
	version="0.1",
	author="Alvin Shaita",
	author_email="alvinshaita@gmail.com",
	url="https://github.com/alvinshaita/attridict",
	license="MIT License",
	packages=["."],
	keywords="dict, attridict, attrdict, attribute, attributes, dictionary, attr, dot, struct",
	description="A dict implementation with support for easy and clean access of its values through attributes",
	long_description=long_description,
	long_description_content_type='text/markdown'
)
