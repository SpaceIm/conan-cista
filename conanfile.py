from conans import ConanFile, tools
import os


class CistaConan(ConanFile):
    name = "cista"
    description = (
        "Cista++ is a simple, open source (MIT license) C++17 "
        "compatible way of (de-)serializing C++ data structures."
    )
    license = "MIT"
    topics = ("cista", "serialization", "deserialization", "reflection")
    homepage = "https://github.com/felixguendling/cista"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "compiler"
    no_copy_source = True

    def validate(self):
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, 17)

    def source(self):
        for file in self.conan_data["sources"][self.version]:
            filename = os.path.basename(file["url"])
            tools.download(filename=filename, **file)

    def package(self):
        self.copy("LICENSE", dst="licenses")
        self.copy("cista.h", dst="include")

    def package_info(self):
        self.cpp_info.names["cmake_find_package"] = "cista"
        self.cpp_info.names["cmake_find_package_multi"] = "cista"
