# attridict
![GitHub](https://img.shields.io/github/license/alvinshaita/attridict.svg)

A Python package implementing atrribute dictionary.

This provides an easier and cleaner way to access dict values using their keys as attributes. It is typically a dict child, maintaining all the dict functionalities, but including some extra features.



## Installation
To install the package from PyPI, use:
```
pip install attridict
```




## Usage
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
## License
The project is MIT licensed
