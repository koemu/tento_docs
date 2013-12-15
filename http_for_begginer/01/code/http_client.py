#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 簡易HTTPクライアント
# required: Python 2.6 or later
# urllibを使っていますが、これはパッケージインストールの手間を省くためです。

import urllib

URI = "http://www.koemu.com:8888/"
res = urllib.urlopen( URI )

print "HTTP Status: %d" % res.getcode()
print "Body:\n%s" % res.read()