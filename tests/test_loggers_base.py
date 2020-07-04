# -*- coding: utf-8 -*-

import unittest

import diff_archiver.loggers

class TestLoggerBase(unittest.TestCase):
	def test_log(self):
		logger=diff_archiver.loggers.LoggerBase()
		self.assertTrue(logger.log)
