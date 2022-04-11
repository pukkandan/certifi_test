from distutils.core import setup
import py2exe

setup(
    console=[{
        'script': './__main__.py',
        'dest_base': 'certifi_test',
    }],
    options={
        'py2exe': {
            'bundle_files': 0,
        }
    },
    zipfile=None
)
