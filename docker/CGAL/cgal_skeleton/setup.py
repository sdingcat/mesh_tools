from distutils.core import setup, Extension
module = Extension("calcification_Module",
                   sources = ["skeleton_module.cpp"],
                   extra_compile_args=['-std=c++14'],
                   extra_link_args=['-lmpfr','-lgmp'],
                   library_dirs = ['/usr/include/eigen3'],
                   include_dirs=['/usr/include/eigen3'])

setup(name="Calcfication",
      version = "1.0",
      description = "This is a package for calcification_Module",
      ext_modules = [module])
