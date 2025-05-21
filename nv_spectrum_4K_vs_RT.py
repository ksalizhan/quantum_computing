import pandas as pd
import matplotlib.pyplot as plt

# Load both CSV files
room_temp = pd.read_csv('sglue_RT2.csv', header=None)
cold_temp = pd.read_csv('sglue4K2.csv', header=None)

# Name the columns
room_temp.columns = ['Wavelength (nm)', 'Intensity_RT']
cold_temp.columns = ['Wavelength (nm)', 'Intensity_4K']

# Convert to numeric and drop bad rows
room_temp['Wavelength (nm)'] = pd.to_numeric(room_temp['Wavelength (nm)'], errors='coerce')
room_temp['Intensity_RT'] = pd.to_numeric(room_temp['Intensity_RT'], errors='coerce')
cold_temp['Wavelength (nm)'] = pd.to_numeric(cold_temp['Wavelength (nm)'], errors='coerce')
cold_temp['Intensity_4K'] = pd.to_numeric(cold_temp['Intensity_4K'], errors='coerce')

room_temp.dropna(inplace=True)
cold_temp.dropna(inplace=True)

# Plot both
plt.figure(figsize=(10, 6))
plt.plot(room_temp['Wavelength (nm)'], room_temp['Intensity_RT'], label='NV at Room Temperature', color='red', alpha=0.7)
plt.plot(cold_temp['Wavelength (nm)'], cold_temp['Intensity_4K'], label='NV spectrum at 4K', color='blue', alpha=0.7)

plt.title("Spectrum Comparison: Room Temp vs 4K (R2:C4 NV)", fontsize=16)
plt.xlabel("Wavelength (nm)", fontsize=14)
plt.ylabel("Photon Counts / Intensity", fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
