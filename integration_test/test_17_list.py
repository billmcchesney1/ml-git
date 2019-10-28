"""
© Copyright 2020 HP Development Company, L.P.
SPDX-License-Identifier: GPL-2.0-only
"""

import os
import unittest

from integration_test.helper import check_output, clear, init_repository, add_file
from integration_test.helper import PATH_TEST, ML_GIT_DIR

from integration_test.output_messages import messages


class AcceptanceTests(unittest.TestCase):

    def setUp(self):
        os.chdir(PATH_TEST)
        self.maxDiff = None

    def test_01_list(self):
        clear(ML_GIT_DIR)
        clear(os.path.join(PATH_TEST,'local_git_server.git', 'refs', 'tags'))
        init_repository('dataset', self)

        add_file(self, 'dataset', '--bumpversion', 'new')

        self.assertIn(messages[17] % (os.path.join(ML_GIT_DIR, "dataset", "metadata"),
                                      os.path.join('computer-vision', 'images', 'dataset-ex')),
                      check_output("ml-git dataset commit dataset-ex"))

        self.assertIn('ML dataset\r\n|-- computer-vision\r\n|   |-- images\r\n|   |   |-- dataset-ex\r\n', check_output("ml-git dataset list"))