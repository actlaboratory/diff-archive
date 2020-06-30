# -*- coding: utf-8 -*-

import os
import unittest

import resolver

class TestResolver(unittest.TestCase):
	def test_resolveLocal(self):
		r=resolver.Resolver()
		resolved=r.resolve("tests/dl.md")
		self.assertEqual(resolved, "tests/dl.md")

	def testHttps(self):
		fname="dl.md"
		remote="https://github.com/actlaboratory/diff_archiver/raw/master/tests/dl.md"
		if os.path.exists(fname): os.remove(fname)
		r=resolver.Resolver()
		resolved=r.resolve(remote)
		self.assertEqual(resolved, fname)
		self.assertTrue(os.path.exists(fname))
		os.remove(fname)
