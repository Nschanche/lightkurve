import lightkurve as lk
from astropy.utils.data import get_pkg_data_filename
import numpy as np

filename_tess = get_pkg_data_filename("../data/tess25155310-s01-first-cadences.fits.gz")
# a local version of TABBY_TPF with ~ 2 days of data; should be sufficient for most tests
filename_tpf_tabby_lite = get_pkg_data_filename("../data/test-tpf-kplr-tabby-100-cadences.fits")

# Check if a Kepler TPF has a prf attribute 
# Check if tpf.prf returns an object of class PRF (specifically KeplerPRF)
# Check that the shape of the PRF object matches the TPF
# Check that the sum of the vanilla PRF values is very close to 1 (this wouldn't be true if we added stretch parameters)
def test_tpf_has_prfattribute():
	tpf = lk.KeplerTargetPixelFile(filename_tpf_tabby_lite)
	assert hasattr(tpf, 'prf')
	assert isinstance(tpf.prf, lk.prf.prfmodel.PRF)
	assert isinstance(tpf.prf, lk.prf.prfmodel.KeplerPRF)
	
	assert tpf.prf.shape == tpf.shape[1:3]
	
	assert np.isclose(np.sum(tpf.prf.evaluate()), 1., rtol=.01)
	

# Create a Kepler PRF directly (ie not tied to a TFP)
	
	
	


# Check if a TESS TPF has a prf attribute and that it returns an object of class PRF	
#def test_tpf_has_prfattribute():
#	tpf = lk.TessTargetPixelFile(filename_tess)
#	assert hasattr(tpf, 'prf')
#	assert isinstance(tpf.prf, lk.prf.prfmodel.PRF)
	

	
# Check if the output PRF has the right shape
# Check if the sum of the PRF is close to 1 (1000) when given flux=1 (1000)