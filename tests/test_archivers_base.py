# -*- coding: utf-8 -*-

import unittest

import diff_archiver.archivers

class TestArchiverBase(unittest.TestCase):
	def test_pack(self):
		archiver=diff_archiver.archivers.ArchiverBase()
		self.assertTrue(archiver.pack)

	def test_unpack(self):
		archiver=diff_archiver.archivers.ArchiverBase()
		self.assertTrue(archiver.unpack)
