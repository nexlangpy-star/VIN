from setuptools import setup, find_packages
import os

setup(
    name="Lib_Devil",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    author="devil",
    description="BETA",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    include_package_data=True,
    data_files=[
        ('lib', ["Lib_Devil/TOP.cpython-313.so"]),
    ],
    zip_safe=False,
)