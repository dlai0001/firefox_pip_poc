##########################################################################
#This file is part of WTFramework. 
#
#    WTFramework is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    WTFramework is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with WTFramework.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

from distutils.command.build_py import build_py as _build_py
from distutils.core import setup
import sys
import os


class build_py(_build_py):
    """Specialized Python source builder."""

    # implement whatever needs to be different...
    print "Installing Firefox v22", sys.argv
    if "setup.py" not in sys.argv: # make sure user is running this from pip and not directly
        # download
        os.system('curl -o firefox_install.dmg "http://download.cdn.mozilla.net/pub/mozilla.org/firefox/releases/22.0/mac/en-US/Firefox%2022.0.dmg" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Connection: keep-alive" -H "Accept-Encoding: gzip,deflate,sdch" -H "Referer: http://www.mozilla.org/en-US/products/download.html?product=firefox-22.0&os=osx&lang=en-US" -H "Host: download.cdn.mozilla.net" -H "Accept-Language: en-US,en;q=0.8" -H "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36"')
        # mount
        os.system('hdiutil attach firefox_install.dmg')
    
        # copy
        os.system('cp -R /Volumes/Firefox/Firefox.app /Applications/Firefox_TEST.app')
    
        # unmount / delete
        os.system('hdiutil detach /Volumes/Firefox/') 
        os.system('rm firefox_install.dmg')

setup(
    name='zzfirefox_installer',
    version='22.0.0',
    author='David Lai',
    url='https://github.com/dlai0001',
    cmdclass={"_build_py": _build_py}
)
