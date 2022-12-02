import numpy as np
import matplotlib.pyplot as plt
import astropy as astro
import pandas as pd
import math

#import data from file
with open('iso_timeseries.list','rt') as filedata:
    values = np.loadtxt('APER_timeseries.list', dtype=float)

time =  values[:,0]

exo_flux = values[:,1]
exoflux_error = values[:,2]

ref1_flux = values[:,11]
ref1_flux_err = values[:,12]

#get weighted mean for each frame for calibration sources.
def mean_weighted(row):
    fluxes = row[7::2]
    errors = row[8::2]
    avg = np.average(fluxes,weights=errors)
    return avg

avg_flux=[]

for i in range(len(time)):
    frame_vals = values[i,:]
    avg_flux.append(mean_weighted(frame_vals))
#print(avg_flux)

#scaling factors
scale_fact=[]
for i in avg_flux:
    x = avg_flux[0]/i
    scale_fact.append(x)

#print(scale_fact)

scaled_exoflux = exo_flux*scale_fact
#print(scaled_exoflux)
def plot_scatter(yval,error):
    (fig1,ax1)= plt.subplots()
    ax1.errorbar(time,yval,yerr=error,fmt='o',markersize=2)
    #ax1.set_yscale('log')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Flux')
    plt.show()

#plot_scatter(ref1_flux*scale_fact,ref1_flux_err*scale_fact)
#plot_scatter(scaled_exoflux,exoflux_error*scale_fact)

'''
plot_scatter(values[:,3],values[:,4])
plot_scatter(values[:,5],values[:,6])
plot_scatter(values[:,9],values[:,10])
plot_scatter(values[:,11],values[:,12])
plot_scatter(values[:,13],values[:,14])
plot_scatter(values[:,15],values[:,16])
plot_scatter(values[:,17],values[:,18])
plot_scatter(values[:,19],values[:,20])
plot_scatter(values[:,21],values[:,22]) #
'''

min_mean = np.mean(scaled_exoflux[0:30])
max_mean = np.mean(scaled_exoflux[69:101])
#print(min_mean)
#print(max_mean)

mag_dif = -2.5 * math.log10(min_mean/max_mean)
#print(mag_dif)

radius_ratio = ((max_mean-min_mean)/max_mean)*0.5
print(radius_ratio)

print('test!')