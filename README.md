# DotConfCompiler

![Python3](https://img.shields.io/badge/python-3-green.svg?style=flat-square) ![PyPI](https://img.shields.io/pypi/v/confcompiler?style=flat-square) ![PyPI - Format](https://img.shields.io/pypi/format/confcompiler?style=flat-square)

Compile, Read and update your .conf file in python

# Read data
```pycon
>>> from confcompiler import ConfRead
>>>
>>> Hostname = ConfRead('Config.conf', 'Hostname')
>>> Hostname
127.0.0.1
>>> type(Hostname)
<class 'str'>
>>>
>>> Connected = ConfRead('Config.conf', 'Connected')
>>> Connected
True
>>> type(Connected)
<class 'bool'>
```

# Write data
```pycon
>>> from confcompiler import ConfWrite
>>>
>>> ConfWrite('Config.conf', 'Hostname', '127.0.0.1')
>>> ConfWrite('Config.conf', 'Connected', True)
```

# .conf cheat sheat
```
Commenting - All comments must start with '#' and must be on
             there on line, you cannot comment a line with 
             data involved.

Variables  - Data must start with a variable name then continued
             with '=' after that the data.
```
