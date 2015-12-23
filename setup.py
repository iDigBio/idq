import os

from setuptools import setup, find_packages

from codecs import open

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r', 'utf-8') as f:
        return f.read()

setup(
    name='idq',
    version='0.6.0',
    description='iDigQuality Base Module',
    long_description=read('README.rst') + "\n\n",
    url='http://github.com/idigbio/idq/',   
    license='MIT',
    author='Alex Thompson',
    author_email='godfoder@acis.ufl.edu',
    packages=find_packages(exclude=['tests*']),
    install_requires=['flask', 'flask-bootstrap', 'flask-wtf', 'flask-nav', 'unicodecsv'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
