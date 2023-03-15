# attridict
![Build Status](https://github.com/alvinshaita/attridict/actions/workflows/attridict.yml/badge.svg?branch=main)
![GitHub](https://img.shields.io/github/license/alvinshaita/attridict.svg)


A Python package implementing atrribute dictionary.

This provides an easier and cleaner way to access dict values using their keys as attributes. It is typically a dict child, maintaining all the dict functionalities, but including some extra features.



## Installation
To install the package from PyPI, use:
```
pip install attridict
```




## Usage

Creating an attridict object
```python
>>> import attridict
>>> att = attridict()
>>> att
{}
>>> att.foo = "bar"
>>> att.foo
'bar'
>>> att
{'foo': 'bar'}
```
<br/>

A dict can be converted into an attridict object by passing it as an argument
```python
>>> import attridict

>>> data = {'red': 'hot', 'blue': 'cold'}

>>> colors = attridict(data)
>>> colors
{'red': 'hot', 'blue': 'cold'}

>>> colors.red
'hot'
```
<br/>

Modifying attridict object
```python
>>> import attridict

>>> data = {'red': 'hot', 'blue': 'cold'}

>>> colors = attridict(data)
>>> colors
{'red': 'hot', 'blue': 'cold'}

>>> colors.blue
'cold'

>>> colors.blue = "sky"
>>> colors.red = "rose"
>>> colors.blue
'sky'
>>> colors.red
'rose'
>>> colors
{'red': 'rose', 'blue': 'sky'}

>>> colors.green = "grass"
>>> colors
{'red': 'rose', 'blue': 'sky', 'green': 'grass'}
```
<br/>

Typical `dict` operations work on attridict objects
```python
>>> import attridict

>>> data = {'red': 'rose', 'blue': 'sky'}

>>> colors = attridict(data)
>>> colors
{'red': 'rose', 'blue': 'sky'}

>>> colors.red
'rose'
>>> colors["red"]
'rose'

>>> colors["red"] = "tomato"
>>> colors["red"]
'tomato'
>>> colors.red
'tomato'
```
## License
The project is MIT licensed
