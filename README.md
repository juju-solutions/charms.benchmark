[![Build Status](https://travis-ci.org/juju-solutions/charms.benchmark.svg?branch=master)](https://travis-ci.org/juju-solutions/charms.benchmark)
[![Coverage Status](https://coveralls.io/repos/juju-solutions/charms.benchmark/badge.svg)](https://coveralls.io/r/juju-solutions/charms.benchmark)

# charms.benchmark

charms.benchmark provides commands to ease the development of benchmark charms. You can either import the python library into your action, or use the equivalent CLI commands.

    #!/bin/bash

    benchmark-start || true

    ... (your code goes here) ...

    benchmark-finish || true

# Installation

    $ pip install charms.benchmark

# Development

    $ make venv
    $ . venv/bin/activate
    $ (venv) make develop
