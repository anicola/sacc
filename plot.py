import sacc
import datetime
import numpy as np
import sys
import matplotlib.pyplot as plt
import h5py

##all_run_file=open('/global/cscratch1/sd/kakoon/sacc/all_run_file.txt', 'w')
run=True
run_half=True
save_f='save_half_noshear.out'
save_f_2='save_half_shear.out'
j=1
smt='5'
theory_file='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory_shear_h_%s.sacc'%smt
theory_2='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory_gauss_0.05_radeccut_delell25_RSD.sacc'
#theory_3='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory_shear_noh.sacc'
#theory_4='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory_noshear_noh.sacc'
#theory_5='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory_5.sacc'
output_name_separate='/global/cscratch1/sd/kakoon/sacc/mean_10_runs_%s_Fullsky_separate_noshear_linear_5_delell25_RSD.png'%smt
output_name='/global/cscratch1/sd/kakoon/sacc/mean_10_runs_%s_Fullsky_shear_linear.png'%smt
output_chi_name='/global/cscratch1/sd/kakoon/sacc/chi_data_theory_%s_Fullsky_linear.png'%smt
f=sacc.SACC.loadFromHDF(theory_file)
f2=sacc.SACC.loadFromHDF(theory_2)
#f3=sacc.SACC.loadFromHDF(theory_3)
#f4=sacc.SACC.loadFromHDF(theory_4)
#f5=sacc.SACC.loadFromHDF(theory_5)
seed_list=np.arange(10)+11*np.ones(10)###[11,12,13,14,15,16,17,18,19,20]
title="seed %i ~ %i"%(seed_list[0],seed_list[-1])
if run:
    for i in seed_list:
        shot_noise_bin_a, shot_noise_bin_a_2=[],[]
        input_str='%i'%i
        #filename='/global/cscratch1/sd/kakoon/namaster_output/cat_%i_shear_linear_3072_101017_Fullsky.sacc'%i
        filename='/global/cscratch1/sd/kakoon/namaster_output/cat_%i_noshear_linear_%s_gauss_0.05_radeccut_3072_102317_Fullsky_delell25.sacc'%(i,smt)
        filename2='/global/cscratch1/sd/kakoon/namaster_output/cat_%i_noshear_linear_%s_gauss_0.05_radeccut_3072_110617_Fullsky_delell25.sacc'%(i,smt)
        filename=filename2
        print "reading :" + filename +"    for shear"
        print "reading :" + filename2 +"   for no-shear"
        s=sacc.SACC.loadFromHDF(filename)
        s2=sacc.SACC.loadFromHDF(filename2)
        for numb, tracer in enumerate(s.tracers):
            ngal=np.sum(tracer.Nz)
            print ngal
            shot_noise_bin=4*np.pi/ngal
            shot_noise_bin_a=np.append(shot_noise_bin_a,shot_noise_bin)
        for numb_2, tracer2 in enumerate(s2.tracers):
            ngal_2=np.sum(tracer2.Nz)
            shot_noise_bin_2=4*np.pi/ngal_2
            shot_noise_bin_a_2=np.append(shot_noise_bin_a_2, shot_noise_bin_2)
        #print shot_noise_bin_a, shot_noise_bin_a_2
        tr_number=np.arange(len(s.tracers))
        for tr_i in tr_number:
            tbin = np.logical_and(s.binning.binar['T1']==tr_i,s.binning.binar['T2']==tr_i)
            tbin2=np.logical_and(s2.binning.binar['T1']==tr_i,s2.binning.binar['T2']==tr_i)
            if j==1:
                if tr_i==0:
                    mean_array_0=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_array_noshear_0=[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]
                if tr_i==1:
                    mean_array_1=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_array_noshear_1=[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]
                if tr_i==2:
                    mean_array_2=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_array_noshear_2=[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]
                if tr_i==3:
                    mean_array_3=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_array_noshear_3=[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]
                if tr_i==4:
                    mean_array_4=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_array_noshear_4=[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]
            else:
                if tr_i==0:
                    mean_array_0=np.concatenate((mean_array_0,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_array_noshear_0=np.concatenate((mean_array_noshear_0,[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]),axis=0)
                if tr_i==1:
                    mean_array_1=np.concatenate((mean_array_1,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_array_noshear_1=np.concatenate((mean_array_noshear_1,[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]),axis=0)
                if tr_i==2:
                    mean_array_2=np.concatenate((mean_array_2,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_array_noshear_2=np.concatenate((mean_array_noshear_2,[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]),axis=0)
                if tr_i==3:
                    mean_array_3=np.concatenate((mean_array_3,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_array_noshear_3=np.concatenate((mean_array_noshear_3,[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]),axis=0)
                if tr_i==4:
                    mean_array_4=np.concatenate((mean_array_4,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_array_noshear_4=np.concatenate((mean_array_noshear_4,[s2.mean.vector[tbin2]]-shot_noise_bin_a_2[tr_i]),axis=0)
        j+=1
    if i==seed_list[-1]:
        binning_array=s.binning.binar['ls'][tbin]
        binning_array_2=s2.binning.binar['ls'][tbin2]
        mean_array_00=np.mean(mean_array_0,axis=0)
        std_00=np.std(mean_array_0,axis=0)
        mean_array_11=np.mean(mean_array_1,axis=0)
        std_11=np.std(mean_array_1,axis=0)
        mean_array_22=np.mean(mean_array_2,axis=0)
        std_22=np.std(mean_array_2,axis=0)
        mean_array_33=np.mean(mean_array_3,axis=0)
        std_33=np.std(mean_array_3,axis=0)
        mean_array_44=np.mean(mean_array_4,axis=0)
        std_44=np.std(mean_array_4,axis=0)
        mean_noshear_array_00=np.mean(mean_array_noshear_0,axis=0)
        std_noshear_00=np.std(mean_array_noshear_0,axis=0)
        mean_noshear_array_11=np.mean(mean_array_noshear_1,axis=0)
        std_noshear_11=np.std(mean_array_noshear_1,axis=0)
        mean_noshear_array_22=np.mean(mean_array_noshear_2,axis=0)
        std_noshear_22=np.std(mean_array_noshear_2,axis=0)
        mean_noshear_array_33=np.mean(mean_array_noshear_3,axis=0)
        std_noshear_33=np.std(mean_array_noshear_3,axis=0)
        mean_noshear_array_44=np.mean(mean_array_noshear_4,axis=0)
        std_noshear_44=np.std(mean_array_noshear_4,axis=0)

i=0
kk=1

if run_half:
    for i in seed_list:
        shot_noise_bin_a, shot_noise_bin_a_2=[],[]
        input_str='%i'%i
        filename3='/global/cscratch1/sd/kakoon/namaster_output/cat_%i_noshear_linear_halfbz_%s_gauss_0.05_radeccut_3072_120517_Fullsky_delell25.sacc'%(i,smt)
        filename4=filename3###'/global/cscratch1/sd/kakoon/namaster_output/cat_%i_noshear_linear_half_%s_3072_101617_Fullsky.sacc'%(i,smt) ###3072_101617_Fullsky.sacc'%i###_%s_3072_101617_Fullsky.sacc'%(i,smt)
        print "reading :" + filename3 + "for shear, half bias"
        print "reading :" + filename4 + "for noshear, half bias"
        s=sacc.SACC.loadFromHDF(filename3)
        s2=sacc.SACC.loadFromHDF(filename4)
        for numb, tracer in enumerate(s.tracers):
            ngal=np.sum(tracer.Nz)
            shot_noise_bin=4*np.pi/ngal
            shot_noise_bin_a=np.append(shot_noise_bin_a,shot_noise_bin)
        for numb_2, tracer2 in enumerate(s2.tracers):
            ngal_2=np.sum(tracer2.Nz)
            shot_noise_bin_2=4*np.pi/ngal_2
            shot_noise_bin_a_2=np.append(shot_noise_bin_a_2, shot_noise_bin_2)
        tr_number=np.arange(len(s.tracers))
        for tr_i in tr_number:
            tbin = np.logical_and(s.binning.binar['T1']==tr_i,s.binning.binar['T2']==tr_i)
            if kk==1:
                if tr_i==0:
                    mean_half_0=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_noshear_half_0=[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]
                if tr_i==1:
                    mean_half_1=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_noshear_half_1=[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]
                if tr_i==2:
                    mean_half_2=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_noshear_half_2=[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]
                if tr_i==3:
                    mean_half_3=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_noshear_half_3=[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]
                if tr_i==4:
                    mean_half_4=[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]
                    mean_noshear_half_4=[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]
            else:
                if tr_i==0:
                    mean_half_0=np.concatenate((mean_half_0,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]), axis=0)
                    mean_noshear_half_0=np.concatenate((mean_noshear_half_0,[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]), axis=0)
                if tr_i==1:
                    mean_half_1=np.concatenate((mean_half_1,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]), axis=0)
                    mean_noshear_half_1=np.concatenate((mean_noshear_half_1,[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]), axis=0)
                if tr_i==2:
                    mean_half_2=np.concatenate((mean_half_2,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]), axis=0)
                    mean_noshear_half_2=np.concatenate((mean_noshear_half_2,[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]), axis=0)
                if tr_i==3:
                    mean_half_3=np.concatenate((mean_half_3,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_noshear_half_3=np.concatenate((mean_noshear_half_3,[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]), axis=0)
                if tr_i==4:
                    mean_half_4=np.concatenate((mean_half_4,[s.mean.vector[tbin]]-shot_noise_bin_a[tr_i]),axis=0)
                    mean_noshear_half_4=np.concatenate((mean_noshear_half_4,[s2.mean.vector[tbin]]-shot_noise_bin_a_2[tr_i]), axis=0)
        kk+=1
    if i==seed_list[-1]:
        mean_noshear_half_00=4*np.mean(mean_noshear_half_0,axis=0)
        std_noshear_half_00=np.std(mean_noshear_half_0,axis=0)
        mean_noshear_half_11=4*np.mean(mean_noshear_half_1,axis=0)
        std_noshear_half_11=np.std(mean_noshear_half_1,axis=0)
        mean_noshear_half_22=4*np.mean(mean_noshear_half_2,axis=0)
        std_noshear_half_22=np.std(mean_noshear_half_2,axis=0)
        mean_noshear_half_33=4*np.mean(mean_noshear_half_3,axis=0)
        std_noshear_half_33=np.std(mean_noshear_half_3,axis=0)
        mean_noshear_half_44=4*np.mean(mean_noshear_half_4,axis=0)
        std_noshear_half_44=np.std(mean_noshear_half_4,axis=0)
        np.savetxt(save_f,(mean_noshear_half_00,std_noshear_half_00,mean_noshear_half_11,std_noshear_half_11,mean_noshear_half_22,std_noshear_half_22,mean_noshear_half_33,std_noshear_half_33,mean_noshear_half_44,std_noshear_half_44), delimiter=',')
        mean_half_00=4*np.mean(mean_half_0,axis=0)
        std_half_00=np.std(mean_half_0,axis=0)
        mean_half_11=4*np.mean(mean_half_1,axis=0)
        std_half_11=np.std(mean_half_1,axis=0)
        mean_half_22=4*np.mean(mean_half_2,axis=0)
        std_half_22=np.std(mean_half_2,axis=0)
        mean_half_33=4*np.mean(mean_half_3,axis=0)
        std_half_33=np.std(mean_half_3,axis=0)
        mean_half_44=4*np.mean(mean_half_4,axis=0)
        std_half_44=np.std(mean_half_4,axis=0)
        np.savetxt(save_f_2,(mean_half_00,std_half_00,mean_half_11,std_half_11,mean_half_22,std_half_22,mean_half_33,std_half_33,mean_half_44,std_half_44), delimiter=',')
else:
    print "reading..."+save_f+" and "+save_f_2
    save_array_1=np.loadtxt(save_f, delimiter=',')
    save_array_2=np.loadtxt(save_f_2,delimiter=',')
    mean_noshear_half_00,std_noshear_half_00,mean_noshear_half_11,std_noshear_half_11,mean_noshear_half_22,std_noshear_half_22,mean_noshear_half_33,std_noshear_half_33,mean_noshear_half_44,std_noshear_half_44=save_array_1
    mean_half_00,std_half_00,mean_half_11,std_half_11,mean_half_22,std_half_22,mean_half_33,std_half_33,mean_half_44,std_half_44=save_array_2
plt.figure()
number=len(seed_list)
cmap=plt.get_cmap('gist_rainbow')
colors=[cmap(i) for i in np.linspace(0,1,number)]
for i,color in enumerate(colors,start=0):### in range(1,10):
    plt.plot(binning_array, mean_array_0[i], color=color,  label='seed=%i'%seed_list[i])  
    print len(binning_array_2),len(mean_array_noshear_0[i])
    plt.plot(binning_array_2, mean_array_noshear_0[i], color=color, ls='--', label='noshear, seed=%i'%seed_list[i])
plt.xscale('log')
plt.yscale('log')
#plt.legend(loc='best')
plt.xlabel(r'$l$')
plt.ylabel(r'$C_{l}$')
plt.savefig('/global/cscratch1/sd/kakoon/sacc/shear_noshear_seed11_20.png')


plt.figure()
plt.errorbar(binning_array, mean_array_00, yerr=std_00, fmt='-', color="b",label='0,0')
plt.errorbar(binning_array, mean_array_11, yerr=std_11, fmt='-', color="g",label='1,1')
plt.errorbar(binning_array, mean_array_22, yerr=std_22, fmt='-', color="r",label='2,2')
plt.errorbar(binning_array, mean_array_33, yerr=std_33, fmt='-', color="cyan",label='3,3')
plt.errorbar(binning_array, mean_array_44, yerr=std_44, fmt='-', color='purple',label='4,4')
number=10
cmap=plt.get_cmap('gist_rainbow')
colors=[cmap(i) for i in np.linspace(0,1,number)]
#for i,color in enumerate(colors,start=0):### in range(1,10):
#    if i==3 or i==9:
#        plt.plot(binning_array, mean_array_0[i], color=color,  label='seed=%i'%(i+11))
#    else:
#        plt.plot(binning_array, mean_array_0[i], color='black', label='seed=%i'%(i+11))
tr_number=np.arange(len(f.tracers))
for tr_i in [0,1,2,3,4]:
    tbin = np.logical_and(f2.binning.binar['T1']==tr_i,f2.binning.binar['T2']==tr_i)
    plt.plot(f2.binning.binar['ls'][tbin],f2.mean.vector[tbin],'--',label='theory_%i,%i' %(tr_i,tr_i))
plt.xscale('log')
plt.yscale('log')
plt.ylim(1e-8,1e-3)
plt.legend(loc='best')
plt.xlabel(r'$l$')
plt.ylabel(r'$C_{l}$')
plt.savefig(output_name)

fig,ax=plt.subplots(2,2,figsize=(20,20))  
##plt.tight_layout()
mll1=binning_array*(binning_array+1)
mll2=binning_array_2*(binning_array_2+1)
##ax[0,0].errorbar(binning_array, mll1*mean_array_00, yerr=std_00, fmt='-',color='b', label='shear')
##ax[0,0].errorbar(binning_array, mll1*mean_half_00, yerr=std_half_00, fmt='-',color='orange', label='4*half_bz')
ax[0,0].errorbar(binning_array, mll1*mean_noshear_half_00, yerr=std_noshear_half_00, fmt='-',color='g', label='4*half_bz,no_shear')
ax[0,0].errorbar(binning_array_2, mll2*mean_noshear_array_00, yerr=mll2*std_noshear_00,fmt='-', color='r', label='no_shear')
tr_number=np.arange(len(f.tracers))
tr_n_2=np.arange(len(f2.tracers))
#tr_n_3=np.arange(len(f3.tracers))
tbin=np.logical_and(f.binning.binar['T1']==0,f.binning.binar['T2']==0)
tbin2=np.logical_and(f2.binning.binar['T1']==0,f2.binning.binar['T2']==0)
#tbin3=np.logical_and(f3.binning.binar['T1']==0,f3.binning.binar['T2']==0)
#tbin4=np.logical_and(f4.binning.binar['T1']==0,f4.binning.binar['T2']==0)
#tbin5=np.logical_and(f5.binning.binar['T1']==0,f5.binning.binar['T2']==0)
ax[0,0].set_title('0,0')
#ax[0,0].plot(f5.binning.binar['ls'][tbin5],f5.mean.vector[tbin5],'-.',color='r',label='theory_5')
l=f.binning.binar['ls'][tbin]
l2=f2.binning.binar['ls'][tbin2]
##ax[0,0].plot(l,l*(l+1)*f.mean.vector[tbin],'--',color='black',label='theory_shear_h')
ax[0,0].plot(l2,l2*(l2+1)*f2.mean.vector[tbin2],':',color='black',label='theory_noshear_h')
#ax[0,0].plot(f3.binning.binar['ls'][tbin3],f3.mean.vector[tbin3],'--',color='purple',label='theory_shear_noh')
#ax[0,0].plot(f4.binning.binar['ls'][tbin4],f4.mean.vector[tbin4],':',color='purple',label='theory_noshear_noh')
ax[0,1].set_title('1,1')
##ax[0,1].errorbar(binning_array, mll1*mean_array_11, yerr=std_11, fmt='-',color='b', label='shear')
##ax[0,1].errorbar(binning_array, mll1*mean_half_11, yerr=std_half_11, fmt='-',color='orange', label='4*half_bz')
ax[0,1].errorbar(binning_array, mll1*mean_noshear_half_11, yerr=std_noshear_half_11, fmt='-',color='g', label='4*half_bz,no_shear')
ax[0,1].errorbar(binning_array_2,mll2*mean_noshear_array_11, yerr=mll2*std_noshear_11,fmt='-', color='r', label='no_shear')
tbin=np.logical_and(f.binning.binar['T1']==1,f.binning.binar['T2']==1)
tbin2=np.logical_and(f2.binning.binar['T1']==1,f2.binning.binar['T2']==1)
l=f.binning.binar['ls'][tbin]
l2=f2.binning.binar['ls'][tbin2]
#tbin3=np.logical_and(f3.binning.binar['T1']==1,f3.binning.binar['T2']==1)
#tbin4=np.logical_and(f4.binning.binar['T1']==1,f4.binning.binar['T2']==1)
#tbin5=np.logical_and(f5.binning.binar['T1']==1,f5.binning.binar['T2']==1)
#ax[0,1].plot(f5.binning.binar['ls'][tbin5],f5.mean.vector[tbin5],'-.',color='r',label='theory_5')
#ax[0,1].plot(f.binning.binar['ls'][tbin],l*(l+1)*f.mean.vector[tbin],'--',color='black',label='theory_shear_h')
ax[0,1].plot(f2.binning.binar['ls'][tbin2],l2*(l2+1)*f2.mean.vector[tbin2],':',color='black',label='theory_noshear_h')
#ax[0,1].plot(f3.binning.binar['ls'][tbin3],f3.mean.vector[tbin3],'--',color='purple',label='theory_shear_noh')
#ax[0,1].plot(f4.binning.binar['ls'][tbin4],f4.mean.vector[tbin4],':',color='purple',label='theory_noshear_noh')
ax[1,0].set_title('2,2')
##ax[1,0].errorbar(binning_array, mll1*mean_array_22, yerr=std_22, fmt='-',color='b', label='shear') 
##ax[1,0].errorbar(binning_array, mll1*mean_half_22, yerr=std_half_22, fmt='-',color='orange', label='4*half_bz')
ax[1,0].errorbar(binning_array, mll1*mean_noshear_half_22, yerr=std_noshear_half_22, fmt='-',color='g', label='4*half_bz,no_shear')
ax[1,0].errorbar(binning_array_2, mll2*mean_noshear_array_22, yerr=mll2*std_noshear_22,fmt='-', color='r', label='no_shear')
tbin=np.logical_and(f.binning.binar['T1']==2,f.binning.binar['T2']==2)
tbin2=np.logical_and(f2.binning.binar['T1']==2,f2.binning.binar['T2']==2)
l=f.binning.binar['ls'][tbin]
l2=f2.binning.binar['ls'][tbin2]
#tbin3=np.logical_and(f3.binning.binar['T1']==2,f3.binning.binar['T2']==2)
#tbin4=np.logical_and(f4.binning.binar['T1']==2,f4.binning.binar['T2']==2)
#tbin5=np.logical_and(f5.binning.binar['T1']==2,f5.binning.binar['T2']==2)
#ax[1,0].plot(f5.binning.binar['ls'][tbin5],f5.mean.vector[tbin5],'-.',color='r',label='theory_5')
##ax[1,0].plot(f.binning.binar['ls'][tbin], l*(l+1)*f.mean.vector[tbin],'--',color='black',label='theory_shear_h')
ax[1,0].plot(f2.binning.binar['ls'][tbin2],l2*(l2+1)*f2.mean.vector[tbin2],':',color='black',label='theory_noshear_h')
#ax[1,0].plot(f3.binning.binar['ls'][tbin3],f3.mean.vector[tbin3],'--',color='purple',label='theory_shear_noh')
#ax[1,0].plot(f4.binning.binar['ls'][tbin4],f4.mean.vector[tbin4],':',color='purple',label='theory_noshear_noh')
ax[1,1].set_title('3,3')
##ax[1,1].errorbar(binning_array, mll1*mean_array_33, yerr=std_33, fmt='-',color='b', label='shear')
##ax[1,1].errorbar(binning_array, mll1*mean_half_33, yerr=std_half_33, fmt='-',color='orange', label='4*half_bz')
ax[1,1].errorbar(binning_array, mll1*mean_noshear_half_33, yerr=std_noshear_half_33, fmt='-',color='g', label='4*half_bz,no_shear')
ax[1,1].errorbar(binning_array_2, mll2*mean_noshear_array_33, yerr=mll2*std_noshear_33,fmt='-', color='r', label='no_shear')
tbin=np.logical_and(f.binning.binar['T1']==3,f.binning.binar['T2']==3)
tbin2=np.logical_and(f2.binning.binar['T1']==3,f2.binning.binar['T2']==3)
l=f.binning.binar['ls'][tbin]
l2=f2.binning.binar['ls'][tbin2]
#tbin3=np.logical_and(f2.binning.binar['T1']==3,f2.binning.binar['T2']==3)
#tbin4=np.logical_and(f4.binning.binar['T1']==3,f4.binning.binar['T2']==3)
#tbin5=np.logical_and(f5.binning.binar['T1']==3,f5.binning.binar['T2']==3)
#ax[1,1].plot(f5.binning.binar['ls'][tbin5],f5.mean.vector[tbin5],'-.',color='r',label='theory_5')
##ax[1,1].plot(f.binning.binar['ls'][tbin],l*(l+1)*f.mean.vector[tbin],'--',color='black',label='theory_shear_h')
ax[1,1].plot(f2.binning.binar['ls'][tbin2],l2*(l2+1)*f2.mean.vector[tbin2],':',color='black',label='theory_noshear_h')
#ax[1,1].plot(f3.binning.binar['ls'][tbin3],f3.mean.vector[tbin3],'--',color='purple',label='theory_shear_noh')
#ax[1,1].plot(f4.binning.binar['ls'][tbin4],f4.mean.vector[tbin4],':',color='purple',label='theory_noshear_noh')
ax[0,0].set_xscale('log')
#ax[0,0].set_yscale('log')
ax[0,0].set_ylim(0.,0.2)
ax[0,0].set_xlim(10,1000)
ax[0,0].legend(loc='best')
ax[0,0].set_xlabel(r'$l$')
ax[0,0].set_ylabel(r'$l*(l+1)C_{l}$')
ax[0,1].set_xscale('log')
#ax[0,1].set_yscale('log')
ax[0,1].set_ylim(0.,0.1)
ax[0,1].set_xlim(10,1000)
ax[0,1].legend(loc='best')
ax[0,1].set_xlabel(r'$l$')
ax[0,1].set_ylabel(r'$l(l+1)C_{l}$')
ax[1,0].set_xscale('log')
#ax[1,0].set_yscale('log')
ax[1,0].set_ylim(0,0.1)
ax[1,0].set_xlim(10,1000)
ax[1,0].legend(loc='best')
ax[1,0].set_xlabel(r'$l$')
ax[1,0].set_ylabel(r'$l(l+1)C_{l}$')
ax[1,1].set_xscale('log')
#ax[1,1].set_yscale('log')
ax[1,1].set_ylim(0,0.1)
ax[1,1].set_xlim(10,1000)
ax[1,1].legend(loc='best')
ax[1,1].set_xlabel(r'$l$')
ax[1,1].set_ylabel(r'$l(l+1)C_{l}$')
plt.suptitle(title)
fig.savefig(output_name_separate)



##chi2_0=np.power(np.subtract(mean_array_00,theory_0),2)/np.power(std_00,2)
##chi2_1=np.power(np.subtract(mean_array_11,theory_1),2)/np.power(std_11,2)
##chi2_2=np.power(np.subtract(mean_array_22,theory_2),2)/np.power(std_22,2)
##chi2_3=np.power(np.subtract(mean_array_33,theory_3),2)/np.power(std_33,2)
##chi2_4=np.power(np.subtract(mean_array_44,theory_4),2)/np.power(std_44,2)

##plt.figure()
##plt.plot(binning_array,chi2_0, '-o', color='b', label='0,0')
##plt.plot(binning_array,chi2_1, '-o', color='g', label='1,1')
##plt.plot(binning_array,chi2_2, '-o', color='r', label='2,2')
##plt.plot(binning_array,chi2_3, '-o', color='cyan', label='3,3')
##plt.plot(binning_array,chi2_4, '-o', color='purple', label='4,4')
##plt.xscale('log')
##plt.yscale('log')
##plt.legend(loc='best')
##plt.xlabel(r'$l$')
##plt.ylabel(r'$Chi^{2}$')
##plt.savefig(output_chi_name)
#ss=sacc.SACC.loadFromHDF(filename=mean_filename)
#ss.err_plot_vector(out_name='/global/cscratch1/sd/kakoon/sacc/'+'mean_10_runs_2.png')
