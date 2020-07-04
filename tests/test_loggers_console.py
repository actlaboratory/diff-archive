# -*- coding: utf-8 -*-

import unittest

import diff_archiver.loggers

class TestLoggerConsole(unittest.TestCase):
	def test_log(self):
		logger=diff_archiver.loggers.ConsoleLogger()
		#printだけなので、存在確認のみ
		self.assertTrue(logger.log)
