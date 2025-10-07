from scipy.interpolate import CubicSpline
import numpy as np
#import matplotlib.pyplot as plt


class Goggle():

    min_wavelength: float
    max_wavelength: float
    wavelength: np.ndarray
    optical_density: np.ndarray

    interpolator: CubicSpline

    def __init__(self):
        pass

    def load_data(self, data_file: str):

        goggle_data = np.loadtxt(data_file, delimiter=",", skiprows=1)
        self.wavelength = goggle_data[:, 0]
        self.optical_density = goggle_data[:, 1]

        self.min_wavelength = np.min(self.wavelength)
        self.max_wavelength = np.max(self.wavelength)

        self.interpolator = CubicSpline(self.wavelength, self.optical_density, extrapolate = False)

    def evaluate_OD(self, wavelength):
        return self.interpolator(wavelength)

    def attenuate(self, wavelength, intensities):
        attenuated_intensities = np.copy(intensities)
        valid_indices = self.valid_indices(wavelength)
        ODs = self.evaluate_OD(wavelength[valid_indices])
        attenuated_intensities[valid_indices] = np.divide(attenuated_intensities[valid_indices], np.power(10, ODs))
        return attenuated_intensities

    def valid_indices(self, wavelengths):
        return np.argwhere((wavelengths > self.min_wavelength) & (wavelengths < self.max_wavelength))


class C1033(Goggle):

    def __init__(self):

        data_file = 'laser_goggles/data/C1033.csv'
        self.load_data(data_file)

class C1023(Goggle):
    def __init__(self):
        data_file = "laser_goggles/data/C1023.csv"
        self.load_data(data_file)

class T5H03(Goggle):
    def __init__(self):
        data_file = 'laser_goggles/data/T5H03.csv'
        self.load_data(data_file)

class T5H05(Goggle):
    def __init__(self):
        data_file = 'laser_goggles/data/T5H05.csv'
        self.load_data(data_file)


