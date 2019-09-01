import numpy as np

def get_Pn(Gain):
    h = 6.62606896*10e-34
    f = 193.1*10e12
    B = 50*10e9
    NF = 4
    Pn = 2*np.pi*h*f*B*(NF + 1/Gain)

    return Pn

def get_SNR(Ps, Pn):
    SNR = 10*np.log10(Ps/Pn)

    return SNR

print(get_Pn(6))