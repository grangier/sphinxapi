from setuptools import setup, find_packages
import os

version_info = (0, 0, 1)
__version__ =  ".".join(map(str, version_info))

setup(name='sphinxapi',
    version=__version__,
    description="SphinxAPI",
    long_description="",
    keywords='',
    author='Andrew Aksyonoff',
    author_email='',
    url='http://sphinxsearch.com/',
    license='GPL',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
