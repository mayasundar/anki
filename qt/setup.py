#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys

import setuptools


def package_files(directory):
    entries = []
    for (path, directories, filenames) in os.walk(directory):
        entries.append((path, [os.path.join(path, f) for f in filenames]))
    return entries


# just the Python files for type hints?
pyonly = os.getenv("PYFILESONLY")
minimum_python_version = (3, 7)

if pyonly:
    extra_files = []
else:
    extra_files = package_files("aqt_data")

install_requires = [
    "beautifulsoup4",
    "requests",
    "send2trash",
    "pyaudio",
    "markdown",
    "jsonschema",
    "pyqt5>=5.9",
    'psutil; sys.platform == "win32"',
    'pywin32; sys.platform == "win32"',
    'darkdetect; sys.platform == "darwin"',
]

if sys.version_info < minimum_python_version:
    raise RuntimeError(
        "The minimum Python interpreter version required for Anki is '%s' "
        "and version '%s' was found!" % (minimum_python_version, sys.version_info)
    )


setuptools.setup(
    name="aqt",
    version="2.1.24",  # automatically updated
    author="Ankitects Pty Ltd",
    description="Anki's Qt GUI code",
    long_description="Anki's QT GUI code",
    long_description_content_type="text/markdown",
    url="https://apps.ankiweb.net",
    packages=setuptools.find_packages(".", exclude=["tests"]),
    data_files=extra_files,
    license="License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    classifiers=[],
    python_requires=">=3.7",
    package_data={"aqt": ["py.typed"]},
    install_requires=install_requires,
)
