# -*- coding: utf-8 -*-
"""Installer for the spirit.plone.forms package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CONTRIBUTORS.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    author="Thomas Massmann",
    author_email="thomas.massmann@it-spir.it",
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    description="Form fields, validators and widgets for Plone.",
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    extras_require={
        "test": [
            "plone.app.contenttypes",
            "plone.app.robotframework[debug]",
            "plone.app.testing",
            "plone.testing>=5.0.0",
        ],
    },
    include_package_data=True,
    install_requires=[
        "setuptools",
        # -*- Extra requirements: -*-
        "z3c.jbot",
    ],
    keywords="Python Plone CMS",
    license="GPL version 2",
    long_description=long_description,
    name="spirit.plone.forms",
    namespace_packages=["spirit", "spirit.plone"],
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["ez_setup"]),
    project_urls={
        "PyPI": "https://pypi.python.org/pypi/spirit.plone.forms",
        "Source": "https://github.com/it-spirit/spirit.plone.forms",
        "Tracker": "https://github.com/it-spirit/spirit.plone.forms/issues",
    },
    python_requires=">=3.7",
    url="https://github.com/it-spirit/spirit.plone.forms",
    version="0.1.0.dev0",
    zip_safe=False,
)
