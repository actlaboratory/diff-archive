# -*- coding: utf-8 -*-
# diff_archiver console logger
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>

from .base import LoggerBase

class ConsoleLogger(LoggerBase):
	"""コンソールに出力"""
	def log(self, log_str):
		print(log_str)
		