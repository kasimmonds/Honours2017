# -*- coding: utf-8 -*-


#import neccessary modules
from netCDF4 import Dataset
import numpy as np
import  matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid
import matplotlib.colors as colors

#ERA/AWAP COMPARISON FOR TNN SON K=9
#era dataset
nce = Dataset('/srv/ccrc/data06/z5147939/ncfiles/clust_3m/tnn_SON_2013_K_8_sil_0.1.nc', mode='r')
sil = nce.variables['sil_width'][:,:]
clust = nce.variables['cluster'][:,:]
lon = nce.variables['longitude'][:]
lat = nce.variables['latitude'][:]
mlon = nce.variables['medoid_lon'][:]
mlat = nce.variables['medoid_lat'][:]

#seperate each cluster to determine mean silhouette coefficient
c1 = np.where(clust == 1)
c2 = np.where(clust == 2)
c3 = np.where(clust == 3)
c4 = np.where(clust == 4)
c5 = np.where(clust == 5)
c6 = np.where(clust == 6)
c7 = np.where(clust == 7)
c8 = np.where(clust == 8)


#for each cluster assign mean sil co value
s_clust = np.zeros((clust.shape))
for i in range(0,len(lat)):
  for j in range(0,len(lon)):
    if clust[i,j] == 1:
      s_clust[i,j] = np.mean(sil[c1])
    if clust[i,j] == 2:
      s_clust[i,j] = np.mean(sil[c2])
    if clust[i,j] == 3:
      s_clust[i,j] = np.mean(sil[c3])
    if clust[i,j] == 4:
      s_clust[i,j] = np.mean(sil[c4])
    if clust[i,j] == 5:
      s_clust[i,j] = np.mean(sil[c5])
    if clust[i,j] == 6:
      s_clust[i,j] = np.mean(sil[c6])
    if clust[i,j] == 7:
      s_clust[i,j] = np.mean(sil[c7])
    if clust[i,j] == 8:
      s_clust[i,j] = np.mean(sil[c8])
    if s_clust[i,j] == 0:
      s_clust[i,j] = np.NaN

##print 'The ERA max is %s and min is %s' % (np.nanmax(s_clust), np.nanmin(s_clust))
#print 'cluster 0 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c1]), mlat[0], mlon[0])
#print 'cluster 1 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c2]), mlat[1], mlon[1])
#print 'cluster 2 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c3]), mlat[2], mlon[2])
##print 'cluster 3 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c4]), mlat[3], mlon[3])
#print 'cluster 4 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c5]), mlat[4], mlon[4])
##print 'cluster 5 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c6]), mlat[5], mlon[5])
#print 'cluster 6 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c7]), mlat[6], mlon[6])
#print 'cluster 7 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c8]), mlat[7], mlon[7])
#print 'cluster 8 mean = %s, lat = %s, lon = %s' % (np.mean(sil[c9]), mlat[8], mlon[8])


#make groups for clusters lat/lons
#lons
lon_c1 = []
lon_c2 = []
lon_c3 = []
lon_c4 = []
lon_c5 = []
lon_c6 = []
lon_c7 = []
lon_c8 = []


#lats
lat_c1 = []
lat_c2 = []
lat_c3 = []
lat_c4 = []
lat_c5 = []
lat_c6 = []
lat_c7 = []
lat_c8 = []


for i in range(0,len(lat)):
  for j in range(0,len(lon)):
    if clust[i,j] == 1 and sil[i,j] > 0.1:
      lon_c1.append(lon[j])
      lat_c1.append(lat[i])
    if clust[i,j] == 2 and sil[i,j] > 0.1:
      lon_c2.append(lon[j])
      lat_c2.append(lat[i])
    if clust[i,j] == 3 and sil[i,j] > 0.1:
      lon_c3.append(lon[j])
      lat_c3.append(lat[i])
    if clust[i,j] == 4 and sil[i,j] > 0.1:
      lon_c4.append(lon[j])
      lat_c4.append(lat[i])
    if clust[i,j] == 5 and sil[i,j] > 0.1:
      lon_c5.append(lon[j])
      lat_c5.append(lat[i])
    if clust[i,j] == 6 and sil[i,j] > 0.1:
      lon_c6.append(lon[j])
      lat_c6.append(lat[i])
    if clust[i,j] == 7 and sil[i,j] > 0.1:
      lon_c7.append(lon[j])
      lat_c7.append(lat[i])
    if clust[i,j] == 8 and sil[i,j] > 0.1:
      lon_c8.append(lon[j])
      lat_c8.append(lat[i])



#awap k=9 data
nca = Dataset('/srv/ccrc/data06/z5147939/ncfiles/clust_3m/tnn_ap_SON_2013_K_8_sil_0.1.nc', mode='r')
sila = nca.variables['sil_width'][:,:]
clusta = nca.variables['cluster'][:,:]
mlona = nca.variables['medoid_lon'][:]
mlata = nca.variables['medoid_lat'][:]

#global definitions
lons, lats = np.meshgrid(lon,lat)
v = np.linspace( 0, 0.28, 29, endpoint=True)
norm = colors.BoundaryNorm(boundaries=v, ncolors=256)

#plot figure(s)
fig = plt.figure(figsize=(17,4))
ax = plt.subplot(131)
m = Basemap(projection='cyl', llcrnrlat=-45.0, llcrnrlon=110.0, urcrnrlat=-5.0, urcrnrlon=160.0) #define basemap as around Australia
m.drawcoastlines()
m.drawparallels(np.array([-45, -35, -25, -15, -5]), labels=[1,0,0,0], fontsize=8)
m.drawmeridians(np.array([110, 120, 130, 140, 150, 160]), labels=[0,0,0,1], fontsize=8)
xi, yi = m(lons,lats)
mmlon, mmlat = m(mlon,mlat)
jet = plt.cm.get_cmap('jet')

m.plot(mlon[0],mlat[0], marker='D', color='r')
ax.annotate('1.', xy = (mlon[0],mlat[0]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[0],mlata[0], marker='o', color='r')

m.plot(mlon[1],mlat[1], marker='D', color='b')
ax.annotate('8.', xy = (mlon[1],mlat[1]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[1],mlata[1], marker='o', color='b')

m.plot(mlon[2],mlat[2], marker='D', color='g')
ax.annotate('5.', xy = (mlon[2],mlat[2]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[3],mlata[3], marker='o', color='g')

m.plot(mlon[3],mlat[3], marker='D', color='w', label='ERA-Interim')
ax.annotate('3.', xy = (mlon[3],mlat[3]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[2],mlata[2], marker='o', color='w', label='AWAP')

m.plot(mlon[4],mlat[4], marker='D', color='c')
ax.annotate('6.', xy = (mlon[4],mlat[4]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[4],mlata[4], marker='o', color='c')

m.plot(mlon[5],mlat[5], marker='D', color='m')
ax.annotate('2.', xy = (mlon[5],mlat[5]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[6],mlata[6], marker='o', color='m')

m.plot(mlon[6],mlat[6], marker='D', color='y')
ax.annotate('4.', xy = (mlon[6],mlat[6]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[5],mlata[5], marker='o', color='y')

m.plot(mlon[7],mlat[7], 'kD')
ax.annotate('7.', xy = (mlon[7],mlat[7]), xytext=(5, 5), textcoords='offset points')
m.plot(mlona[7],mlata[7],'ko')



plt.legend(numpoints=1, prop={'size':10})
plt.title('a) Medoid Positions for ERA-Interim and AWAP', fontsize=12)


ax = plt.subplot(132)
m = Basemap(projection='cyl', llcrnrlat=-45.0, llcrnrlon=110.0, urcrnrlat=-5.0, urcrnrlon=160.0) #define basemap as around Australia
m.drawcoastlines()
m.drawparallels(np.array([-45, -35, -25, -15, -5]), labels=[1,0,0,0], fontsize=8)
m.drawmeridians(np.array([110, 120, 130, 140, 150, 160]), labels=[0,0,0,1], fontsize=8)
xi, yi = m(lons,lats)
mmlon, mmlat = m(mlon,mlat)
jet = plt.cm.get_cmap('jet')

#large markers for significant values, small markers for insignificant
min_marker_size = 3
msize = np.zeros((sil.shape))
for i in range(0,len(lat)):
  for j in range(0,len(lon)):
    if sil[i,j] > 0.1:
      msize[i,j] = 3 * min_marker_size
    else:
      msize[i,j] =  min_marker_size

#plot lines between significant values and medoids
for i in range(0,len(lon_c1)):
  m.plot([mlon[0],lon_c1[i]],[mlat[0],lat_c1[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c2)):
  m.plot([mlon[1],lon_c2[i]],[mlat[1],lat_c2[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c3)):
  m.plot([mlon[2],lon_c3[i]],[mlat[2],lat_c3[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c4)):
  m.plot([mlon[3],lon_c4[i]],[mlat[3],lat_c4[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c5)):
  m.plot([mlon[4],lon_c5[i]],[mlat[4],lat_c5[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c6)):
  m.plot([mlon[5],lon_c6[i]],[mlat[5],lat_c6[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c7)):
  m.plot([mlon[6],lon_c7[i]],[mlat[6],lat_c7[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c8)):
  m.plot([mlon[7],lon_c8[i]],[mlat[7],lat_c8[i]], color='0.8', linewidth=0.75, zorder=1)


mymap= m.scatter(xi, yi, s=msize, c=s_clust, norm=norm, cmap=jet, edgecolors='none', zorder=2)
medoid = m.plot(mmlon, mmlat, 'D', color='k', fillstyle='none', mew=1.5, markersize=3)
plt.title('b) ERA-Interim SON TNn, K=8', fontsize=12)
#cb.set_label('Cluster mean silhouette coefficent', fontsize=10)


#awap k=9 data
#seperate each cluster to determine mean silhouette coefficient
c1a = np.where(clusta == 1)
c2a = np.where(clusta == 2)
c3a = np.where(clusta == 3)
c4a = np.where(clusta == 4)
c5a = np.where(clusta == 5)
c6a = np.where(clusta == 6)
c7a = np.where(clusta == 7)
c8a = np.where(clusta == 8)



#for each cluster assign mean sil co value
s_clusta = np.zeros((clusta.shape))
for i in range(0,len(lat)):
  for j in range(0,len(lon)):
    if clusta[i,j] == 1:
      s_clusta[i,j] = np.mean(sila[c1a])
    if clusta[i,j] == 2:
      s_clusta[i,j] = np.mean(sila[c2a])
    if clusta[i,j] == 3:
      s_clusta[i,j] = np.mean(sila[c3a])
    if clusta[i,j] == 4:
      s_clusta[i,j] = np.mean(sila[c4a])
    if clusta[i,j] == 5:
      s_clusta[i,j] = np.mean(sila[c5a])
    if clusta[i,j] == 6:
      s_clusta[i,j] = np.mean(sila[c6a])
    if clusta[i,j] == 7:
      s_clusta[i,j] = np.mean(sila[c7a])
    if clusta[i,j] == 8:
      s_clusta[i,j] = np.mean(sila[c8a])
    if s_clusta[i,j] == 0:
      s_clusta[i,j] = np.NaN


#print 'The AWAP max is %s and min is %s' % (np.nanmax(s_clusta), np.nanmin(s_clusta))

#make groups for clusters lat/lons
#lons
lon_c1a = []
lon_c2a = []
lon_c3a = []
lon_c4a = []
lon_c5a = []
lon_c6a = []
lon_c7a = []
lon_c8a = []


#lats
lat_c1a = []
lat_c2a = []
lat_c3a = []
lat_c4a = []
lat_c5a = []
lat_c6a = []
lat_c7a = []
lat_c8a = []


for i in range(0,len(lat)):
  for j in range(0,len(lon)):
    if clusta[i,j] == 1 and sila[i,j] > 0.1:
      lon_c1a.append(lon[j])
      lat_c1a.append(lat[i])
    if clusta[i,j] == 2 and sila[i,j] > 0.1:
      lon_c2a.append(lon[j])
      lat_c2a.append(lat[i])
    if clusta[i,j] == 3 and sila[i,j] > 0.1:
      lon_c3a.append(lon[j])
      lat_c3a.append(lat[i])
    if clusta[i,j] == 4 and sila[i,j] > 0.1:
      lon_c4a.append(lon[j])
      lat_c4a.append(lat[i])
    if clusta[i,j] == 5 and sila[i,j] > 0.1:
      lon_c5a.append(lon[j])
      lat_c5a.append(lat[i])
    if clusta[i,j] == 6 and sila[i,j] > 0.1:
      lon_c6a.append(lon[j])
      lat_c6a.append(lat[i])
    if clusta[i,j] == 7 and sila[i,j] > 0.1:
      lon_c7a.append(lon[j])
      lat_c7a.append(lat[i])
    if clusta[i,j] == 8 and sila[i,j] > 0.1:
      lon_c8a.append(lon[j])
      lat_c8a.append(lat[i])


#plot figure
ax = plt.subplot(133)
m = Basemap(projection='cyl', llcrnrlat=-45.0, llcrnrlon=110.0, urcrnrlat=-5.0, urcrnrlon=160.0) #define basemap as around Australia
m.drawcoastlines()
m.drawparallels(np.array([-45, -35, -25, -15, -5]), labels=[1,0,0,0], fontsize=8)
m.drawmeridians(np.array([110, 120, 130, 140, 150, 160]), labels=[0,0,0,1], fontsize=8)
xi, yi = m(lons,lats)
mmlona, mmlata = m(mlona,mlata)

#large markers for significant values, small markers for insignificant
min_marker_size = 3
msizea = np.zeros((sila.shape))
for i in range(0,len(lat)):
  for j in range(0,len(lon)):
    if sila[i,j] > 0.1:
      msizea[i,j] = 3 * min_marker_size
    else:
      msizea[i,j] =  min_marker_size

#plot lines between significant values and medoids
for i in range(0,len(lon_c1a)):
  m.plot([mlona[0],lon_c1a[i]],[mlata[0],lat_c1a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c2a)):
  m.plot([mlona[1],lon_c2a[i]],[mlata[1],lat_c2a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c3a)):
  m.plot([mlona[2],lon_c3a[i]],[mlata[2],lat_c3a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c4a)):
  m.plot([mlona[3],lon_c4a[i]],[mlata[3],lat_c4a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c5a)):
  m.plot([mlona[4],lon_c5a[i]],[mlata[4],lat_c5a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c6a)):
  m.plot([mlona[5],lon_c6a[i]],[mlata[5],lat_c6a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c7a)):
  m.plot([mlona[6],lon_c7a[i]],[mlata[6],lat_c7a[i]], color='0.8', linewidth=0.75, zorder=1)

for i in range(0,len(lon_c8a)):
  m.plot([mlona[7],lon_c8a[i]],[mlata[7],lat_c8a[i]], color='0.8', linewidth=0.75, zorder=1)



mymap= m.scatter(xi, yi, s=msizea, c=s_clusta, norm=norm, cmap=jet, edgecolors='none', zorder=2)
medoid = m.plot(mmlona, mmlata, 'D', color='k', fillstyle='none', mew=1.5, markersize=3)
plt.title('c) AWAP SON TNn, K=8', fontsize=12)
cax = fig.add_axes([0.92, 0.1, 0.015, 0.8])
cb = fig.colorbar(mymap, cax, orientation='vertical')
cb.ax.tick_params(labelsize=8)
cb.set_label('Cluster strength', fontsize=10)
plt.savefig('/home/z5147939/hdrive/figs/tnn_son_8clust.png', bbox_inches='tight')
plt.show()
