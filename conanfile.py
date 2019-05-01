#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os

class NanomsgConan(ConanFile):
    name = "IXWebSocket"
    version = "1.3.7"
    description = "WebSocket client/server"
    topics = ("conan", "IXWebSocket", "communication", "socket", "websocket")
    url = "https://github.com/zinnion/conan-IXWebSocket"
    homepage = "https://github.com/maurodelazeri/IXWebSocket"
    author = "Zinnion <mauro@zinnion.com>"
    license = "MIT"
    exports = ["LICENSE.md"]
    exports_sources = ["CMakeLists.txt"]
    settings = "os", "compiler", "build_type", "arch"
    short_paths = True
    generators = "cmake"
    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def requirements(self):
        self.requires.add("OpenSSL/1.1.1b@zinnion/stable")
        self.requires.add("zlib/1.2.11@zinnion/stable")

    def source(self):
        tools.get("{0}/archive/v{1}.tar.gz".format(self.homepage, self.version))
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        os.environ['OPENSSL_ROOT_DIR'] = self.deps_cpp_info["OpenSSL"].rootpath
        #os.environ['zlib_DIR'] = self.deps_cpp_info["zlib"].rootpath
        cmake.configure(source_folder=self.source_subfolder, build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy(pattern="*.cpp", dst="include/ixwebsocket", src=self.source_subfolder + '/ixwebsocket')
        self.copy(pattern="*.h", dst="include/ixwebsocket", src=self.source_subfolder + '/ixwebsocket')
        self.copy("libixwebsocket.a", dst="lib", src=self.build_subfolder, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libs = ["ixwebsocket"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")
