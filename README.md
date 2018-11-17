Repackaged version of Python 3.6's GDBM native extension that links against Homebrew's GDBM (1.18.1).

You probably don't need this. If you get the error

```
>>> import dbm.gnu
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/dbm/gnu.py", line 3, in <module>
    from _gdbm import *
ModuleNotFoundError: No module named '_gdbm'
>>> 
```

Then this package might work (but you really should just install Python 3 from Homebrew, which doesn't have this issue.)

If you really need this to work on a Python.org-downloaded Python, run

```
brew install gdbm
python3 setup.py build
python3 setup.py install
```

The macOS version of Python downloaded from Python's website omits the GDBM module entirely.
Only the Homebrew version of Python 3 includes the GDBM module, but I prefer to install Python separately.

License: the .c and .h files are directly from CPython and follow its license.
