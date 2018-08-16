import numpy as np
import healpy as hp
import h5py
import sacc
import glob
import matplotlib.pyplot as plt
import pymaster as nmt
import astropy.table
import pyccl as ccl
def make_hp_map(ra,dec,nside=2048):
    good = np.logical_or(np.logical_not(np.isnan(ra)),np.logical_not(np.isnan(dec)))
    pix_nums = hp.ang2pix(nside,np.pi/2.-dec[good]*np.pi/180,ra[good]*np.pi/180)
    pix_counts = np.bincount(pix_nums,minlength=12*nside**2)
    return pix_counts

filelist = glob.glob('/global/cscratch1/sd/kakoon/CoLoRe_2pt_sims/Mock_*noshear_linear_5*srcs*.h5')
bin0 = 0.5
bin1 = 0.6
nside=2048
npointsz=1000
map_tot = np.zeros(12*nside**2)
hist_tot = np.zeros(npointsz)
total_objs = 0
area = 4.*np.pi
rsd = True
for filename in filelist:
    test = h5py.File(filename,'r')
    print filename
    if rsd:
        zbin = (test['sources1']['Z_COSMO']+test['sources1']['DZ_RSD']>=bin0) &  (test['sources1']['Z_COSMO']+test['sources1']['DZ_RSD']<bin1)
    else:
        zbin = (test['sources1']['Z_COSMO']>=bin0) &  (test['sources1']['Z_COSMO']<bin1) 
    map_aux = make_hp_map(test['sources1']['RA'][zbin],test['sources1']['DEC'][zbin],nside=nside)
    if rsd:
        hist, binedges = np.histogram(test['sources1']['Z_COSMO'][zbin]+test['sources1']['DZ_RSD'][zbin],range=(0,2.0),bins=npointsz)
    else:
        hist, binedges = np.histogram(test['sources1']['Z_COSMO'][zbin],range=(0,2.0),bins=npointsz)
    map_tot = map_tot + map_aux
    hist_tot = hist_tot + hist
    total_objs = total_objs + np.count_nonzero(zbin)
    test.close
hhub=0.69
cosmo = ccl.Cosmology(ccl.Parameters(Omega_c=0.266,Omega_b=0.049,h=hhub,sigma8=0.8,n_s=0.96,),matter_power_spectrum='halofit')
zmax=2.5
ngrid=3072
rsm =5.0/hhub
shear=False
if shear:
    a_grid=np.sqrt((ccl.comoving_radial_distance(cosmo,1./(1+zmax))*(1+2./ngrid)/ngrid)**2+rsm**2)
else:
    a_grid=np.sqrt((ccl.comoving_radial_distance(cosmo,1./(1+zmax))*(1+2./ngrid)/ngrid)**2*0.5+rsm**2)
bias_tab = astropy.table.Table.read('../2pt_validation/mass_mapping/bz_dz.txt',format='ascii')
tracer=ccl.ClTracer(cosmo,'nc',False,False,n=(0.5*binedges[1:]+0.5*binedges[:-1],hist_tot/np.sum(hist_tot)),bias=(bias_tab['col1'],bias_tab['col2']),r_smooth=a_grid)

cls = hp.anafast(map_tot/np.mean(map_tot)-1.)
ells = np.arange(len(cls))
shot_noise = area/total_objs
cl_th=ccl.angular_cl(cosmo,tracer,tracer,ells)
tab_th = astropy.table.Table([ells,cl_th],names=('l','cl'))
tab_th.write('comparison_theory_new_smooth_dplus_1percent_norsd.fits.gz',overwrite=True)

w=nmt.NmtWorkspace()
bpw=nmt.NmtBin(nside,nlb=25)
field = nmt.NmtField(np.ones_like(map_tot),[map_tot/np.mean(map_tot)-1])
w.compute_coupling_matrix(field,field,bpw)

def compute_master(fa,fb,wsp,clb) :
    cl_coupled=nmt.compute_coupled_cell(fa,fb)
    cl_decoupled=wsp.decouple_cell(cl_coupled,cl_bias=clb)
    return cl_decoupled

cls_nmt = compute_master(field,field,w,clb=None)[0]
ell_eff = bpw.get_effective_ells()
tab = astropy.table.Table([np.arange(len(cls)),cls],names=('l','cl'))
tab.write('comparison_anafast_dplus_1percent_norsd.fits.gz',overwrite=True)
tab2 = astropy.table.Table([ell_eff,cls_nmt],names=('l','cl'))
tab2.write('comparison_nmt_dplus_1percent_norsd.fits.gz',overwrite=True)
plt.plot(ell_eff,ell_eff*(ell_eff+1)*(cls_nmt-shot_noise),label='NaMaster')
plt.plot(ells,ells*(ells+1)*(cls-shot_noise),label='Anafast')
plt.plot(ells,ells*(ells+1)*cl_th,label='Theory')
plt.xlabel('$l$')
plt.ylabel('$l(l+1)C_{l}$')
plt.xscale('log')
#plt.yscale('log')
plt.legend(loc='best')
plt.show()
plt.savefig('test_nmt_anafast_dplus_norsd.png')
plt.figure()
plt.plot(ells,(cls-shot_noise)/cl_th-1.)
plt.xlabel('$l$')
plt.ylabel('$\Delta C_{l}$')
plt.xscale('log')
plt.ylim(-2,2)
plt.show()
plt.savefig('test_nmt_anafast_dplus_norsd_ratio.png')