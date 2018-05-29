import pytest
import os
import shutil
from sdg import reset_all_csv
import pandas as pd

root = os.path.dirname(os.path.realpath(__file__))

def test_reset_csv():
    """Check that output_path is as expected"""

    testroot = os.path.join(root, 'testroot')

    os.makedirs(testroot, exist_ok=False)
    shutil.copytree(os.path.join(root, 'data'), os.path.join(testroot, 'data'))
    shutil.copytree(os.path.join(root, 'meta'), os.path.join(testroot, 'meta'))

    reset_all_csv(root=testroot)

    df = pd.read_csv(os.path.join(testroot, 'data', 'indicator_1-2-1.csv'))

    assert df.shape == (6, 3)

    # poor man's teardown
    shutil.rmtree(testroot)
