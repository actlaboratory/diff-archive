# -*- coding: utf-8 -*-

import unittest

import archivers

class TestArchiverBase(unittest.TestCase):
	def test_pack(self):
		archiver=archivers.ArchiverBase()
		self.assertTrue(archiver.pack)

	def test_unpack(self):
		archiver=archivers.ArchiverBase()
		self.assertTrue(archiver.unpack)
