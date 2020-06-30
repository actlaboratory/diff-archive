# -*- coding: utf-8 -*-
# diff_archiver sample client
#Copyright (C) 2020 Yukio Nozawa <personal@nyanchangames.com>
import diff_archiver
archiver=diff_archiver.DiffArchiver("tests/data/base.zip", "tests/data/modified_patch.zip", "patch")
archiver.work()

