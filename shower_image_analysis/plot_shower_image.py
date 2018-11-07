import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.colors import LogNorm
from itertools import chain

#df = pd.read_pickle('/Users/whitbeck/LDMXanalysis/samples/shower_image/4pt0_gev_electron_gun_image_tree.pkl')
df = pd.read_pickle('/Users/whitbeck/LDMXanalysis/samples/shower_image/4pt0_gev_muon_gun_image_tree.pkl')
df['hit_rho'] = map(lambda x , y : np.sqrt(x*x+y*y),df['hit_posx'],df['hit_posy'])

#unroll 2D array into 1D array
rho = list(chain.from_iterable(df['hit_rho']))
posx = list(chain.from_iterable(df['hit_posx']))
posy = list(chain.from_iterable(df['hit_posy']))
posz = list(chain.from_iterable(df['hit_posz']))
energy = list(chain.from_iterable(df['hit_energy']))

#print zip(rho,posx,posy,posz)[:10]
print posz[:100]

i=10
binning = plt.hist2d(df['hit_posx'][i],df['hit_posy'][i],bins=[np.arange(-50,50,5),np.arange(-50,50,5)],weights=df['hit_energy'][i],norm=LogNorm())
plt.colorbar()
plt.draw()
plt.savefig('energy_x_vs_y_image.pdf',dpi=200)

plt.clf()
binning = plt.hist2d(df['hit_posz'][i],df['hit_rho'][i],bins=200,weights=df['hit_energy'][i],norm=LogNorm())
#binning = plt.hist2d(posx,posy,bins=200,weights=energy,norm=LogNorm())
#binning = plt.hist2d(posz,rho,bins=[np.arange(0,30,1),np.arange(0,50,5)],weights=energy)
#print binning
plt.draw()
plt.savefig('energy_r_vs_z_image.pdf',dpi=200)
