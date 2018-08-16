import sacc_2 as sacc
import datetime
import numpy as np
import sys


#if len(sys.argv)==1:
#    filename=raw_input('Enter a filename: ')
#else:
#    filename=sys.argv[1]
mean_filename='/global/cscratch1/sd/kakoon/sacc/mean_10_runs.txt'
for i in range(11,20):

    input_str='%i'%i
    filename='/global/cscratch1/sd/kakoon/namaster_output/cat_%i_3072_082417.sacc'%i
    print "reading :" + filename
    t=datetime.datetime.now()
    daystr="%02i%02i%02i"%(t.year-2000, t.month, t.day)
    output_file='/global/cscratch1/sd/kakoon/sacc/'+daystr+"_"+input_str+"_"+"output.png"

    s=sacc.SACC.loadFromHDF(filename)
    s.printInfo()
    s.plot_vector(out_name=output_file, mean_file=mean_filename)
    #s.saveToHDF(mean_filename, mean_filename=mean_filename)
    
theory='/global/cscratch1/sd/kakoon/2pt_validation/namaster_fastcat/theory.sacc'
ss=sacc.SACC.loadFromHDF(filename=mean_filename)
tf=sacc.SACC.loadFromHDF(filename=theory)
ss.err_plot_vector(theory_file=tf,out_name='/global/cscratch1/sd/kakoon/sacc/'+'mean_10_runs.png')

