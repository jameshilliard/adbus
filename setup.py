#!/usr/bin/env python3
# Copyright: 2017, CCX Technologies
"""distutils build and configuration script for python-adbus."""

from distutils.core import setup
from distutils.core import Extension
import sys

exec(open('adbus/__version__.py').read())

if "--cythonize" in sys.argv:
    from Cython.Build import cythonize
    sdbus = cythonize(
        [Extension("adbus.sdbus", ["adbus/sdbus.pyx"], libraries=["systemd"])]
    )
    sys.argv.remove("--cythonize")
else:
    sdbus = [Extension("adbus.sdbus", ["adbus/sdbus.c"], libraries=["systemd"])]


def build():
    """Build Package."""

    setup(
        name='adbus',
        version=__version__,
        description='asyncio based dbus interface',
        license='MIT',
        author='CCX Technologies',
        author_email='charles@ccxtechnologies.com',
        url='http://github.com/ccxtechnologies/python-adbus',
        download_url=
        'https://github.com/ccxtechnologies/python-adbus/archive/v0.2.1.tar.gz',
        platforms=['linux'],
        provides=['adbus'],
        packages=['adbus', 'adbus.server', 'adbus.client'],
        ext_modules=sdbus
    )


if __name__ == "__main__":
    build()
