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
		archiver=diff_archiver.DiffArchiver("tests/data/base.zip", "tests/data/modified_latest.zip", "tmp/patch", logger=None)
		archiver.work()
		self.assertTrue(os.path.isfile("tmp/patch.zip"))
		os.remove("tmp/patch.zip")

	def test_local_clean(self):
		if os.path.exists("base"): shutil.rmtree("base")
		if os.path.exists("latest"): shutil.rmtree("latest")
		if os.path.exists("patch"): shutil.rmtree("patch")
		shutil.copyfile("tests/data/base.zip", "tests/data/base2.zip")
		archiver=diff_archiver.DiffArchiver("tests/data/base.zip", "tests/data/modified_latest.zip", "tmp/patch", logger=None, clean_base_package=True)
		archiver.work()
		self.assertTrue(os.path.isfile("tmp/patch.zip"))
		self.assertFalse(os.path.isfile("tests/data/base.zip"))
		shutil.move("tests/data/base2.zip", "tests/data/base.zip")
		self.assertTrue(os.path.isfile("tests/data/base.zip"))
		os.remove("tmp/patch.zip")


