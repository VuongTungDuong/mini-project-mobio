# convert_py_to_pyx.py

# setup.py

from Cython.Build import cythonize
from setuptools import setup

setup(ext_modules=cythonize("conver_c.py", language_level=3))
