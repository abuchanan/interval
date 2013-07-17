from setuptools import setup, find_packages, Extension


setup(
    name='interval',
    description='Utilities for working with intervals.',
    long_description=open('README.md').read(),
    version='1.0.0',
    author='Alex Buchanan',
    author_email='buchanae@gmail.com',
    license='MIT',
    packages=find_packages(),
    ext_modules=[
        Extension('interval.intervaltree', ['interval/intervaltree.pyx']),
    ],
    install_requires=['cython'],
)
