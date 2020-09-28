# -*- coding: utf-8 -*-
# diff_archiver main implementation
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>

import os
import shutil
import time

from . import archivers
from . import loggers
from . import resolver
from . import patcher

class Error(Exception): pass

class DiffArchiver():
	"""DiffArchiver オブジェクトを使うと、ベースパッケージと最新パッケージとの間の差分を取得して、更新部分だけを入れたアーカイブを作ることができます。"""
	def __init__(self,base_archive_path, latest_archive_path, diff_archive_path, archiver=archivers.ZipArchiver(), logger=loggers.ConsoleLogger(), clean_base_package=False, skip_root = False):
		"""
			必要な情報を指定して、処理の準備をします。
			:param base_archive_path: ベースパッケージのパス(http/https から始まるとダウンロード)
			:type base_archive_path: str
			:param latest_archive_path: 最新パッケージのパス(http/https から始まるとダウンロード)
			:type latest_archive_path: str
			:param diff_archive_path: 作成するパッチのパス名
			:type diff_archive_path: str
			:param archiver: アーカイブ化するときに利用するアーカイバーオブジェクト
			:type archiver: archivers.ArchiverBase
			:param logger: ロギング用オブジェクト(None でログ出力をオフにする)
			:type logger: loggers.LoggerBase
			:param clean_base_package: 処理終了後、ベースパッケージを削除するならTrue
			:type clean_base_package: bool
			:param skip_root: パッケージのルートディレクトリをスキップする。
			:type skip_root: bool
		"""
		self.base_archive_path=base_archive_path
		self.latest_archive_path=latest_archive_path
		self.diff_archive_path=diff_archive_path
		self.archiver=archiver
		self.logger=logger
		self.clean_base_package=clean_base_package
		self.skip_root = skip_root

	def work(self):
		"""処理を実行する。"""
		started=time.time()
		self._log("Starting.")
		self._log("Base archive path: %s, latest archive path: %s, archiver: %s" % (self.base_archive_path, self.latest_archive_path, self.archiver.__class__.__name__))
		self._log("Resolving archives...")
		r=resolver.Resolver()
		base=r.resolve(self.base_archive_path)
		latest=r.resolve(self.latest_archive_path)
		self._log("Archive path resolution done.")
		self._log("Unpacking archives...")
		try:
			self.archiver.unpack(base,"base")
			self.archiver.unpack(latest,"latest")
		except archivers.Error as e:
			self._log("Error: failed to unpack (%s)" % e)
			raise Error("Could not unpack one of the archives.")
		#end except
		self._log("Archive unpacking done.")
		self._log("Applying patch...")
		p=patcher.Patcher()
		ret={}
		try:
			ret=p.patch("base", "latest", "patch")
		except patcher.Error as e:
			self._log("Failed to apply patch (%s)" % e)
		#end except
		self._log(str(ret))
		self._log("Patch done.")
		self._log("Packing into diff archive...")
		out_dir_path = "patch"
		if self.skip_root:
			out_dir_path = os.path.join("patch", os.listdir("patch")[0])
		try:
			self.archiver.pack(out_dir_path, self.diff_archive_path)
		except archivers.Error as e:
			self._log("Failed to pack into diff archive(%s)" % e)
		#end except
		self._log("Packing done.")
		self._log("Cleaning up unpacked resources.")
		self._clean_unpacked_resources()
		if self.clean_base_package:
			self._log("Cleaning base package")
			self._clean_base_package(base)
		#end cleane base package
		elapsed=time.time()-started
		self._log("Operation completed in %.2f seconds." % elapsed)
	#end work

	def _log(self, log_str):
		if not self.logger: return
		self.logger.log("diff_archiver: %s" % log_str)

	def _clean_unpacked_resources(self):
		shutil.rmtree("base")
		shutil.rmtree("latest")

	def _clean_base_package(self, base):
		os.remove(base)
