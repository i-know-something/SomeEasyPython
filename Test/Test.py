#程序参考简书代码https://www.jianshu.com/p/ec98a31fc782
#测试新下载的几个包


import pywt
import numpy as np
import matplotlib.pyplot as plt

sampline_rate = 1024
t = np.arange(0,1.0,1.0/sampline_rate)

f1=100
f2=200
f3=100

data = np.piecewise(t,[t<1,t<0.8,t<0.3],
                    [lambda t :np.sin(2*np.pi*f1*t),
                     lambda t :np.sin(2*np.pi*f2*t),
                     lambda t :np.sin(2*np.pi*f3*t)])

wavename = "cgau8"
totalscal = 256

fc = pywt.central_frequency(wavename)#center frequency

cparam = 2 * fc *totalscal
scales = cparam/np.arange(totalscal,1,-1)
[cwtmatr,frequencies] = pywt.cwt(data,scales,wavename,1.0/sampline_rate) #连续小波变换

plt.figure(figsize=(8,4))
plt.plot(t,data)
plt.xlabel(u"time(s)")
plt.subplot(211)
plt.plot(t, data)
plt.xlabel(u"time(s)")
plt.title(u"300Hz 200Hz 100Hz Time spectrum")
plt.subplot(212)
plt.contourf(t, frequencies, abs(cwtmatr))
plt.ylabel(u"freq(Hz)")
plt.xlabel(u"time(s)")
plt.subplots_adjust(hspace=0.4)
plt.show()