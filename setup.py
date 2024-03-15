#!/usr/bin/env python3
# Copyright 2021 CodeNotary, Inc. All rights reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='simple-passbolt-client',
      version='0.0.2',
      license="Apache License Version 2.0",
      description='Simple Python client for passbolt',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Simone Lazzaris',
      url='https://github.com/slazzaris/pybolt',
      # download_url='',
      packages=['pybolt'],
      keywords=['passbolt', 'gpgauth'],
      install_requires=[
        'certifi==2024.2.2',
        'cffi==1.16.0',
        'charset-normalizer==3.3.2',
        'cryptography==42.0.5',
        'idna==3.6',
        'PGPy==0.6.0',
        'pyasn1==0.5.1',
        'pycparser==2.21',
        'requests==2.31.0',
        'urllib3==2.2.1'
      ],
      classifiers=[
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
          'Programming Language :: Python :: 3.9',
      ],
      python_requires='>=3.9',
      )
