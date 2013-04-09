from distutils.core import setup

import interval


setup(
    name='interval',
    description='A small utility class for representing 0-based, half-open intervals.',
    long_description=open('README.md').read(),
    version=interval.__version__,
    author='Alex Buchanan',
    author_email='buchanae@gmail.com',
    license='MIT',
    py_modules=['interval']
)
