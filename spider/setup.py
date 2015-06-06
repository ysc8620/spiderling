from distutils.core import setup
import py2exe



# setup(console=["main.py"])


includes = ['scrapy', 'os', 'twisted']
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
        'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
        'Tkconstants', 'Tkinter']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
            'tk84.dll']

setup(
    options = {"py2exe": {
                      "includes": ['lxml.etree', 'lxml._elementpath','zope', 'gzip'],

                     }
          },
    console=['main.py']
)