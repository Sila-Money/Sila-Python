import setuptools
from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='silasdk',


    version='0.2.22',

    description='Sila Python library for message signing and api wrapper',

    url="https://github.com/Sila-Money/Sila-Python",

    author='Sila',
    author_email='support@silamoney.com',

    license='Apache',

    classifiers=[

        # How stable is your project?
        #   3 - Alpha, 4 - Beta,5 - Production/Stable

        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6'

    ],

    keywords='Sila v0.2.22 Rest API',

    packages=find_packages(exclude=["tests", "tests.*"]),

    install_requires=["requests>=2.20.0", "pyaml>=15.8.2",
                      "eth-account==0.5.4", "pysha3==1.0.2"],

    zip_safe=False,

    include_package_data=True,

    extras_require={},


    package_data={},


    entry_points={}
)
