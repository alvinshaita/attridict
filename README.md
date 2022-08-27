# attridict
Attribute Dictonary

## Installation
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
