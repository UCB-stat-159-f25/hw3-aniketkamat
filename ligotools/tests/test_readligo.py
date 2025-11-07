import numpy as np
import pytest
from ligotools import readligo

def test_dq_channel_to_seglist_with_list():
    temp = np.zeros(50)
    for i in range(20):
        temp[i+5] = 1
    seg = readligo.dq_channel_to_seglist(temp, fs=1)
    print(seg)
    assert len(seg) == 1
    assert seg[0].start == 5
    assert seg[0].stop == 25

def test_dq2segs_with_dict():
    temp = np.zeros(80)
    for i in range(20):
        temp[i+5] = 1
    for j in range(10):
        temp[j+35] = 1
    tempdict = {'DEFAULT': temp}
    offset = 398409
    seg = readligo.dq2segs(tempdict,offset)
    seg = seg.seglist
    assert len(seg) == 2
    assert seg[0][0] == 5 + 398409
    assert seg[0][1] == 25 + 398409
    assert seg[1][0] == 35 + 398409
    assert seg[1][1] == 45 + 398409

if __name__ == '__main__':
    pytest.main([__file__, '-v'])