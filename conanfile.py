from conans import ConanFile, tools, os

class BoostWinapiConan(ConanFile):
    name = "Boost.Winapi"
    version = "1.64.0"
    url = "https://github.com/bincrafters/conan-boost-winapi"
    source_url = "https://github.com/boostorg/winapi"
    description = "Please visit http://www.boost.org/doc/libs/1_64_0/libs/libraries.htm"
    license = "www.boost.org/users/license.html"
    lib_short_name = "winapi"
    requires =  "Boost.Config/1.64.0@bincrafters/testing", \
                      "Boost.Predef/1.64.0@bincrafters/testing"
    
    def source(self):
        self.run("git clone --depth=50 --branch=boost-{0} {1}.git"
                 .format(self.version, self.source_url))

    def package(self):
        include_dir = os.path.join(self.build_folder, self.lib_short_name, "include")
        self.copy(pattern="*", dst="include", src=include_dir)

    def package_id(self):
        self.info.header_only()