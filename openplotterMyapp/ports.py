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
import os
from openplotterSettings import language

class Ports:
	def __init__(self,conf,currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(__file__)
		language.Language(currentdir,'openplotter-myapp',currentLanguage)

		#[{'id':0, description':_('My App'), 'data':[Signal K keys], 'type':'UDP/TCP', 'mode':'client/server', 'address':'localhost', 'port':000000, 'editable':'1'}]
		self.connections = []

		connectionId = 'conn1'
		try: port = int(self.conf.get('MYAPP', connectionId))
		except: port = 50000 #default port
		self.connections.append({'id':connectionId, 'description':_('My App'), 'data':['Random.Number1','Random.Number2'], 'type':'UDP', 'mode':'client', 'address':'localhost', 'port':port, 'editable':'1'})

	def usedPorts(self):
		state = self.conf.get('MYAPP', 'sending')
		if state == '1': return self.connections
