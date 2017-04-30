# Working Effectively with Unit Tests - Python

A Python companion to [Working Effectively with Unit Tests](https://leanpub.com/wewut). The Java examples used in WEwUT are translated to Python 2.7 (using `unittest` and `mock`)  for use by non-Java folk.

To run tests for a chapter:

    cd chX
    python -m unittest discover

Or if you wish to execute only a certain subfolder of tests:

    cd chX
    python -m unittest discover -s subfolder
