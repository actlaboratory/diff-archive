# -*- coding: utf-8 -*-

import os
import shutil
import unittest

import diff_archiver

class TestDiffArchiver(unittest.TestCase):
	def test_local(self):
		if os.path.exists("base"): shutil.rmtree("base")
		if os.path.exists("latest"): shutil.rmtree("latest")
		if os.path.exists("patch"): shutil.rmtree("patch")
		archiver=diff_archiver.DiffArchiver("tests/data/base.zip", "tests/data/modified_patch.zip", "tmp/patch", logger=None)
		archiver.work()
		self.assertTrue(os.path.isfile("tmp/patch.zip"))
		os.remove("tmp/patch.zip")

