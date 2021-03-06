# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.k4.Ilcsoftpackage import Ilcsoftpackage 
from spack.pkg.k4.Ilcsoftpackage import ilc_url_for_version, k4_add_latest_commit_as_version


class Aidatt(CMakePackage, Ilcsoftpackage):
    """Tracking toolkit developed in the AIDA project."""

    homepage = "https://github.com/AIDASoft/aidaTT"
    url      = "https://github.com/AIDASoft/aidaTT/archive/v00-10.tar.gz"
    git      = "https://github.com/AIDASoft/aidaTT.git"

    maintainers = ['vvolkl']

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.10',     sha256='5379a369ee29bebeece7e814c0595bac9f08f2737ce03ae529b4b4e84dea1283')

    depends_on('ilcutil')
    depends_on('eigen')
    depends_on('generalbrokenlines')
    depends_on('dd4hep')
    depends_on('lcio')
