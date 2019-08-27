"""
© Copyright 2020 HP Development Company, L.P.
SPDX-License-Identifier: GPL-2.0-only
"""

import errno
import os
import os.path
import shutil
import stat
import subprocess


def clear(path):
    # SET the permission for files inside the .git directory to clean up
    for root, _, files in os.walk(path):
        for f in files:
            os.chmod(os.path.join(root, f), stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    try:
        shutil.rmtree(path)
    except Exception as e:
        print("except: ", e)

def check_output(command , output_expected):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    error_received = err.decode("utf-8")
    process.terminate()
    return output_expected in error_received

'''
def common_commands(self):
   create_dir('mlgit-testautomation')

   # assertion: 1 - Run the command  to DATASET
   os.chdir('mlgit-testautomation')
   old = os.getcwd()
   process = subprocess.Popen('ml-git init', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   self.assertTrue(check_output(process, "INFO - Initialized empty ml-git repository in"))
   process = subprocess.Popen('ml-git dataset remote add https://github.com/caitanojunior/mlgit-testautomation.git',
   stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   self.assertTrue(check_output(process,
   'INFO - ml-git project: add remote repository [https://github.com/caitanojunior/mlgit-testautomation.git] for [dataset]'))
   process = subprocess.Popen('ml-git store add br.edu.ufcg.virtus.hp.ml.gitml.test0 --credentials=default --region=us-east-1',
   stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
   self.assertTrue(check_output(process,
   'INFO - ml-git project: add store [s3h://br.edu.ufcg.virtus.hp.ml.gitml.test0] in region [us-east-1] with creds from profile [default]'))
   process = subprocess.Popen('ml-git dataset init', stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
   self.assertTrue(check_output(process, 'INFO - metadata init: [https://github.com/caitanojunior/mlgit-testautomation.git] @'))
'''