import pytest
import os
from sdg import build_data
from sdg.path import output_path
import json
import shutil

src_dir = os.path.dirname(os.path.realpath(__file__))

def test_build():
    """Check that output_path is as expected"""

    site_dir = os.path.join(src_dir, '_site')

    build_result = build_data(src_dir=src_dir, site_dir=site_dir, git=False)
    assert build_result

    exp_dirs = set(['comb', 'data', 'edges', 'headline', 'meta'])
    act_dirs = os.listdir(site_dir)

    assert all([a in exp_dirs for a in act_dirs])

    meta9 = json.load(open(output_path('9-3-1', ftype='meta', format='json', site_dir=site_dir)))
    assert meta9['indicator'] == '9.3.1'

    # poor man's teardown
    shutil.rmtree(site_dir)
