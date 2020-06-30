# -*- coding: utf-8 -*-
# diff_archiver archiver zip
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>

import os
import shutil
import zipfile
from .base import ArchiverBase, Error
class ZipArchiver(ArchiverBase):
	"""zipファイルのアーカイバー。"""

	def pack(self, out_dir_path, archive_path):
		try:
			ArchiverBase.unpack(self, out_dir_path, archive_path)
			shutil.make_archive(archive_path, "zip", out_dir_path)
		except Exception as e:
			raise Error(str(e))
	#end except

	def unpack(self, archive_path, out_dir_path):
		try:
			ArchiverBase.unpack(self, archive_path, out_dir_path)
			if not os.path.isdir(out_dir_path): os.mkdir(out_dir_path)
			with zipfile.ZipFile(archive_path) as archive:
				archive.extractall(out_dir_path)
			#end with
		except Exception as e:
			raise Error(str(e))
		#end except
	#end unpack
