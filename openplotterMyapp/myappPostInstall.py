#!/usr/bin/env python3

# This file is part of Openplotter.
# Copyright (C) 2020 by Sailoog <https://github.com/openplotter/openplotter-myapp>
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

import os
from openplotterSettings import conf
from openplotterSettings import language
from .version import version

def main():
	conf2 = conf.Conf()
	currentdir = os.path.dirname(os.path.abspath(__file__))
	currentLanguage = conf2.get('GENERAL', 'lang')
	language.Language(currentdir,'openplotter-myapp',currentLanguage)

	print(_('Adding app to OpenPlotter...'))
	try:
		app = {
		'name': 'Myapp',
		'platform': 'both',
		'package': 'openplotter-myapp',
		'preUninstall': 'myappPreUninstall',
		'uninstall': 'openplotter-myapp',
		'sources': ['https://dl.cloudsmith.io/public/openplotter/openplotter-external/deb/debian'],
		'dev': 'no',
		'entryPoint': 'openplotter-myapp',
		'postInstall': 'myappPostInstall',
		'reboot': 'no',
		'module': 'openplotterMyapp'
		}
		gpgKey = currentdir+'/data/myapp.gpg.key'
		sourceList = currentdir+'/data/myapp.list'

		externalApps0 = eval(conf2.get('APPS', 'external_apps'))
		externalApps1 = []
		for i in externalApps0:
			if i['package'] != app['package']: externalApps1.append(i)
		externalApps1.append(app)
		conf2.set('APPS', 'external_apps', str(externalApps1))

		os.system('cp '+sourceList+' /etc/apt/sources.list.d')
		os.system('apt-key add - < '+gpgKey)
		os.system('apt update')
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

	###
	### Do here whatever you need after package installation. This file will be ran as sudo. 
	###
	
	print(_('Setting version...'))
	try:
		conf2.set('APPS', 'myapp', version) ### replace myapp by the name of your app, use the same name in openplotterMyapp.py and myappPreUninstall.py scripts.
		print(_('DONE'))
	except Exception as e: print(_('FAILED: ')+str(e))

if __name__ == '__main__':
	main()