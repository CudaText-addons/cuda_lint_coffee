# Copyright (c) 2015-2016 The SublimeLinter Community
# Copyright (c) 2013-2014 Aparajita Fishman
# License: MIT
# Change for CudaLint: Alexey T.

import os
from cuda_lint import Linter, util
from cudax_nodejs import NODE_FILE

_js = os.path.join(os.path.dirname(__file__), 'node_modules', 'coffeescript', 'bin', 'coffee')


class Coffee(Linter):
    """Provides an interface to coffee --compile."""

    syntax = 'CoffeeScript'
    cmd = (NODE_FILE, _js, '--compile', '--stdio')
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.5'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>warning)): (?P<message>[^\r\n]+)'
    )
    error_stream = util.STREAM_STDERR
    comment_re = r'\s*/[/*]'
