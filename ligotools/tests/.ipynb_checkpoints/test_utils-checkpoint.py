import numpy as np
from scipy.signal import windows
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
from scipy.io import wavfile
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
#from ligotools import readligo as rl
from IPython.display import Audio
from ligotools.utils import whiten, write_wavfile, reqshift

def test_whiten():
    fs = 4096
    temp = np.linspace(0, 1, fs)
    stemp = np.sin(100 *np.pi *temp)
    ftemp = lambda x: np.ones(x.shape, x.dtype)
    result = whiten(stemp, ftemp, 1/fs)
    assert(np.mean(result) < 0.0001)
    assert(np.mean(result) > 0)
    assert(len(result)==4096) #proper length
    assert(np.var(result) < 0.01)
    assert(np.var(result) > 0)

def test_reqshift():
    fs = 4096
    temp = np.linspace(0, 1, fs)
    stemp = np.sin(100 *np.pi *temp)
    result = reqshift(stemp, 100, fs)
    assert(stemp.all()!=result.all())
    assert(len(result)==len(stemp))
    assert(np.max(result) < 2) #upper bound on shift

if __name__ == '__main__':
    pytest.main([__file__, '-v'])