# Copyright (c) 2015-2016 The SublimeLinter Community
# Copyright (c) 2013-2014 Aparajita Fishman
# License: MIT
# Change for CudaLint: Alexey T.

import os
from cuda_lint import Linter, util

_node = 'node' if os.name=='nt' else 'nodejs'
_js = os.path.join(os.path.dirname(__file__), 'node_modules', 'coffee-script', 'bin', 'coffee')


class Coffee(Linter):
    """Provides an interface to coffee --compile."""

    syntax = 'CoffeeScript'
    cmd = (_node, _js, '--compile', '--stdio')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.5'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>warning)): (?P<message>[^\r\n]+)'
    )
    error_stream = util.STREAM_STDERR
    comment_re = r'\s*/[/*]'
