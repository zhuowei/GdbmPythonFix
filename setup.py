from distutils.core import setup, Extension
# https://docs.python.org/3/extending/building.html
# https://raw.githubusercontent.com/python/cpython/9df346bf98069a87de14a3c2f69009d800994c63/Modules/_gdbmmodule.c

module1 = Extension('_gdbm',
                    sources = ['_gdbmmodule.c'],
                    library_dirs = ['/usr/local/Cellar/gdbm/1.18.1/lib'],
                    libraries = ['gdbm'])

setup (name = 'gdbm_extension',
       version = '1.0',
       description = 'gdbmmodule.c from Python 3 packaged for separate install',
       ext_modules = [module1])
