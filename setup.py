# coding=utf-8
"""
Setup for snappysonic 
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgerytorsosimulator',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgerytorsosimulator has been superseded by snappysonic"',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/UCL/snappysonic',
    author='Stephen Thompson',
    author_email='s.thompson@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging education',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
            'data'
        ]
    ),

    install_requires=[
        'snappysonic'
    ],

    entry_points={
        'console_scripts': [
            'snappysonic=snappysonic.__main__:main',
        ],
    },
)
