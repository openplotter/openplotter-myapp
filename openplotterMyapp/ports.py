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
import subprocess, os
from openplotterSettings import language

# This scripts define the addresses and ports used by this app to be shown when checking the system.
class Ports:
	def __init__(self,conf,currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(__file__)
		language.Language(currentdir,'openplotter-myapp',currentLanguage)

		# check the app and set the addresses.
		# self.usedPorts=[{'description':_('My App'), 'type':'UDP/TCP', 'address':'localhost', 'port':000000, 'direction':'out/in'}]
		self.usedPorts=[]
		try:
			subprocess.check_output(['systemctl', 'is-active', 'openplotter-myapp-read.service']).decode('utf-8')
			self.usedPorts=[{'description':_('My App'), 'type':'UDP', 'address':'localhost', 'port':self.conf.get('MYAPP', 'port'), 'direction':'out'}]
		except:pass
