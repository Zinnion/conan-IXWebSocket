#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class NanomsgConan(ConanFile):
    name = "IXWebSocket"
    version = "1.3.1"
    description = "WebSocket client/server"
    topics = ("conan", "IXWebSocket", "communication", "socket", "websocket")
    url = "https://github.com/zinnion/conan-IXWebSocket"
    homepage = "https://github.com/machinezone/IXWebSocket"
    author = "Zinnion <mauro@zinnion.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    settings = "os", "compiler", "build_type", "arch"
    short_paths = True
    generators = "cmake"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"
    options = {
       "shared": [True, False],
       "enable_tests": [True, False],
       "enable_tools": [True, False],
       "enable_nngcat": [True, False],
    }

    default_options = (
        "shared=False",
        "enable_tests=False",
        "enable_tools=False",
        "enable_nngcat=False"
    )

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.compiler == "Visual Studio" and float(self.settings.compiler.version.value) < 14:
            raise Exception("ngg could not be built by MSVC <14")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.source_subfolder, build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="license", src=self.source_subfolder)
        self.copy(pattern="*.cpp", dst="include/ixwebsocket", src=self.source_subfolder + '/ixwebsocket')
        self.copy(pattern="*.h", dst="include/ixwebsocket", src=self.source_subfolder + '/ixwebsocket')
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
