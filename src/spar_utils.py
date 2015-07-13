# -*- coding: utf-8 -*-
"""

"""
import numpy as np
from math import pi, cos, sqrt, radians, sin, exp, log10, log, floor, ceil
import algopy
import scipy as scp

def thrust_table(size_of_turbine,ADEN,RWA): 
    wind = np.array(range(0,26))
    if size_of_turbine == '3MW':
        Ct = np.array([0.001,0.001,0.001,0.001,0.868,0.869,0.879,0.869,0.868,0.868,0.778,0.675,0.542,0.393,0.305,0.244,0.199,0.166,0.141,0.120,0.104,0.091,0.080,0.072,0.064,0.058])
    elif size_of_turbine == '6MW':
        Ct = np.array([0.001,0.001,0.001,0.768,0.768,0.762,0.764,0.768,0.758,0.763,0.688,0.608,0.434,0.328,0.259,0.209,0.171,0.143,0.122,0.104,0.089,0.078,0.070,0.062,0.055,0.050])
    elif size_of_turbine == '10MW': 
        Ct = np.array([0.001,0.001,0.001,0.923,0.923,0.919,0.904,0.858,0.814,0.814,0.814,0.814,0.577,0.419,0.323,0.259,0.211,0.175,0.148,0.126,0.109,0.095,0.084,0.074,0.066,0.059])
    else: 
        print "examples are 3MW, 6MW, or 10MW"
    thrust = 0.5*ADEN*wind**2.*RWA*Ct/1000.
    return (wind,Ct,thrust)
    
def filtered_stiffeners_table():
    TABLE = np.zeros(125,dtype=[('name',np.str_, 16),('area','f8'),('d','f8'),('tw','f8'),('bf','f8'),('tf','f8'),('yna','f8'),('Ir','f8')])
    # name area(m^2) depth(m) web thickness(m) flange width(m) flange thickness(m) yna(m) Ir (m^4)
    TABLE [0] = ('ST1.5x3.75',1.1,1.5,0.349,2.51,0.26,1.068,0.2)
    TABLE [1] = ('ST1.5x2.85',0.83,1.5,0.17,2.33,0.26,1.171,0.114)
    TABLE [2] = ('ST2x4.75',1.39,2.,0.326,2.8,0.293,1.447,0.462)
    TABLE [3] = ('MT2x3',0.855,1.9,0.13,3.8,0.16,1.559,0.208)
    TABLE [4] = ('WT2x6.5',1.91,2.08,0.28,4.06,0.345,1.64,0.526)
    TABLE [5] = ('ST2.5x7.375',2.170,2.500,0.494,3.284,0.326,1.711,1.270)
    TABLE [6] = ('ST2.5x5',1.470,2.500,0.214,3.000,0.326,1.930,0.671)
    TABLE [7] = ('WT2.5x8',2.350,2.510,0.240,5.000,0.360,2.052,0.845)
    TABLE [8] = ('MT3x1.85',0.540,2.960,0.098,2.000,0.129,2.133,0.483)
    TABLE [9] = ('WT3x4.25',1.250,2.920,0.170,3.940,0.194,2.282,0.904)
    TABLE [10] = ('WT3x4.5',1.340,2.950,0.170,3.940,0.215,2.327,0.950)
    TABLE [11] = ('WT3x7.5',2.220,3.000,0.230,5.990,0.260,2.443,1.410)
    TABLE [12] = ('WT3x10',2.950,3.100,0.260,6.020,0.365,2.540,1.760)
    TABLE [13] = ('ST3.5x7.65',2.250,3.500,0.252,3.662,0.392,2.683,2.190)
    TABLE [14] = ('MT4x3.1',0.904,4.000,0.129,2.280,0.177,2.820,1.500)
    TABLE [15] = ('WT4x5',1.480,3.950,0.170,3.940,0.205,2.997,2.150)
    TABLE [16] = ('WT4x7.5',2.220,4.050,0.245,4.010,0.315,3.052,3.280)
    TABLE [17] = ('WT4x9',2.630,4.070,0.230,5.250,0.330,3.236,3.410)
    TABLE [18] = ('WT4x10.5',3.080,4.140,0.250,5.270,0.400,3.309,3.900)
    TABLE [19] = ('MT5x3.75',1.100,5.000,0.130,2.690,0.173,3.490,2.910)
    TABLE [20] = ('WT5x6',1.770,4.930,0.190,3.960,0.210,3.570,4.350)
    TABLE [21] = ('WT5x7.5',2.210,5.000,0.230,4.000,0.270,3.630,5.450)
    TABLE [22] = ('WT5x8.5',2.500,5.050,0.240,4.010,0.330,3.730,6.060)
    TABLE [23] = ('WT5x9.5',2.810,5.120,0.250,4.020,0.395,3.840,6.680)
    TABLE [24] = ('WT5x11',3.240,5.090,0.240,5.750,0.360,4.020,6.880)
    TABLE [25] = ('MT6x5',1.460,5.990,0.149,3.250,0.180,4.130,5.620)
    TABLE [26] = ('WT6x7',2.080,5.960,0.200,3.970,0.225,4.200,7.670)
    TABLE [27] = ('ST6x17.5',5.120,6.000,0.428,5.080,0.544,4.350,17.200)
    TABLE [28] = ('WT6x9.5',2.790,6.080,0.235,4.010,0.350,4.430,10.100)
    TABLE [29] = ('WT6x115',33.900,7.530,1.290,12.900,2.070,5.710,106.000)
    TABLE [30] = ('MT7x9',2.550,7.000,0.215,4.000,0.270,4.880,13.100)
    TABLE [31] = ('WT6x15',4.400,6.170,0.260,6.520,0.440,4.900,13.500)
    TABLE [32] = ('WT6x26.5',7.780,6.030,0.345,9.990,0.575,5.010,17.700)
    TABLE [33] = ('WT7x11',3.250,6.870,0.230,5.000,0.335,5.110,14.800)
    TABLE [34] = ('WT7x13',3.850,6.960,0.255,5.030,0.420,5.240,17.300)
    TABLE [35] = ('WT7x15',4.420,6.920,0.270,6.730,0.385,5.340,19.000)
    TABLE [36] = ('WT7x17',5.000,6.990,0.285,6.750,0.455,5.460,20.900)
    TABLE [37] = ('WT7x19',5.580,7.050,.310,6.770,0.515,5.510,23.300)
    TABLE [38] = ('WT6x105',30.900,7.360,1.180,12.800,1.900,5.640,92.100)
    TABLE [39] = ('WT8x13',3.840,7.850,0.250,5.500,0.345,5.760,23.500)
    TABLE [40] = ('WT6x139.5',41.000,7.930,1.530,13.100,2.470,5.880,141.000)
    TABLE [41] = ('WT8x15.5',4.560,7.940,0.275,5.530,0.440,5.920,27.500)
    TABLE [42] = ('WT8x18',5.290,7.930,0.295,6.990,0.430,6.050,30.600)
    TABLE [43] = ('WT7x72.5',21.300,7.390,0.680,15.500,1.090,6.100,62.500)
    TABLE [44] = ('WT8x20',5.890,8.010,0.305,7.000,0.505,6.200,33.100)
    TABLE [45] = ('WT7x116.5',34.200,8.020,1.070,15.900,1.720,6.370,116.000)
    TABLE [46] = ('WT9x17.5',5.150,8.850,0.300,6.000,0.425,6.460,40.100)
    TABLE [47] = ('WT7x141.5',41.600,8.370,1.290,16.100,2.070,6.510,153.000)
    TABLE [48] = ('WT9x20',5.880,8.950,0.315,6.020,0.525,6.660,44.800)
    TABLE [49] = ('WT9x23',6.770,9.030,0.360,6.060,0.605,6.700,52.100)
    TABLE [50] = ('WT9x25',7.330,8.990,0.355,7.500,0.570,6.870,53.500)
    TABLE [51] = ('WT9x27.5',8.100,9.060,0.390,7.530,0.630,6.900,59.500)
    TABLE [52] = ('ST10x48',14.100,10.200,0.800,7.200,0.920,7.070,143.000)
    TABLE [53] = ('ST10x33',9.690,10.000,0.505,6.260,0.795,7.190,92.900)
    TABLE [54] = ('ST10x43',12.700,10.200,0.660,7.060,0.920,7.290,124.000)
    TABLE [55] = ('WT10.5x22',6.490,10.300,0.350,6.500,0.450,7.320,71.100)
    TABLE [56] = ('WT10.5x25',7.360,10.400,0.380,6.530,0.535,7.470,80.300)
    TABLE [57] = ('WT10.5x24',7.070,10.300,0.350,8.140,0.430,7.560,74.900)
    TABLE [58] = ('WT10.5x28.5',8.370,10.500,0.405,6.560,0.650,7.650,90.400)
    TABLE [59] = ('WT10.5x27.5',8.100,10.400,0.375,8.220,0.522,7.760,84.400)
    TABLE [60] = ('WT9x96',28.200,10.175,0.960,11.455,1.750,7.835,202.000)
    TABLE [61] = ('WT10.5x31',9.130,10.500,0.400,8.240,0.615,7.920,93.800)
    TABLE [62] = ('WT10.5x34',10.000,10.600,0.430,8.270,0.685,8.010,103.000)
    TABLE [63] = ('ST12x50',14.700,12.000,0.745,7.250,0.870,8.160,215.000)
    TABLE [64] = ('WT12x27.5',8.150,11.800,0.395,7.010,0.505,8.320,117.000)
    TABLE [65] = ('WT12x31',9.160,11.900,0.430,7.040,0.590,8.450,132.000)
    TABLE [66] = ('WT10.5x50.5',14.900,10.700,0.500,12.300,0.800,8.520,135.000)
    TABLE [67] = ('ST12x60.5',17.800,12.300,0.800,8.050,1.090,8.670,259.000)
    TABLE [68] = ('ST12x40',11.700,12.000,0.500,7.000,0.870,8.700,162.000)
    TABLE [69] = ('WT12x34',10.000,11.900,0.415,8.970,0.585,8.840,137.000)
    TABLE [70] = ('WT10.5x91',26.800,11.400,0.830,12.500,1.480,8.920,253.000)
    TABLE [71] = ('WT12x38',11.200,12.000,0.440,8.990,0.680,9.000,151.000)
    TABLE [72] = ('WT12x42',12.400,12.100,0.470,9.020,0.770,9.130,166.000)
    TABLE [73] = ('WT12x47',13.800,12.200,0.515,9.070,0.875,9.210,186.000)
    TABLE [74] = ('WT12x52',15.300,12.000,0.500,12.800,0.750,9.410,189.000)
    TABLE [75] = ('WT12x65.5',19.300,12.200,0.605,12.900,0.960,9.550,238.000)
    TABLE [76] = ('WT12x73',21.500,12.400,0.650,12.900,1.090,9.740,264.000)
    TABLE [77] = ('WT12x81',23.900,12.500,0.705,13.000,1.220,9.800,293.000)
    TABLE [78] = ('WT13.5x42',12.400,13.400,0.460,9.960,0.640,9.920,216.000)
    TABLE [79] = ('WT13.5x47',13.800,13.500,0.490,9.990,0.745,10.090,239.000)
    TABLE [80] = ('WT13.5x51',15.000,13.500,0.515,10.000,0.830,10.130,258.000)
    TABLE [81] = ('WT13.5x64.5',18.900,13.800,0.610,10.000,1.100,10.410,323.000)
    TABLE [82] = ('WT15x45',13.200,14.800,0.470,10.400,0.610,10.760,290.000)
    TABLE [83] = ('WT15x54',15.900,14.900,0.545,10.500,0.760,10.890,349.000)
    TABLE [84] = ('WT15x58',17.100,15.000,0.565,10.500,0.850,11.060,373.000)
    TABLE [85] = ('WT13.5x108.5',32.000,14.200,0.830,14.100,1.500,11.100,502.000)
    TABLE [86] = ('WT15x62',18.200,15.100,0.585,10.500,0.930,11.200,396.000)
    TABLE [87] = ('WT15x66',19.400,15.200,0.615,10.500,1.000,11.300,421.000)
    TABLE [88] = ('WT15x74',21.700,15.300,0.650,10.500,1.180,11.460,466.000)
    TABLE [89] = ('WT15x86.5',25.500,15.200,0.655,15.000,1.070,11.890,497.000)
    TABLE [90] = ('WT16.5x59',17.300,16.400,0.550,11.500,0.740,11.930,469.000)
    TABLE [91] = ('WT16.5x65',19.200,16.500,0.580,11.500,0.855,12.140,513.000)
    TABLE [92] = ('WT15x117.5',34.600,15.700,0.830,15.100,1.500,12.290,674.000)
    TABLE [93] = ('WT16.5x70.5',20.800,16.700,0.605,11.500,0.960,12.410,552.000)
    TABLE [94] = ('WT16.5x84.5',24.800,16.900,0.670,11.500,1.220,12.690,649.000)
    TABLE [95] = ('WT18x67.5',19.900,17.800,0.600,12.000,0.790,12.840,637.000)
    TABLE [96] = ('WT16.5x100.5',29.600,16.800,0.715,15.700,1.150,13.030,725.000)
    TABLE [97] = ('WT18x75',22.100,17.900,0.625,12.000,0.940,13.120,698.000)
    TABLE [98] = ('WT18x80',23.500,18.000,0.650,12.000,1.020,13.260,740.000)
    TABLE [99] = ('WT18x85',25.000,18.100,0.680,12.000,1.100,13.370,786.000)
    TABLE [100] = ('WT18x91',26.800,18.200,0.725,12.100,1.180,13.430,845.000)
    TABLE [101] = ('WT16.5x159',46.800,17.600,1.040,16.000,1.890,13.580,1160.000)
    TABLE [102] = ('WT20x74.5',21.900,19.100,0.630,11.800,0.830,13.650,815.000)
    TABLE [103] = ('WT18x116',34.100,18.600,0.870,12.100,1.570,13.780,1080.000)
    TABLE [104] = ('WT18x115',33.800,18.000,0.760,16.500,1.260,13.990,934.000)
    TABLE [105] = ('WT18x130',38.200,18.100,0.840,16.600,1.440,14.050,1060.000)
    TABLE [106] = ('WT20x83.5',24.600,19.300,0.650,11.800,1.020,14.110,899.000)
    TABLE [107] = ('WT20x87',25.500,19.100,0.650,15.750,0.830,14.230,907.000)
    TABLE [108] = ('WT18x179.5',52.700,18.700,1.120,16.700,2.010,14.370,1500.000)
    TABLE [109] = ('WT18x196.5',57.800,18.900,1.220,16.800,2.200,14.460,1660.000)
    TABLE [110] = ('WT20x91.5',26.900,19.500,0.650,11.800,1.220,14.570,958.000)
    TABLE [111] = ('WT20x105.5',31.000,19.700,0.750,11.800,1.420,14.620,1120.000)
    TABLE [112] = ('WT20x163.5',48.000,20.400,1.180,12.100,2.130,14.740,1840.000)
    TABLE [113] = ('WT20x99.5',29.200,19.300,0.650,15.800,1.070,14.830,988.000)
    TABLE [114] = ('WT18x325',95.500,20.200,1.970,17.600,3.540,14.940,3030.000)
    TABLE [115] = ('WT20x233',68.400,21.220,1.670,12.640,2.950,15.000,2770.000)
    TABLE [116] = ('WT20x148.5',43.700,19.900,0.930,15.800,1.650,15.190,1500.000)
    TABLE [117] = ('WT20x107.5',31.700,19.500,0.650,15.800,1.220,15.220,1030.000)
    TABLE [118] = ('WT20x138.5',40.700,19.800,0.830,15.800,1.580,15.300,1360.000)
    TABLE [119] = ('WT20x198.5',58.400,20.500,1.220,16.100,2.200,15.470,2070.000)
    TABLE [120] = ('WT20x251.5',74.000,21.000,1.540,16.400,2.760,15.610,2730.000)
    TABLE [121] = ('WT20x296.5',87.200,21.500,1.790,16.700,3.230,15.840,3310.000)
    TABLE [122] = ('WT22x115',33.800,21.500,0.710,15.800,1.220,16.330,1440.000)
    TABLE [123] = ('WT22x167.5',49.100,22.000,1.020,16.000,1.770,16.490,2160.000)
    TABLE [124] = ('WT22x131',38.600,21.700,0.790,15.800,1.420,16.500,1650.000)
    return TABLE

def full_stiffeners_table():
    TABLE = np.zeros(327,dtype=[('name',np.str_, 16),('area','f8'),('d','f8'),('tw','f8'),('bf','f8'),('tf','f8'),('yna','f8'),('Ir','f8')])
    # name area(m^2) depth(m) web thickness(m) flange width(m) flange thickness(m) yna(m) Ir (m^4)
    TABLE [0] = ('ST1.5x3.75',1.1, 1.5,0.349,2.51,0.26,1.068,0.2)
    TABLE [1] = ('ST1.5x2.85',0.83,1.5,0.17,2.33,0.26,1.171,0.114)
    TABLE [2] = ('ST2x4.75',1.39,2,0.326,2.8,0.293,1.447,0.462)
    TABLE [3] = ('ST2x3.85',1.13,2,0.193,2.66, 0.293,1.552,0.307)
    TABLE [4] = ('MT2x3',0.855,1.9,0.13,3.8,0.16, 1.559,0.208)
    TABLE [5] = ('MT2x6.5',1.9,2,0.254,3.94,0.371,1.59,0.43)
    TABLE [6] = ('WT2x6.5',1.91,2.08,0.28,4.06,0.345,1.64,0.526)
    TABLE [7] = ('ST2.5x7.375',2.17,2.5,0.494,3.284,0.326,1.711,1.27)
    TABLE [8] = ('ST2.5x5',1.47,2.5,0.214,3,0.326,1.93,0.671)
    TABLE [9] = ('MT2.5x9.45',2.78,2.5,0.316,5,0.416,1.989,1.05)
    TABLE [10] = ('WT2.5x8',2.35,2.51,0.24,5,0.36,2.052,0.845)
    TABLE [11] = ('ST3x8.63',2.53,3,0.465,3.57,0.359,2.085,2.12)
    TABLE [12] = ('WT2.5x9.5',2.78,2.58,0.27,5.03,0.43,2.093,1.01)
    TABLE [13] = ('MT3x1.85',0.54,2.96,0.098,2,0.129,2.133,0.483)
    TABLE [14] = ('MT3x2.2',0.643,3,0.114,1.84,0.171,2.159,0.579)
    TABLE [15] = ('WT3x4.25',1.25,2.92,0.17,3.94,0.194,2.282,0.904)
    TABLE [16] = ('ST3x6.25',1.83,3,0.232,3.33,0.359,2.308,1.26)
    TABLE [17] = ('WT3x4.5',1.34,2.95,0.17,3.94,0.215,2.327,0.95)
    TABLE [18] = ('WT3x6',1.78,3.02,0.23,4,0.28,2.343,1.32)
    TABLE [19] = ('WT3x7.5',2.22,3,0.23,5.99,0.26,2.443,1.41)
    TABLE [20] = ('ST3.5x10',2.94,3.5,0.45,3.86,0.392,2.46,3.36)
    TABLE [21] = ('WT3x8',2.37,3.14,0.26,4.03,0.405,2.464,1.69)
    TABLE [22] = ('MT3x10',2.94,3,0.25,5.938,0.379,2.469,1.54)
    TABLE [23] = ('WT3x10',2.95,3.1,0.26,6.02,0.365,2.54,1.76)
    TABLE [24] = ('WT3x12.5',3.68,3.19,0.32,6.08,0.455,2.58,2.29)
    TABLE [25] = ('ST3.5x7.65',2.25,3.5,0.252,3.662,0.392,2.683,2.19)
    TABLE [26] = ('MT4x3.1',0.904,4,0.129,2.28,0.177,2.82,1.5)
    TABLE [27] = ('MT4x3.25',0.953,4,0.135,2.28,0.189,2.82,1.57)
    TABLE [28] = ('ST4x11.5',3.38,4,0.441,4.17,0.425,2.85,5)
    TABLE [29] = ('WT4x6.5',1.92,4,0.23,4,0.255,2.97,2.89)
    TABLE [30] = ('WT4x5',1.48,3.95,0.17,3.94,0.205,2.997,2.15)
    TABLE [31] = ('WT4x7.5',2.22,4.05,0.245,4.01,0.315,3.052,3.28)
    TABLE [32] = ('ST4x9.2',2.7,4,0.271,4,0.425,3.058,3.49)
    TABLE [33] = ('WT4x9',2.63,4.07,0.23,5.25,0.33,3.236,3.41)
    TABLE [34] = ('WT4x12',3.54,3.97,0.245,6.5,0.4,3.275,3.53)
    TABLE [35] = ('WT4x14',4.12,4.03,0.285,6.54,0.465,3.296,4.23)
    TABLE [36] = ('WT4x10.5',3.08,4.14,0.25,5.27,0.4,3.309,3.9)
    TABLE [37] = ('WT4x15.5',4.56,4,0.285,8,0.435,3.332,4.28)
    TABLE [38] = ('WT4x17.5',5.14,4.06,0.31,8.02,0.495,3.372,4.82)
    TABLE [39] = ('WT4x20',5.87,4.13,0.36,8.07,0.56,3.395,5.73)
    TABLE [40] = ('ST5x17.5',5.14,5,0.594,4.94,0.491,3.44,12.5)
    TABLE [41] = ('MT5x4',1.17,4.97,0.141,2.69,0.182,3.45,3.08)
    TABLE [42] = ('MT5x4.5',1.32,5,0.157,2.69,0.206,3.46,3.47)
    TABLE [43] = ('WT4x24',7.05,4.25,0.4,8.11,0.685,3.473,6.85)
    TABLE [44] = ('MT5x3.75',1.1,5,0.13,2.69,0.173,3.49,2.91)
    TABLE [45] = ('WT4x29',8.54,4.38,0.51,8.22,0.81,3.506,9.12)
    TABLE [46] = ('WT4x33.5',9.84,4.5,0.57,8.28,0.935,3.564,10.9)
    TABLE [47] = ('WT5x6',1.77,4.93,0.19,3.96,0.21,3.57,4.35)
    TABLE [48] = ('WT5x7.5',2.21,5,0.23,4,0.27,3.63,5.45)
    TABLE [49] = ('WT5x8.5',2.5,5.05,0.24,4.01,0.33,3.73,6.06)
    TABLE [50] = ('ST5x12.7',3.73,5,0.311,4.66,0.491,3.8,7.79)
    TABLE [51] = ('WT5x9.5',2.81,5.12,0.25,4.02,0.395,3.84,6.68)
    TABLE [52] = ('WT5x16.5',4.85,4.87,0.29,7.96,0.435,4.001,7.71)
    TABLE [53] = ('WT5x11',3.24,5.09,0.24,5.75,0.36,4.02,6.88)
    TABLE [54] = ('WT5x19.5',5.73,4.96,0.315,7.99,0.53,4.084,8.84)
    TABLE [55] = ('MT6x5.9',1.72,6,0.177,3.07,0.225,4.11,6.61)
    TABLE [56] = ('WT5x13',3.81,5.17,0.26,5.77,0.44,4.11,7.86)
    TABLE [57] = ('MT6x5',1.46,5.99,0.149,3.25,0.18,4.13,5.62)
    TABLE [58] = ('MT6x5.4',1.58,5.99,0.16,3.07,0.21,4.13,6.03)
    TABLE [59] = ('WT5x15',4.42,5.24,0.3,5.81,0.51,4.14,9.28)
    TABLE [60] = ('WT5x22.5',6.63,5.05,0.35,8.02,0.62,4.143,10.2)
    TABLE [61] = ('ST6x25',7.32,6,0.687,5.48,0.659,4.16,25.1)
    TABLE [62] = ('WT5x24.5',7.21,4.99,0.34,10,0.56,4.183,10)
    TABLE [63] = ('WT6x7',2.08,5.96,0.2,3.97,0.225,4.2,7.67)
    TABLE [64] = ('WT5x27',7.91,5.05,0.37,10,0.615,4.214,11.1)
    TABLE [65] = ('WT5x30',8.82,5.11,0.42,10.1,0.68,4.226,12.9)
    TABLE [66] = ('WT6x8',2.36,6,0.22,3.99,0.265,4.26,8.7)
    TABLE [67] = ('WT5x34',9.99,5.2,0.47,10.1,0.77,4.268,14.9)
    TABLE [68] = ('WT5x38.5',11.3,5.3,0.53,10.2,0.87,4.31,17.4)
    TABLE [69] = ('ST6x17.5',5.12,6,0.428,5.08,0.544,4.35,17.2)
    TABLE [70] = ('WT5x44',12.9,5.42,0.605,10.3,0.99,4.36,20.8)
    TABLE [71] = ('ST6x20.4',5.96,6,0.462,5.25,0.659,4.42,18.9)
    TABLE [72] = ('WT5x50',14.7,5.55,0.68,10.3,1.12,4.42,24.5)
    TABLE [73] = ('WT6x9.5',2.79,6.08,0.235,4.01,0.35,4.43,10.1)
    TABLE [74] = ('WT5x56',16.5,5.68,0.755,10.4,1.25,4.47,28.6)
    TABLE [75] = ('ST6x15.9',4.65,6,0.35,5,0.544,4.49,14.8)
    TABLE [76] = ('WT6x11',3.24,6.16,0.26,4.03,0.425,4.53,11.7)
    TABLE [77] = ('WT6x13',3.82,6.11,0.23,6.49,0.38,4.86,11.7)
    TABLE [78] = ('MT7x9',2.55,7,0.215,4,0.27,4.88,13.1)
    TABLE [79] = ('WT6x20',5.84,5.97,0.295,8.01,0.515,4.88,14.4)
    TABLE [80] = ('WT6x15',4.4,6.17,0.26,6.52,0.44,4.9,13.5)
    TABLE [81] = ('WT6x22.5',6.56,6.03,0.335,8.05,0.575,4.9,16.6)
    TABLE [82] = ('WT6x25',7.3,6.1,0.37,8.08,0.64,4.93,18.7)
    TABLE [83] = ('WT6x17.5',5.17,6.25,0.3,6.56,0.52,4.95,16)
    TABLE [84] = ('WT6x26.5',7.78,6.03,0.345,9.99,0.575,5.01,17.7)
    TABLE [85] = ('WT6x29',8.52,6.1,0.36,10,0.64,5.07,19.1)
    TABLE [86] = ('WT6x32.5',9.54,6.06,0.39,12,0.605,5.075,20.6)
    TABLE [87] = ('WT7x11',3.25,6.87,0.23,5,0.335,5.11,14.8)
    TABLE [88] = ('WT6x36',10.6,6.13,0.43,12,0.67,5.11,23.2)
    TABLE [89] = ('WT6x39.5',11.6,6.19,0.47,12.1,0.735,5.13,25.8)
    TABLE [90] = ('WT6x43.5',12.8,6.27,0.515,12.1,0.81,5.17,28.9)
    TABLE [91] = ('WT6x48',14.1,6.36,0.55,12.2,0.9,5.23,32)
    TABLE [92] = ('WT7x13',3.85,6.96,0.255,5.03,0.42,5.24,17.3)
    TABLE [93] = ('ST7.5x25',7.34,7.5,0.55,5.64,0.622,5.25,40.5)
    TABLE [94] = ('WT6x53',15.6,6.45,0.61,12.2,0.99,5.26,36.3)
    TABLE [95] = ('WT6x60',17.6,6.56,0.71,12.3,1.11,5.28,43.4)
    TABLE [96] = ('WT7x15',4.42,6.92,0.27,6.73,0.385,5.34,19)
    TABLE [97] = ('WT6x68',20,6.71,0.79,12.4,1.25,5.36,50.6)
    TABLE [98] = ('WT6x76',22.4,6.86,0.87,12.5,1.4,5.43,58.5)
    TABLE [99] = ('WT7x17',5,6.99,0.285,6.75,0.455,5.46,20.9)
    TABLE [100] = ('ST7.5x21.45',6.3,7.5,0.411,5.5,0.622,5.49,32.9)
    TABLE [101] = ('WT6x85',25,7.02,0.96,12.6,1.56,5.5,67.8)
    TABLE [102] = ('WT7x19',5.58,7.05,0.31,6.77,0.515,5.51,23.3)
    TABLE [103] = ('WT7x21.5',6.31,6.83,0.305,8,0.53,5.52,21.9)
    TABLE [104] = ('WT7x24',7.07,6.9,0.34,8.03,0.595,5.55,24.9)
    TABLE [105] = ('WT6x95',27.9,7.19,1.06,12.7,1.74,5.57,79)
    TABLE [106] = ('WT7x26.5',7.8,6.96,0.37,8.06,0.66,5.58,27.6)
    TABLE [107] = ('WT6x105',30.9,7.36,1.18,12.8,1.9,5.64,92.1)
    TABLE [108] = ('WT7x30.5',8.96,6.95,0.375,9.99,0.645,5.7,28.9)
    TABLE [109] = ('WT6x115',33.9,7.53,1.29,12.9,2.07,5.71,106)
    TABLE [110] = ('WT7x34',9.99,7.02,0.415,10,0.72,5.73,32.6)
    TABLE [111] = ('WT8x13',3.84,7.85,0.25,5.5,0.345,5.76,23.5)
    TABLE [112] = ('WT7x37',10.9,7.09,0.45,10.1,0.785,5.77,36)
    TABLE [113] = ('WT7x41',12,7.16,0.51,10.1,0.855,5.77,41.2)
    TABLE [114] = ('WT6x126',37,7.71,1.4,13,2.25,5.79,121)
    TABLE [115] = ('WT6x139.5',41,7.93,1.53,13.1,2.47,5.88,141)
    TABLE [116] = ('WT8x15.5',4.56,7.94,0.275,5.53,0.44,5.92,27.5)
    TABLE [117] = ('WT7x45',13.2,7.01,0.44,14.5,0.71,5.92,36.5)
    TABLE [118] = ('WT7x49.5',14.6,7.08,0.485,14.6,0.78,5.94,40.9)
    TABLE [119] = ('WT7x54.5',16,7.16,0.525,14.6,0.86,5.99,45.3)
    TABLE [120] = ('WT7x60',17.7,7.24,0.59,14.7,0.94,6,51.7)
    TABLE [121] = ('WT6x152.5',44.8,8.16,1.63,13.2,2.71,6,162)
    TABLE [122] = ('WT7x66',19.4,7.33,0.645,14.7,1.03,6.04,57.8)
    TABLE [123] = ('WT8x18',5.29,7.93,0.295,6.99,0.43,6.05,30.6)
    TABLE [124] = ('ST9x35',10.3,9,0.711,6.25,0.691,6.06,84.5)
    TABLE [125] = ('WT7x72.5',21.3,7.39,0.68,15.5,1.09,6.1,62.5)
    TABLE [126] = ('WT6x168',49.4,8.41,1.78,13.4,2.96,6.1,190)
    TABLE [127] = ('WT7x79.5',23.4,7.49,0.745,15.6,1.19,6.14,70.2)
    TABLE [128] = ('WT7x88',25.9,7.61,0.83,15.7,1.31,6.18,80.5)
    TABLE [129] = ('WT8x20',5.89,8.01,0.305,7,0.505,6.2,33.1)
    TABLE [130] = ('WT8x22.5',6.63,8.07,0.345,7.04,0.565,6.21,37.8)
    TABLE [131] = ('WT8x25',7.37,8.13,0.38,7.07,0.63,6.24,42.3)
    TABLE [132] = ('WT7x96.5',28.4,7.74,0.89,15.7,1.44,6.25,89.8)
    TABLE [133] = ('WT8x28.5',8.39,8.22,0.43,7.12,0.715,6.28,48.7)
    TABLE [134] = ('WT7x105.5',31,7.86,0.98,15.8,1.56,6.29,102)
    TABLE [135] = ('WT7x116.5',34.2,8.02,1.07,15.9,1.72,6.37,116)
    TABLE [136] = ('WT7x128.5',37.8,8.19,1.18,16,1.89,6.44,133)
    TABLE [137] = ('WT9x17.5',5.15,8.85,0.3,6,0.425,6.46,40.1)
    TABLE [138] = ('ST9x27.35',8.02,9,0.461,6,0.691,6.49,62.3)
    TABLE [139] = ('WT7x141.5',41.6,8.37,1.29,16.1,2.07,6.51,153)
    TABLE [140] = ('WT7x155.5',45.7,8.56,1.41,16.2,2.26,6.59,176)
    TABLE [141] = ('WT8x33.5',9.98,8.16,0.395,10.2,0.665,6.61,48.7)
    TABLE [142] = ('WT8x38.5',11.5,8.26,0.455,10.3,0.76,6.64,57)
    TABLE [143] = ('WT9x20',5.88,8.95,0.315,6.02,0.525,6.66,44.8)
    TABLE [144] = ('WT7x171',50.3,8.77,1.54,16.4,2.47,6.68,203)
    TABLE [145] = ('WT8x44.5',13.2,8.38,0.525,10.4,0.875,6.69,67.3)
    TABLE [146] = ('WT9x23',6.77,9.03,0.36,6.06,0.605,6.7,52.1)
    TABLE [147] = ('WT8x50',14.9,8.48,0.585,10.4,0.985,6.73,76.8)
    TABLE [148] = ('WT7x185',54.4,8.96,1.66,16.5,2.66,6.77,229)
    TABLE [149] = ('WT7x199',58.5,9.15,1.77,16.6,2.85,6.85,257)
    TABLE [150] = ('WT9x25',7.33,8.99,0.355,7.5,0.57,6.87,53.5)
    TABLE [151] = ('WT9x27.5',8.1,9.06,0.39,7.53,0.63,6.9,59.5)
    TABLE [152] = ('ST10x37.5',11,10,0.635,6.39,0.795,6.93,109)
    TABLE [153] = ('WT7x213',62.6,9.34,1.88,16.7,3.04,6.94,287)
    TABLE [154] = ('WT9x30',8.82,9.12,0.415,7.56,0.695,6.96,64.7)
    TABLE [155] = ('WT9x35.5',10.4,9.23,0.495,7.64,0.81,6.97,78.2)
    TABLE [156] = ('WT9x32.5',9.55,9.18,0.45,7.59,0.75,6.98,70.7)
    TABLE [157] = ('WT7x227.5',66.9,9.51,2.02,16.8,3.21,7,321)
    TABLE [158] = ('ST10x48',14.1,10.2,0.8,7.2,0.92,7.07,143)
    TABLE [159] = ('WT7x250',73.5,9.8,2.19,17,3.5,7.13,375)
    TABLE [160] = ('ST10x33',9.69,10,0.505,6.26,0.795,7.19,92.9)
    TABLE [161] = ('WT7x275',80.9,10.1,2.38,17.2,3.82,7.25,442)
    TABLE [162] = ('ST10x43',12.7,10.2,0.66,7.06,0.92,7.29,124)
    TABLE [163] = ('WT9x38',11.2,9.11,0.425,11,0.68,7.31,71.8)
    TABLE [164] = ('WT10.5x22',6.49,10.3,0.35,6.5,0.45,7.32,71.1)
    TABLE [165] = ('WT9x43',12.7,9.2,0.48,11.1,0.77,7.34,82.4)
    TABLE [166] = ('WT9x48.5',14.3,9.3,0.535,11.1,0.87,7.39,93.8)
    TABLE [167] = ('WT9x53',15.6,9.37,0.59,11.2,0.94,7.4,104)
    TABLE [168] = ('WT9x59.5',17.5,9.48,0.655,11.3,1.06,7.45,119)
    TABLE [169] = ('WT7x302.5',88.9,10.5,2.6,17.4,4.16,7.45,524)
    TABLE [170] = ('WT10.5x25',7.36,10.4,0.38,6.53,0.535,7.47,80.3)
    TABLE [171] = ('WT7x332.5',97.8,10.8,2.83,17.7,4.52,7.55,622)
    TABLE [172] = ('WT10.5x24',7.07,10.3,0.35,8.14,0.43,7.56,74.9)
    TABLE [173] = ('WT9x65',19.1,9.63,0.67,11.2,1.2,7.61,127)
    TABLE [174] = ('WT10.5x28.5',8.37,10.5,0.405,6.56,0.65,7.65,90.4)
    TABLE [175] = ('WT9x71.5',21,9.74,0.73,11.2,1.32,7.65,142)
    TABLE [176] = ('WT9x79',23.2,9.86,0.81,11.3,1.44,7.69,160)
    TABLE [177] = ('WT7x404',119,11.4,3.74,18.6,5.12,7.7,901)
    TABLE [178] = ('WT7x365',107,11.2,3.07,17.9,4.91,7.73,739)
    TABLE [179] = ('WT9x87.5',25.7,10,0.89,11.4,1.59,7.74,181)
    TABLE [180] = ('WT10.5x27.5',8.1,10.4,0.375,8.22,0.522,7.76,84.4)
    TABLE [181] = ('WT9x96',28.2,10.175,0.96,11.455,1.75,7.835,202)
    TABLE [182] = ('WT9x105.5',31.1,10.335,1.06,11.555,1.91,7.895,229)
    TABLE [183] = ('WT10.5x31',9.13,10.5,0.4,8.24,0.615,7.92,93.8)
    TABLE [184] = ('WT9x117',34.4,10.53,1.16,11.65,2.11,7.98,260)
    TABLE [185] = ('WT10.5x36.5',10.7,10.6,0.455,8.3,0.74,8,110)
    TABLE [186] = ('WT10.5x34',10,10.6,0.43,8.27,0.685,8.01,103)
    TABLE [187] = ('WT10.5x41.5',12.2,10.7,0.515,8.36,0.835,8.04,127)
    TABLE [188] = ('WT9x129',38,10.73,1.28,11.77,2.3,8.05,298)
    TABLE [189] = ('WT10.5x46.5',13.7,10.8,0.58,8.42,0.93,8.06,144)
    TABLE [190] = ('WT9x141.5',41.6,10.925,1.4,11.89,2.5,8.125,337)
    TABLE [191] = ('ST12x50',14.7,12,0.745,7.25,0.87,8.16,215)
    TABLE [192] = ('WT9x155.5',45.8,11.16,1.52,12.005,2.74,8.23,383)
    TABLE [193] = ('WT12x27.5',8.15,11.8,0.395,7.01,0.505,8.32,117)
    TABLE [194] = ('ST12x45',13.2,12,0.625,7.13,0.87,8.4,190)
    TABLE [195] = ('WT12x31',9.16,11.9,0.43,7.04,0.59,8.45,132)
    TABLE [196] = ('WT10.5x50.5',14.9,10.7,0.5,12.3,0.8,8.52,135)
    TABLE [197] = ('WT10.5x61',17.9,10.8,0.6,12.4,0.96,8.52,166)
    TABLE [198] = ('WT10.5x55.5',16.3,10.8,0.55,12.3,0.875,8.57,150)
    TABLE [199] = ('WT10.5x66',19.4,10.9,0.65,12.4,1.03,8.57,181)
    TABLE [200] = ('WT10.5x73.5',21.6,11,0.72,12.5,1.15,8.61,204)
    TABLE [201] = ('ST12x60.5',17.8,12.3,0.8,8.05,1.09,8.67,259)
    TABLE [202] = ('ST12x40',11.7,12,0.5,7,0.87,8.7,162)
    TABLE [203] = ('WT10.5x83',24.4,11.2,0.75,12.4,1.36,8.81,226)
    TABLE [204] = ('WT12x34',10,11.9,0.415,8.97,0.585,8.84,137)
    TABLE [205] = ('WT10.5x91',26.8,11.4,0.83,12.5,1.48,8.92,253)
    TABLE [206] = ('WT10.5x100.5',29.6,11.5,0.91,12.6,1.63,8.93,285)
    TABLE [207] = ('WT12x38',11.2,12,0.44,8.99,0.68,9,151)
    TABLE [208] = ('ST12x53',15.6,12.3,0.62,7.87,1.09,9.02,216)
    TABLE [209] = ('WT12x42',12.4,12.1,0.47,9.02,0.77,9.13,166)
    TABLE [210] = ('WT12x47',13.8,12.2,0.515,9.07,0.875,9.21,186)
    TABLE [211] = ('WT12x51.5',15.1,12.3,0.55,9,0.98,9.29,204)
    TABLE [212] = ('WT12x52',15.3,12,0.5,12.8,0.75,9.41,189)
    TABLE [213] = ('WT12x58.5',17.2,12.1,0.55,12.8,0.85,9.48,212)
    TABLE [214] = ('WT12x65.5',19.3,12.2,0.605,12.9,0.96,9.55,238)
    TABLE [215] = ('WT12x73',21.5,12.4,0.65,12.9,1.09,9.74,264)
    TABLE [216] = ('WT12x81',23.9,12.5,0.705,13,1.22,9.8,293)
    TABLE [217] = ('WT12x88',25.8,12.6,0.75,12.9,1.34,9.86,319)
    TABLE [218] = ('WT12x96',28.1,12.7,0.81,13,1.46,9.9,350)
    TABLE [219] = ('WT13.5x42',12.4,13.4,0.46,9.96,0.64,9.92,216)
    TABLE [220] = ('WT12x103.5',30.4,12.9,0.87,13,1.57,10.03,382)
    TABLE [221] = ('WT12x114.5',33.6,13,0.96,13.1,1.73,10.04,431)
    TABLE [222] = ('WT13.5x47',13.8,13.5,0.49,9.99,0.745,10.09,239)
    TABLE [223] = ('WT13.5x51',15,13.5,0.515,10,0.83,10.13,258)
    TABLE [224] = ('WT12x125',36.8,13.2,1.04,13.2,1.89,10.15,478)
    TABLE [225] = ('WT13.5x57',16.8,13.6,0.57,10.1,0.93,10.18,289)
    TABLE [226] = ('WT12x139.5',41,13.4,1.16,13.3,2.09,10.22,546)
    TABLE [227] = ('WT12X153',44.9,13.6,1.26,13.4,2.28,10.31,611)
    TABLE [228] = ('WT12x167.5',49.2,13.8,1.38,13.5,2.48,10.38,686)
    TABLE [229] = ('WT13.5x64.5',18.9,13.8,0.61,10,1.1,10.41,323)
    TABLE [230] = ('WT12X185',54.4,14,1.52,13.7,2.72,10.43,779)
    TABLE [231] = ('WT12x204',59.5,14.27,1.65,13.8,2.99,10.53,874)
    TABLE [232] = ('WT15x49.5',14.5,14.8,0.52,10.5,0.67,10.71,322)
    TABLE [233] = ('WT12x246',72,14.825,1.97,14.115,3.54,10.755,1130)
    TABLE [234] = ('WT15x45',13.2,14.8,0.47,10.4,0.61,10.76,290)
    TABLE [235] = ('WT13.5x73',21.6,13.7,0.605,14,0.975,10.76,336)
    TABLE [236] = ('WT13.5x80.5',23.8,13.8,0.66,14,1.08,10.82,372)
    TABLE [237] = ('WT13.5x89',26.2,13.9,0.725,14.1,1.19,10.86,414)
    TABLE [238] = ('WT15x54',15.9,14.9,0.545,10.5,0.76,10.89,349)
    TABLE [239] = ('WT15x58',17.1,15,0.565,10.5,0.85,11.06,373)
    TABLE [240] = ('WT13.5x97',28.6,14.1,0.75,14,1.34,11.08,444)
    TABLE [241] = ('WT13.5x108.5',32,14.2,0.83,14.1,1.5,11.1,502)
    TABLE [242] = ('WT13.5x117.5',34.7,14.3,0.91,14.2,1.61,11.1,556)
    TABLE [243] = ('WT15x62',18.2,15.1,0.585,10.5,0.93,11.2,396)
    TABLE [244] = ('WT13.5x129',38,14.5,0.98,14.3,1.77,11.23,613)
    TABLE [245] = ('WT13.5x140.5',41.4,14.6,1.06,14.4,1.93,11.25,677)
    TABLE [246] = ('WT15x66',19.4,15.2,0.615,10.5,1,11.3,421)
    TABLE [247] = ('WT13.5x153.5',45.2,14.8,1.16,14.4,2.09,11.33,753)
    TABLE [248] = ('WT13.5x168',49.5,15,1.26,14.6,2.28,11.42,839)
    TABLE [249] = ('WT15x74',21.7,15.3,0.65,10.5,1.18,11.46,466)
    TABLE [250] = ('WT13.5x184',54.2,15.2,1.38,14.7,2.48,11.49,939)
    TABLE [251] = ('WT13.5x224',65.5,15.71,1.65,14.94,2.99,11.69,1190)
    TABLE [252] = ('WT15x86.5',25.5,15.2,0.655,15,1.07,11.89,497)
    TABLE [253] = ('WT16.5x59',17.3,16.4,0.55,11.5,0.74,11.93,469)
    TABLE [254] = ('WT15x95.5',28.1,15.3,0.71,15,1.19,11.96,549)
    TABLE [255] = ('WT13.5x269.5',79.3,16.3,1.97,15.3,3.54,11.96,1530)
    TABLE [256] = ('WT15x105.5',31.1,15.5,0.775,15.1,1.32,12.11,610)
    TABLE [257] = ('WT16.5x65',19.2,16.5,0.58,11.5,0.855,12.14,513)
    TABLE [258] = ('WT15x130.5',38.4,15.8,0.93,15.2,1.65,12.26,765)
    TABLE [259] = ('WT15x117.5',34.6,15.7,0.83,15.1,1.5,12.29,674)
    TABLE [260] = ('WT15x146',42.9,16,1.02,15.3,1.85,12.38,861)
    TABLE [261] = ('WT16.5x70.5',20.8,16.7,0.605,11.5,0.96,12.41,552)
    TABLE [262] = ('WT16.5x76',22.4,16.7,0.635,11.6,1.06,12.44,592)
    TABLE [263] = ('WT15x163',47.9,16.2,1.14,15.4,2.05,12.44,981)
    TABLE [264] = ('WT15x178.5',52.5,16.4,1.24,15.5,2.24,12.53,1090)
    TABLE [265] = ('WT15x195.5',57.6,16.6,1.36,15.6,2.44,12.6,1220)
    TABLE [266] = ('WT16.5x84.5',24.8,16.9,0.67,11.5,1.22,12.69,649)
    TABLE [267] = ('WT15x238.5',70,17.105,1.63,15.865,2.95,12.805,1550)
    TABLE [268] = ('WT18x67.5 ',19.9,17.8,0.6,12,0.79,12.84,637)
    TABLE [269] = ('WT16.5x100.5',29.6,16.8,0.715,15.7,1.15,13.03,725)
    TABLE [270] = ('WT18x75',22.1,17.9,0.625,12,0.94,13.12,698)
    TABLE [271] = ('WT16.5x110.5',32.6,17,0.775,15.8,1.27,13.19,799)
    TABLE [272] = ('WT18x80',23.5,18,0.65,12,1.02,13.26,740)
    TABLE [273] = ('WT16.5x120.5',35.5,17.1,0.83,15.9,1.4,13.26,872)
    TABLE [274] = ('WT18x85',25,18.1,0.68,12,1.1,13.37,786)
    TABLE [275] = ('WT18x97',28.5,18.2,0.765,12.1,1.26,13.4,901)
    TABLE [276] = ('WT18x91',26.8,18.2,0.725,12.1,1.18,13.43,845)
    TABLE [277] = ('WT18x105',30.9,18.3,0.83,12.2,1.36,13.43,985)
    TABLE [278] = ('WT16.5x131.5',38.7,17.3,0.87,15.8,1.57,13.47,943)
    TABLE [279] = ('WT16.5x145.5',42.8,17.4,0.96,15.9,1.73,13.47,1060)
    TABLE [280] = ('WT16.5x159',46.8,17.6,1.04,16,1.89,13.58,1160)
    TABLE [281] = ('WT20x74.5',21.9,19.1,0.63,11.8,0.83,13.65,815)
    TABLE [282] = ('WT16.5x177',52.1,17.8,1.16,16.1,2.09,13.65,1320)
    TABLE [283] = ('WT16.5x193.5',57,18,1.26,16.2,2.28,13.73,1460)
    TABLE [284] = ('WT18x116',34.1,18.6,0.87,12.1,1.57,13.78,1080)
    TABLE [285] = ('WT18x128',37.7,18.7,0.96,12.2,1.73,13.78,1210)
    TABLE [286] = ('WT18x122.5',36,18,0.8,16.5,1.35,13.97,995)
    TABLE [287] = ('WT18x115',33.8,18,0.76,16.5,1.26,13.99,934)
    TABLE [288] = ('WT18x130',38.2,18.1,0.84,16.6,1.44,14.05,1060)
    TABLE [289] = ('WT20x83.5',24.6,19.3,0.65,11.8,1.02,14.11,899)
    TABLE [290] = ('WT20x87',25.5,19.1,0.65,15.75,0.83,14.23,907)
    TABLE [291] = ('WT18x140',41.2,18.3,0.885,16.6,1.57,14.23,1140)
    TABLE [292] = ('WT18x150',44.1,18.4,0.945,16.7,1.68,14.27,1230)
    TABLE [293] = ('WT18x164',48.2,18.5,1.02,16.6,1.85,14.29,1350)
    TABLE [294] = ('WT18x179.5',52.7,18.7,1.12,16.7,2.01,14.37,1500)
    TABLE [295] = ('WT18x196.5',57.8,18.9,1.22,16.8,2.2,14.46,1660)
    TABLE [296] = ('WT18x219.5',64.5,19.1,1.36,17,2.44,14.5,1890)
    TABLE [297] = ('WT20x91.5',26.9,19.5,0.65,11.8,1.22,14.57,958)
    TABLE [298] = ('WT20x132',38.8,20,0.96,11.9,1.73,14.59,1450)
    TABLE [299] = ('WT20x139',40.9,20.1,1.02,12,1.81,14.6,1540)
    TABLE [300] = ('WT20x105.5',31,19.7,0.75,11.8,1.42,14.62,1120)
    TABLE [301] = ('WT20x117.5',34.5,19.8,0.83,11.9,1.58,14.63,1260)
    TABLE [302] = ('WT20x165.5',48.7,20.4,1.22,12.2,2.13,14.66,1880)
    TABLE [303] = ('WT18x263.5',77.4,19.6,1.61,17.2,2.91,14.73,2340)
    TABLE [304] = ('WT20x163.5',48,20.4,1.18,12.1,2.13,14.74,1840)
    TABLE [305] = ('WT20x99.5',29.2,19.3,0.65,15.8,1.07,14.83,988)
    TABLE [306] = ('WT20x196',57.7,20.8,1.42,12.4,2.52,14.85,2270)
    TABLE [307] = ('WT18x325',95.5,20.2,1.97,17.6,3.54,14.94,3030)
    TABLE [308] = ('WT20x233',68.4,21.22,1.67,12.64,2.95,15,2770)
    TABLE [309] = ('WT20x148.5',43.7,19.9,0.93,15.8,1.65,15.19,1500)
    TABLE [310] = ('WT20x107.5',31.7,19.5,0.65,15.8,1.22,15.22,1030)
    TABLE [311] = ('WT20x160.5',47,20.04,1,15.91,1.77,15.25,1630)
    TABLE [312] = ('WT20x124.5',36.7,19.7,0.75,15.8,1.42,15.29,1210)
    TABLE [313] = ('WT18x399',117,21,2.38,18,4.29,15.29,3930)
    TABLE [314] = ('WT20x138.5',40.7,19.8,0.83,15.8,1.58,15.3,1360)
    TABLE [315] = ('WT20x162',47.7,20.1,1,15.9,1.81,15.33,1650)
    TABLE [316] = ('WT20x186',54.7,20.3,1.16,16.1,2.05,15.33,1930)
    TABLE [317] = ('WT18x424',125,21.225,2.52,18.13,4.53,15.365,4250)
    TABLE [318] = ('WT20x181',53.3,20.3,1.12,16,2.01,15.39,1870)
    TABLE [319] = ('WT20x215.5',63.4,20.6,1.34,16.2,2.36,15.42,2290)
    TABLE [320] = ('WT20x198.5',58.4,20.5,1.22,16.1,2.2,15.47,2070)
    TABLE [321] = ('WT20x251.5',74,21,1.54,16.4,2.76,15.61,2730)
    TABLE [322] = ('WT20x296.5',87.2,21.5,1.79,16.7,3.23,15.84,3310)
    TABLE [323] = ('WT22x115',33.8,21.5,0.71,15.8,1.22,16.33,1440)
    TABLE [324] = ('WT22x167.5',49.1,22,1.02,16,1.77,16.49,2160)
    TABLE [325] = ('WT22x131',38.6,21.7,0.79,15.8,1.42,16.5,1650)
    TABLE [326] = ('WT22x145',42.9,21.8,0.87,15.8,1.58,16.53,1840)
    return TABLE