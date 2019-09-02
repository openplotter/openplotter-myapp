#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2019 by xxxx <https://github.com/xxxx/openplotter-myapp>
#                  
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup
from openplotterMyapp import version

setup (
	name = 'openplotterMyapp',
	version = version.version,
	description = 'This is a template to help create apps for OpenPlotter',
	license = 'GPLv3',
	author="xxxx",
	author_email='xxxx@xxxx.com',
	url='https://github.com/xxxx/openplotter-myapp',
	packages=['openplotterMyapp'],
	classifiers = ['Natural Language :: English',
	'Operating System :: POSIX :: Linux',
	'Programming Language :: Python :: 3'],
	include_package_data=True,
	entry_points={'console_scripts': ['openplotter-myapp=openplotterMyapp.openplotterMyapp:main','openplotter-myapp-read=openplotterMyapp.openplotterMyappRead:main','myappPostInstallation=openplotterMyapp.myappPostInstallation:main']},
	# entry_points: creating entry points you will be able to run these python scripts from everywhere.
		# openplotter-myapp = This is the GUI of your app
		# openplotter-myapp-read = You will use this file to be ran at startup as a service when needed using "sudo systemctl enable openplotter-myapp-read" in your code. See myappPostInstallation file.
		# myappPostInstallation = This file will be run just after package installation and it should contain any extra task to do like installing or removing packages, creating services...
	scripts=['bin/myScript','bin/myappPostInstallation'],
	# scripts: if you need to create entry points for python and non-python scripts like shell scripts you can use this.
		# myScript: a shell script
		# myappPostInstallation: a non-python post installation script. Use only one "entry_points" or "scripts" myappPostInstallation file to be ran after package installation. 
	data_files=[('share/applications', ['openplotterMyapp/data/openplotter-myapp.desktop']),('share/pixmaps', ['openplotterMyapp/data/openplotter-myapp.png']),],
	# data_files = Add files to the host system. This will work only when installed as debian package.
	)
