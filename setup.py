# -*- coding: utf-8 -*-

from setuptools import setup

long_description = open("README.md").read()
install_requires = ['xlrd >= 0.9.3',
                    'xlwt >= 1.0.0']

extras_require = {'docs': ['sphinx>=1.2.2'],
                  'odml': ['python-odml>=0.1.0']}

setup(
    name="python-odmlviz",
    version='0.1.0',
    packages=['odmlviz', 'odmlviz.tests'],
    install_requires=install_requires,
    extras_require=extras_require,

    author="Jana Pick",
    author_email="j.pick@fz-juelich.de",
    description="",
    long_description=long_description,
    license="BSD",
    url='https://github.com/j-pick/python-odmlviz',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Scientific/Engineering']
)
