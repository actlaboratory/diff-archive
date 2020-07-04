# -*- coding: utf-8 -*-

import os
import shutil
import unittest

import diff_archiver.patcher

class TestPatcher(unittest.TestCase):
	def test_patch(self):
		self._makeData()
		p=diff_archiver.patcher.Patcher()
		ret=p.patch("tmp/base", "tmp/latest", "tmp/patch")
		self.assertEqual(ret["contained_files"], ret["removed_files"])
		self.assertEqual(ret["removed_directories"], 1)
		self._cleanData()
		self._makeData()
		with open("tmp/latest/a.txt", "a") as f:
			f.write("+++!")
		#end with
		ret=p.patch("tmp/base", "tmp/latest", "tmp/patch")
		self.assertEqual(ret["removed_files"], 1)
		self._cleanData()

	def _makeData(self):
		os.mkdir("tmp/base")
		os.mkdir("tmp/base/sub")
		with open("tmp/base/a.txt", "w") as f:
			f.write("top level")
		#end with
		with open("tmp/base/sub/b.txt", "w") as f:
			f.write("sub dir")
		#end with
		shutil.copytree("tmp/base", "tmp/latest")

	def _cleanData(self):
		if os.path.isdir("tmp/base"): shutil.rmtree("tmp/base")
		if os.path.isdir("tmp/latest"): shutil.rmtree("tmp/latest")
		if os.path.isdir("tmp/patch"): shutil.rmtree("tmp/patch")


