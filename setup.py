from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='sparc.asset',
      version=version,
      description="utilities to help with the management of assets",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://github.com/davisd50/sparc.asset',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['sparc'],
      include_package_data=True,
      package_data = {
          '': ['*.zcml']
        },
      zip_safe=False,
      install_requires=[
          'setuptools',
          'sparc.common',
          'zope.schema'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
