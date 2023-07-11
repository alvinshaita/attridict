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
>>> from attridict import AttriDict
>>> att = AttriDict()
>>> att
{}
>>> att.foo = "bar"
>>> att.foo
'bar'
>>> att
{'foo': 'bar'}
```

For backward compatibility, the project old import style is still usable.

```
>>> import attridict
>>> att = attridict()
>>> att
{}
```


A dict can be converted into an attridict object by passing it as an argument
```python
>>> from attridict import AttriDict

>>> data = {'red': 'hot', 'blue': 'cold'}

>>> colors = AttriDict(data)
>>> colors
{'red': 'hot', 'blue': 'cold'}

>>> colors.red
'hot'
```
<br/>

Modifying attridict object
```python
>>> from attridict import AttriDict

>>> data = {'red': 'hot', 'blue': 'cold'}

>>> colors = AttriDict(data)
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
>>> from attridict import AttriDict

>>> data = {'red': 'rose', 'blue': 'sky'}

>>> colors = AttriDict(data)
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
<br/>

Nested attribute access
```python
>>> from attridict import AttriDict

>>> data = {'foo': {}}
>>> att = AttriDict(data)

>>> att
{'foo': {}}

>>> att.foo.bar = 'baz'

>>> att.foo.bar
'baz'

>>> att
{'foo': {'bar': 'baz'}}
```
## License
The project is MIT licensed
