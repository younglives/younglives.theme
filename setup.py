from setuptools import setup, find_packages
import os

version_path = os.path.join("younglives", "theme", "version.txt")

version = open(version_path).read().strip()

long_description = open(os.path.join("docs", "README.txt")).read()
long_description += "\n" + open(os.path.join("docs", "INSTALL.txt")).read()
long_description += "\n" + open(os.path.join("docs", "HISTORY.txt")).read()

setup(name='younglives.theme',
      version=version,
      description="Diazo theme for Young Lives",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Plone",
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
      ],
      keywords='',
      author='Michael Davis',
      author_email='M.R.Davis@cranfield.ac.uk',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['younglives'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': ['plone.app.testing', ]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
