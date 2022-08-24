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
>>> att.one = 111
>>> att.one
111
>>> att
{'one': 111}
```
```python
>>> data = {"one": 111, "two": {"three": 333, "four": 444}}
>>> att = attridict(data)
>>> att.two.four
444
>>> att
{"one": 111, "two": {"three": 333, "four": 444}}
>>> att.two = 222
>>> att
{"one": 111, "two": 222}
```
## License
The project is MIT licensed
