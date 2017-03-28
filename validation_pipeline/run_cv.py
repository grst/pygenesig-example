#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Run the signature crossvalidation pipeline.

Performs a crossvalidation, generates a report and gmt files.

Usage:
  run_cv.py CONFIG_FILE

"""
from docopt import docopt
import os
from subprocess import call


if __name__ == '__main__':
    arguments = docopt(__doc__, version='signature crossvalidation 0.1')

    # pass config file to environment for runipy
    os.environ['config_file'] = arguments['CONFIG_FILE']

    # load config file to obtain the output directory
    exec(open(os.environ['config_file']).read())
    report_path = os.path.join(config['out_dir'], 'report.html')

    # run the notebook
    call(['runipy', 'crossvalidation.ipynb', '--html', report_path])
