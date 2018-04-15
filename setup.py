# Copyright 2018 Joe H. Rahme <joehakimrahme@gmail.com>
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""A web implementation of the classic Drugwars game.
"""

from setuptools import setup

repo_url = "http://github.com/joehakimrahme/dopewars"
version = "0.0.1"

setup(
    name='DopeWars',
    author="Joe H. Rahme",
    author_email="joehakimrahme@gmail.com",
    version=version,
    description="A web implementation of the classic Drugwars game",
    url=repo_url,
    download_url=repo_url + "/tarball/" + version,
    long_description=__doc__,
    install_requires=['Django'],
)
