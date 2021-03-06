# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Crawler integration with INSPIRE-HEP."""

from setuptools import find_packages, setup

readme = open('README.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'responses>=0.2.2',
    'pydocstyle>=1.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=1.8.0',
    'pytest-pep8>=1.0.6',
    'pytest>=2.8.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.4',
    ],
    'postgresql': [
        'invenio-db[postgresql,versioning]>=1.0.0a9',
    ],
    'mysql': [
        'invenio-db[mysql,versioning]>=1.0.0a9',
    ],
    'sqlite': [
        'invenio-db[versioning]>=1.0.0a9',
    ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)

setup_requires = [
    'autosemver~=0.1.9',
    'Babel>=1.3',
    'pytest-runner>=2.6.2',
]

install_requires = [
    'autosemver~=0.1.9',
    'six>=1.9.0',
    'Flask>=0.10.1',
    'python-scrapyd-api>=2.0.1',
    'pathlib2>=2.1.0',
    'invenio-celery>=1.0.0a3',
    # 'workflow>=2.0.0',
    'invenio_workflows~=6.0.2',
    # 'invenio_oaiharvester>=1.0.0a1',
]

packages = find_packages()


setup(
    name='inspire-crawler',
    autosemver=True,
    description=__doc__,
    long_description=readme,
    keywords='invenio inspire scrapy crawler',
    license='GPLv2',
    author='CERN',
    author_email='feedback@inspirehep.net',
    url='https://github.com/inspirehep/inspire-crawler',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.api_apps': [
            'inspire_crawler = inspire_crawler:INSPIRECrawler',
        ],
        'invenio_base.apps': [
            'inspire_crawler = inspire_crawler:INSPIRECrawler',
        ],
        'invenio_db.models': [
            'inspire_crawler = inspire_crawler.models',
        ],
        'invenio_celery.tasks': [
            'inspire_crawler = inspire_crawler.tasks',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 1 - Planning',
    ],
)
