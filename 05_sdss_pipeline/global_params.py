# "Global" parameters, used in multiple notebooks,
# This .py file is imported into .ipynb notebooks with 'import global_params'

import numpy as np

# Used in a lot of places
ksz_lmin = 1500
ksz_lmax = 8000
nkbins = 100
kbin_edges = np.linspace(0, 0.3, nkbins+1)
kbin_centers = (kbin_edges[1:] + kbin_edges[:-1]) / 2.

# Halo model params, to compute P_ge^{fid} and P_gg^{fid}.
# Used in 01_prepare_gal_filter.ipynb.
# From https://github.com/alexlague/kSZquest/blob/main/prepare_gal_filter.py
hmodel_ks = np.geomspace(1e-5,100,1000)
hmodel_ms = np.geomspace(2e10,1e17,40)
hmodel_minz = 0.43
hmodel_maxz = 0.7
hmodel_zeff = 0.55
hmodel_ngal = 1e-4 # rough CMASS number density Mpc^-3

# Planck galmask
galmask_sky_percentage = 70
galmask_apodization = 0

# ACT data
act_dr = 5
act_rms_threshold = { 90: 70.0, 150: 70.0 }   # freq -> uK_arcmin

# SDSS data
sdss_survey = 'CMASS_North'
sdss_rpad = 500 # Mpc
sdss_pixsize = 10 # Mpc
sdss_zmin = 0.43
sdss_zmax = 0.7
sdss_zeff = 0.57         # only used in a few places, not very important
sdss_mock_type = 'qpm'   # mocks are also not used very much
sdss_nmocks = 1000

# Surrogate sims
surr_bg = 2.38   # galaxy bias
surr_bv = 0.3    # ad hoc multiplier on halo model P_ge, to make surrogates agree with data
surr_fnl = 250   # we run surrogate sims with fnl = [-surr_fnl, 0, surr_fnl]
num_surrogates = 1000