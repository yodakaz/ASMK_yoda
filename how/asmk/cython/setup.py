from distutils.core import setup, Extension 
from Cython.Build import cythonize 
from numpy import get_include # cimport numpy を使うため

ext = Extension("hamming", sources=["hamming.pyx"], include_dirs=['.', get_include()])
setup(name="hamming", ext_modules=cythonize([ext]))