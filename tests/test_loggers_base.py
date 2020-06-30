# -*- coding: utf-8 -*-

import unittest

import loggers

class TestLoggerBase(unittest.TestCase):
	def test_log(self):
		logger=loggers.LoggerBase()
		self.assertTrue(logger.log)
