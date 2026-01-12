from distutils.core import setup, Extension

# 由于升级到ubuntu20.04,默认安装的CGAL版本是5.0, 而之前是4.12, 编译时需要指定c++14
# 并移除对 -lCGAL 的链接，因为5.0版本的CGAL是一个纯头文件库
# 移除不必要的 -L /usr/include/
# 后两个setup文件做类似修改
module = Extension("cgal_Segmentation_Module",
                   sources = ["neuron_cgal_segmentation.cpp"],
                   extra_compile_args=['-v','-std=c++14'],
                   extra_link_args=['-lgmp','-std=c++14'])

setup(name="CGAL_Segmentation",
      version = "1.0",
      description = "This is a package for cgal_Segmentation_Module",
      ext_modules = [module])
