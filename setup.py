#!/usr/bin/env python
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

from setuptools import setup

setup(name='tracestack',
      version='0.2.4',
      description='Instantly search your Python error messages on the web.',
      author='Dan Robinson',
      author_email='danrobinson010@gmail.com',
      url='https://www.github.com/danrobinson/tracestack',
      download_url='https://github.com/danrobinson/tracestack/tarball/0.2.4',
      long_description=long_description,
      packages=['tracestack'],
      test_suite="tests",
      tests_require=["mock", "tox"],
      entry_points = {'console_scripts': ['tracestack=tracestack.command_line:run'],}
     )