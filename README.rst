Bioconvert
==========

**Bioconvert** 是一个协作项目，旨在促进生命科学里的数据从一种格式到另一种格式的相互转换。

.. image:: https://badge.fury.io/py/bioconvert.svg
    :target: https://pypi.python.org/pypi/bioconvert

.. image:: https://secure.travis-ci.org/bioconvert/bioconvert.png
    :target: http://travis-ci.org/bioconvert/bioconvert

.. image:: https://coveralls.io/repos/github/bioconvert/bioconvert/badge.svg?branch=master
   :target: https://coveralls.io/github/bioconvert/bioconvert?branch=master

.. image:: http://readthedocs.org/projects/bioconvert/badge/?version=master
    :target: http://bioconvert.readthedocs.org/en/master/?badge=master
    :alt: Documentation Status

.. .. image:: https://badges.gitter.im/bioconvert/bioconvert.svg
    :target: https://gitter.im/bioconvert/Lobby?source=orgpage

.. image::  https://img.shields.io/github/issues/bioconvert/bioconvert.svg
    :target:  https://github.com/bioconvert/bioconvert/issues

.. image:: https://www.singularity-hub.org/static/img/hosted-singularity--hub-%23e32929.svg
   :target: https://singularity-hub.org/collections/135

.. image:: https://anaconda.org/bioconda/bioconvert/badges/platforms.svg
   :target: https://anaconda.org/bioconda/bioconvert

.. image::  https://anaconda.org/bioconda/bioconvert/badges/installer/conda.svg
    :target: https://conda.anaconda.org/bioconda
    
.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/bioconvert/bioconvert/master


:contributions: Want to add a convertor ? Please join https://github.com/bioconvert/bioconvert/issues/1
:issues: Please use https://github.com/bioconvert/bioconvert/issues


安装
###############

可以使用 **pip** 安装bioconvert::

    pip install bioconvert

同时，原作者提供了在bioconda (http://bioconda.github.io/)上的发行版::

    conda install bioconvert

同时在Singularity container上同样可用。参考以下链接
http://bioconvert.readthedocs.io/en/master/user_guide.html#installation 以了解更多。

使用
##########

::

    bioconvert fastq2fasta input.fastq output.fasta
    bioconvert gz2dsrc input.fq.gz output.dsrc2
    bioconvert bam2bed input.bam output.bed
    bioconvert --help

可用转换器
#######################

.. image:: https://raw.githubusercontent.com/bioconvert/bioconvert/master/doc/conversion.png
    :width: 80%


