#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/testing")

class BoostWinapiConan(base.BoostBaseConan):
    name = "boost_winapi"
    version = "1.68.0"
    url = "https://github.com/bincrafters/conan-boost_winapi"
    lib_short_names = ["winapi"]
    header_only_libs = ["winapi"]
    b2_requires = [
        "boost_config",
        "boost_predef"
    ]
