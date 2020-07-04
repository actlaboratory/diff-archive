# -*- coding: utf-8 -*-

import os
import shutil
import unittest
import zipfile

import diff_archiver.archivers

class TestZipArchiver(unittest.TestCase):
	def test_pack(self):
		os.mkdir("tmp/zip")
		for i in range(5):
			with open("tmp/zip/%s.txt", "w") as f:
				f.write(str(i))
			#end with
		#end for
		archiver=diff_archiver.archivers.ZipArchiver()
		archiver.pack("tmp/zip","tmp/myarchive")
		self.assertTrue(os.path.exists("tmp/myarchive.zip"))
		shutil.rmtree("tmp/zip")
		os.remove("tmp/myarchive.zip")

	def test_unpack(self):
		with open("tmp/zip.txt", "w") as f:
			f.write("unpacked")
		#end with
		with zipfile.ZipFile('tmp/trytounpack.zip', 'w', compression=zipfile.ZIP_DEFLATED) as new_zip:
			new_zip.write("tmp/zip.txt",arcname="zip.txt")
		#end with
		os.remove("tmp/zip.txt")
		archiver=diff_archiver.archivers.ZipArchiver()
		archiver.unpack("tmp/trytounpack.zip","tmp")
		self.assertTrue(os.path.exists("tmp/zip.txt"))
		os.remove("tmp/zip.txt")
		os.remove("tmp/trytounpack.zip")
