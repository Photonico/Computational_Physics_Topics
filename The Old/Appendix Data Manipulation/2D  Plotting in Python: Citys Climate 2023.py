# 2D  Plotting in Python: Citys Climate 2023

# Including temperature statistics in °C and precipitation in millimeter

import numpy as np

# Months
mo = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# Beijing
Beijing_temp_max        = np.array([ -1.1,  2.3,  9.1, 18.4, 25.0, 30.1, 31.9, 30.8, 26.2, 18.5,  8.3,  0.5])
Beijing_temp_min        = np.array([-10.0, -7.7, -1.6,  6.4, 13.8, 19.3, 23.1, 22.3, 15.5,  6.9, -2.2, -8.2])
Beijing_temp_ave        = np.array([ -5.5, -2.8,  3.7, 12.4, 19.4, 24.7, 27.4, 26.5, 20.6, 12.7,  3.1, -3.9])
Beijing_precipitation   = np.array([  3.0,  4.0,  8.0, 25.0, 44.0, 78.0,185.0,165.0, 37.0, 12.0,  3.0,  2.0])

# Shanghai
Shanghai_temp_max       = np.array([  8.3,  9.2, 12.8, 18.1, 23.0, 27.1, 31.1, 31.3, 27.4, 22.8, 17.6, 12.5])
Shanghai_temp_min       = np.array([  0.5,  1.5,  5.3, 10.7, 15.8, 20.2, 24.1, 23.9, 19.4, 14.2,  8.7,  3.7])
Shanghai_temp_ave       = np.array([  4.3,  5.3,  9.0, 14.4, 19.4, 23.6, 27.6, 27.5, 23.4, 18.5, 13.1,  8.1])
Shanghai_precipitation  = np.array([ 53.0, 59.0, 94.0, 87.0, 89.0,152.0,221.0,157.0,121.0, 63.0, 46.0, 43.0])

# Sydney
Sydney_temp_max         = np.array([ 26.6, 26.5, 25.1, 22.6, 19.2, 16.4, 15.6, 17.1, 19.2, 21.5, 23.2, 25.2])
Sydney_temp_min         = np.array([ 19.5, 19.7, 18.8, 15.6, 12.2,  9.4,  8.5,  9.4, 11.3, 13.6, 16.2, 18.5])
Sydney_temp_ave         = np.array([ 23.0, 23.1, 22.0, 19.1, 15.7, 12.9, 12.0, 13.3, 15.3, 17.5, 19.7, 21.8])
Sydney_precipitation    = np.array([102.0,126.0,122.0,131.0,120.0,128.0, 83.0, 81.0, 71.0, 74.0, 85.0, 90.0])

# Calgary
Calgary_temp_max        = np.array([ -0.6,  1.2,  5.6, 11.9, 17.4, 21.4, 23.9, 23.0, 18.0, 11.9,  3.5, -2.5])
Calgary_temp_min        = np.array([-13.7,-12.7, -7.8, -1.3,  3.8,  8.1,  9.7,  8.9,  4.7, -0.5, -8.0,-14.1])
Calgary_temp_ave        = np.array([ -7.2, -5.8, -1.1,  5.3, 10.6, 14.8, 16.8, 15.9, 11.4,  5.7, -2.3, -8.3])
Calgary_precipitation   = np.array([ 11.4, 10.5, 17.3, 31.6, 52.4, 77.7, 71.2, 57.0, 40.2, 23.6, 13.8, 12.3])

# Toronto
Toronto_temp_max        = np.array([ -1.0, -0.4,  4.1, 11.0, 18.3, 23.0, 26.0, 25.1, 21.0, 14.2,  7.4,  0.6])
Toronto_temp_min        = np.array([ -7.3, -7.3, -3.8,  3.0,  9.4, 14.0, 17.0, 16.4, 12.7,  6.0, -0.3, -6.3])
Toronto_temp_ave        = np.array([ -3.8, -3.3,  0.4,  7.7, 14.1, 19.0, 21.9, 21.3, 17.5, 10.5,  3.5, -2.5])
Toronto_precipitation   = np.array([ 54.9, 49.0, 61.5, 69.6, 77.2, 71.1, 66.8, 78.3, 73.0, 73.8, 83.6, 63.2])

# LA
LA_temp_max         = np.array([ 20.0, 20.0, 21.1, 22.8, 23.9, 27.2, 29.4, 30.6, 29.4, 26.7, 22.8, 19.4])
LA_temp_min         = np.array([  9.0, 10.0, 11.1, 12.8, 14.4, 17.2, 18.9, 19.4, 17.8, 14.4, 10.6,  8.9])
LA_temp_ave         = np.array([ 14.4, 15.0, 16.1, 17.8, 19.4, 22.2, 23.9, 25.0, 23.9, 20.9, 16.0, 12.7])
LA_precipitation    = np.array([ 79.0, 87.4, 61.7, 23.1,  6.6,  2.3,  0.3,  1.0,  4.8, 15.2, 47.8, 43.2])

import matplotlib; import matplotlib.pyplot as plt

plt.figure(dpi=192); params = {"text.usetex":True, "font.family":"serif", "mathtext.fontset":"cm", "axes.titlesize":16, "axes.labelsize":14, "figure.facecolor":"w"}
matplotlib.rcParams.update(params)
plt.tick_params(direction="in",top=True,right=True,bottom=True,left=True)
plt.title("Citys Climate"); plt.xlabel(r"Months"); plt.ylabel(r"Temperature in °C")

plt.fill_between(mo, Beijing_temp_max, Beijing_temp_min, alpha=0.12, linewidth=0, color="#FF281E")
plt.plot(mo, Beijing_temp_ave, color="#FF281E", label="Beijing")

plt.fill_between(mo, Shanghai_temp_max, Shanghai_temp_min, alpha=0.12, linewidth=0, color="#FA961E")
plt.plot(mo, Shanghai_temp_ave, color="#FA961E", label="Shanghai")

plt.fill_between(mo, Sydney_temp_max, Sydney_temp_min, alpha=0.12, linewidth=0, color="#78E132")
plt.plot(mo, Sydney_temp_ave, color="#78E132", label="Sydney")

plt.fill_between(mo, Toronto_temp_max, Toronto_temp_min, alpha=0.12, linewidth=0, color="#1EB4FF")
plt.plot(mo, Toronto_temp_ave, color="#1EB4FF", label="Toronto")

plt.fill_between(mo, Calgary_temp_max, Calgary_temp_min, alpha=0.12, linewidth=0, color="#7864E1")
plt.plot(mo, Calgary_temp_ave, color="#7864E1", label="Calgary")

plt.fill_between(mo, LA_temp_max, LA_temp_min, alpha=0.12, linewidth=0, color="#D7A0FF")
plt.plot(mo, LA_temp_ave, color="#D7A0FF", label="LA")

plt.show()
