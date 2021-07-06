#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="HTMLTestReport",
    version="1.0.0",
    keywords=("pip", "HTMLTestReport", "report"),
    description="A TestRunner for Python UnitTest",
    long_description="A TestRunner for use with the Python UnitTest framework",
    license="MIT Licence",

    url="https://github.com/likgjava/htmltestreport",
    author="outman",
    author_email="likg.java@163.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]
)
