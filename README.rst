DotConfCompiler
=================

.. image:: https://img.shields.io/badge/python-3-green.svg?style=flat-square
    :alt: Python3
    
.. image:: https://img.shields.io/pypi/v/confcompiler?style=flat-square
    :alt: PyPI

.. image:: https://img.shields.io/pypi/format/confcompiler?style=flat-square
    :alt: PyPI format

.. image:: https://img.shields.io/pypi/dm/confcompiler?style=flat-square
    :alt: PyPI downloads
    
    


Compile, Read and update your .conf file in python

Read data
~~~~~~~~~~

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

Write data
~~~~~~~~~~
 

.. code-block:: pycon

    >>> from confcompiler import ConfWrite
    >>>
    >>> ConfWrite('Config.conf', 'Hostname', '127.0.0.1')
    >>> ConfWrite('Config.conf', 'Connected', True)


.conf cheat sheat
~~~~~~~~~~~~~~~~~

.. code-block::

    Commenting - All comments must start with '#' and must be on
                 there on line, you cannot comment a line with 
                 data involved.

    Variables  - Data must start with a variable name then continued
                 with '=' after that the data.
