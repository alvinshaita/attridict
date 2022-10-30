'''
python setup.py install
'''

from setuptools import setup

import attridict

readme = open("README.md", 'r')
long_description = readme.read()

setup(
	name="attridict",
	version=attridict.__version__,
	author="Alvin Shaita",
	author_email="alvinshaita@gmail.com",
	url="https://github.com/alvinshaita/attridict",
	license="MIT License",
	packages=["."],
	keywords="attridict, attrdict, struct, dict, dot, attribute, attributes, dictionary, attr",
	description="A dict implementation with support for easy and clean access of its values through attributes",
	long_description=long_description,
	long_description_content_type='text/markdown',
	classifiers=[
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2",
        	"Programming Language :: Python :: 3",
        	"Programming Language :: Python :: Implementation :: CPython",
        	"Programming Language :: Python :: Implementation :: PyPy",
	]
)
