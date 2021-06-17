Unofficial Python 3 API wrapper to get data at [PDDIKTI](https://pddikti.kemdikbud.go.id/) Kemdikbud
====================================================================================================

[![License](https://img.shields.io/github/license/IlhamriSKY/PDDIKTI-kemdikbud-API.svg)](https://github.com/IlhamriSKY/PDDIKTI-kemdikbud-API/blob/master/LICENSE)
[![BuildStatus](https://travis-ci.com/IlhamriSKY/PDDIKTI-kemdikbud-API.svg?branch=main)](https://travis-ci.org/IlhamriSKY/PDDIKTI-kemdikbud-API)
[![Version 0.0.1](https://img.shields.io/badge/stable-0.0.1-brightgreen.svg "Version 0.0.1")](https://github.com/IlhamriSKY/PDDIKTI-kemdikbud-API)
[![python3.x](https://img.shields.io/badge/3.8%20%7C%203.9-blue.svg?&logo=python&label=Python)](https://www.python.org/downloads/release/python-391/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/8c2abcf7e3f648f281936af0c328c4d6)](https://www.codacy.com/gh/IlhamriSKY/PDDIKTI-kemdikbud-API/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=IlhamriSKY/PDDIKTI-kemdikbud-API&amp;utm_campaign=Badge_Grade)

Introduction
------------
Python API wrapper makes it easy for you to get data from the web [pddikti.kemdikbud.go.id](https://pddikti.kemdikbud.go.id/)

Requirements
------------
- Python 3.*
- requests

Installation
------------

    $ pip install pddiktipy

Synopsis
--------
Usage:
code:: python

    from pddiktipy import api

    a = api()

    print(a.search_all('ilham riski'))

