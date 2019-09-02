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

import time, os
from openplotterSettings import language

# This class will be called once startup
class Start():
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(__file__)
		language.Language(currentdir,'openplotter-myapp',currentLanguage)
		# self.initialMessage will be printed at startup. If it is empty the function start will not be called. Use trasnlatable text: _('Starting My App...')
		self.initialMessage = ''

	# this funtion will be called only if self.initialMessage has content.
	def start(self):
		green = '' # green messages will be printed in green after the self.initialMessage
		black = '' # black messages will be printed in black after the green message
		red = '' # red messages will be printed in red in a new line

		# start any program and set the messages

		time.sleep(2)
		return {'green': green,'black': black,'red': red}

# This class will be called after startup and when the user checks the system
class Check():
	def __init__(self, conf, currentLanguage):
		self.conf = conf
		currentdir = os.path.dirname(__file__)
		language.Language(currentdir,'openplotter-myapp',currentLanguage)
		# self.initialMessage will be printed when checking system. If it is empty the function check will not be called. Use trasnlatable text: _('Checking My App...')
		self.initialMessage = ''


	def check(self):
		green = '' # green messages will be printed in green after the self.initialMessage
		black = '' # black messages will be printed in black after the green message
		red = '' # red messages will be printed in red in a new line

		# check any feature and set the messages

		return {'green': green,'black': black,'red': red}

