# -*- coding: utf-8 -*-
# diff_archiver archiver base
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>

class Error(Exception): pass

class ArchiverBase:
	"""アーカイバーを提供するベースクラス。 pack と unpack メソッドを実装しなければならない。"""

	def pack(self, out_dir_path, archive_path):
		"""
			パック処理を実行する。

			:param in_dir_path: パックするディレクトリのパス。
			:typ	e in_dir_path: str
			:param archive_path: 出力先のアーカイブファイルへのパス。
			:type archive_path: str
		"""
		pass

	def unpack(self, archive_path, out_dir_path):
		"""
			アンパック処理を実行する。

			:param archive_path: アーカイブのパス。
			:type archive_path: str
			:param out_dir_path: 解凍先ディレクトリのパス。この中に直接解凍される。
			:type out_dir_path: str
		"""
		pass
