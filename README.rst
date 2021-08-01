ConfCompiler
=================

.. image:: https://img.shields.io/badge/python-3-green.svg
    :target: https://www.python.org/
    :alt: Python3
    
.. image:: https://img.shields.io/pypi/v/confcompiler
    :target: https://pypi.org/project/confcompiler/
    :alt: PyPI

.. image:: https://img.shields.io/pypi/format/confcompiler
    :target: https://pypi.org/project/confcompiler/
    :alt: PyPI format

.. image:: https://img.shields.io/pypi/dm/confcompiler
    :target: https://pypi.org/project/confcompiler/
    :alt: PyPI downloads

.. image:: https://img.shields.io/pypi/status/confcompiler
    :target: https://pypi.org/project/confcompiler/
    :alt: PyPI downloads

Supported Data Types
~~~~~~~~~~~~~~~~~~~~

.. code-block::

    - Str
    - Int
    - Float
    - Bool
    - Tuple
    - List
    - Dict
    - Complex
    - Bytes

Read Data
~~~~~~~~~

.. code-block:: pycon

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

Write Data
~~~~~~~~~~
 

.. code-block:: pycon

    >>> from confcompiler import ConfWrite
    >>>
    >>> ConfWrite('Config.conf', 'Hostname', '127.0.0.1')
    >>> ConfWrite('Config.conf', 'Connected', True)


.conf Cheat Sheat
~~~~~~~~~~~~~~~~~

.. code-block::

    Commenting - All comments must start with '#' and must be on
                 there on line, you cannot comment a line with 
                 data involved.

    Variables  - Data must start with a variable name then continued
                 with '=' after that the data.
                
    Data Types - Str, Int, Float, Bool, Tuple, List, Dict, Complex, Bytes
