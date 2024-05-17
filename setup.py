#!/usr/bin/env python
"""
setup.py file for pycbc waveform plugin package to use ESIGMA waveforms
"""

from setuptools import Extension, setup, Command
from setuptools import find_packages

VERSION = '1.0'

def get_long_description():
    """Finds the README and reads in the description"""
    here = path.abspath(path.dirname(__file__))
    with open(path.join(here, "README.md")) as f:
        long_description = f.read()
    return long_description

setup (
    name = 'pycbc-esigma-plugin',
    version = VERSION,
    description = 'Waveform plugin for PyCBC',
    long_description = get_long_description(),
    author = 'Divyajyoti',
    author_email = 'divyajyoti.physics@gmail.com',
    url = 'http://www.pycbc.org/',
    download_url = 'https://github.com/divyajyoti09/pycbc_esigma_plugin.git'
    keywords = ['pycbc', 'signal processing', 'gravitational waves'],
    install_requires = ['pycbc', 'gwnr'],
    py_modules = ['ESIGMA'],
    entry_points = {"pycbc.waveform.td": ["ESIGMA = IMRESIGMAHM:IMRESIGMAHM_td", 
                                          "ESIGMA = IMRESIGMA:IMRESIGMA_td", 
                                          "ESIGMA = InspiralESIGMAHM:InspiralESIGMAHM_td",
                                          "ESIGMA = InspiralESIGMA:InspiralESIGMA_td"], },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
