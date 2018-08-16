import sacc
import datetime
import numpy as np
import sys
import matplotlib.pyplot as plt


theory_file='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory.sacc'
f=sacc.SACC.loadFromHDF(theory_file)
f.printInfo()
output_file='/global/cscratch1/sd/kakoon/sacc/theory_output.png'
f.plot_vector(out_name=output_file)
#tr_number=np.arange(len(f.tracers))
#for tr_i in tr_number:
#    tbin = np.logical_and(s.binning.binar['T1']==tr_i,s.binning.binar['T2']==tr_i)
#    if tr_i==0:
#        theory_0=f.mean.vector[tbin]
#    if tr_i==1:
#        theory_1=f.mean.vector[tbin]
#    if tr_i==2:
#        theory_2=f.mean.vector[tbin]
#    if tr_i==3:
#        theory_3=f.mean.vector[tbin]
#    if tr_i==4:
#        theory_4=f.mean.vector[tbin]
#    theory_bin=f.binning.binar['ls'][tbin]
#    string='%s, %s, '%(s.binning.binar['ls'][tbin],s.mean.vector[tbin])

#plt.figure()
#plt.plot(theory_bin, theory_0,'--', color='b', label='theory_0,0')
#plt.plot(theory_bin, theory_1,'--', color='g', label='theory_1,1')
#plt.plot(theory_bin, theory_2,'--', color='r', label='theory_2,2')
#plt.plot(theory_bin, theory_3,'--', color='cyan', label='theory_3,3')
#plt.plot(theory_bin, theory_4,'--', color='purple', label='theory_4,4')

#plt.xscale('log')
#plt.yscale('log')
#plt.legend(loc='best')
#plt.xlabel(r'$l$')
#plt.ylabel(r'$C_{l}$')
#plt.savefig('/global/cscratch1/sd/kakoon/sacc/theory_plot.png')
