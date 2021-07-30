from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Compile, Read and update your .conf file in python'
LONG_DESCRIPTION = 'A package that allows you to interact with .conf files withing python.'

# Setting up
setup(
    name="confcompiler",
    version=VERSION,
    author="NotReeceHarris (Reece Harris)",
    author_email="<reece.harris98@protonmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    url = 'https://github.com/NotReeceHarris/DotConfCompiler'
    install_requires=[],
    keywords=['python', 'compile', 'config', 'v.conf', 'update', 'write'],
    classifiers=[
        "Development Status :: 1 - Production",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
