# -*- coding: utf-8 -*-
# diff_archiver patch algorithm
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>

import glob
import hashlib
import os
import shutil

class Error(Exception): pass

class Patcher():
	"""MD5とSHA-1の二重ハッシュで比較するパッチャー。"""
	def patch(self, base_path, latest_path, out_path):
		"""
			base_pathを基準として、latest_path との差分をとって、　out_pathにパッチを作ります。latest_pathには、最新バージョンのアーカイブを展開したディレクトリを指定していると仮定します。パッチ結果を格納した辞書を返します。

			:param base_path: ベースディレクトリのパス。
			:type base_path: str
			:param latest_path: 最新バージョンのパス
			:type latest_path: str
			:param out_path: 最終的にパッチとなるディレクトリのパス。このメソッド呼び出しで変更される。
			:type out_path: str
			:rtype: dict
		"""
		removed_files=0
		removed_directories=0
		base_set=self._getFiles(base_path)
		shutil.copytree(latest_path, out_path)
		out_set=self._getFiles(out_path)
		contained_files=len(out_set)
		for elem in base_set:
			if not elem in out_set: continue
			base_hashes=self._getHashes("%s\\%s" % (base_path, elem))
			out_hashes=self._getHashes("%s\\%s" % (out_path, elem))
			if base_hashes==out_hashes:
				os.remove("%s\\%s" % (out_path, elem))
				removed_files+=1
			#end if
		#end for
		dirs=self._getDirs(out_path)
		for elem in dirs:
			p="%s\\%s" % (out_path, elem)
			if len(os.listdir(p))==0:
				os.rmdir(p)
				removed_directories+=1
			#end if
		#end remove empty directories
		return {"contained_files": contained_files, "removed_files": removed_files, "removed_directories": removed_directories}
	#end patch

	def _getFiles(self,path):
		tmp=glob.glob("%s\\**" % (path), recursive=True)
		ret=set()
		for elem in tmp:
			if not os.path.isfile(elem): continue
			ret.add(elem[len(path)+1:])
		#end for
		return ret

	def _getDirs(self,path):
		tmp=glob.glob("%s\\**" % (path), recursive=True)
		ret=set()
		for elem in tmp:
			if not os.path.isdir(elem): continue
			ret.add(elem[len(path)+1:])
		#end for
		return ret


	def _getHashes(self, path):
		md5=""
		sha1=""
		with open(path,"rb") as f:
			bin=f.read()
			md5=hashlib.md5(bin).hexdigest()
			sha1=hashlib.sha1(bin).hexdigest()
		#end with
		return (md5, sha1)

	def _dirIsEmpty(self, path):
		return len(os.listdir(path))==0
