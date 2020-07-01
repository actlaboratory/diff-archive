# -*- coding: utf-8 -*-

import unittest

import loggers

class TestLoggerConsole(unittest.TestCase):
	def test_log(self):
		logger=loggers.ConsoleLogger()
		#printだけなので、存在確認のみ
		self.assertTrue(logger.log)
