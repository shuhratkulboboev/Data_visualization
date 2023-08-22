import numpy as np
import matplotlib.pyplot as plt
import csv


with open('Orientation.csv','r') as f:
    data = list(csv.reader(f,delimiter=','))
data1 = np.array(data[1:],dtype=np.float64)
time1 =data1[:,0]
time = data1[:,1]
qz= data1[:,6]
qy = data1[:,7]
qx = data1 [:,8]
#qw = data1[:,5]



plt.figure(figsize =(20,10))
#plt.plot(time,elapsed,time,z,time,y,time,x)
plt.plot(time,qz,c='r',label = "qz")
plt.plot(time,qy,c='b',label = "qy")
plt.plot(time,qx,c='g',label = "qx")
#plt.plot(time,qw,c='y',label = "qw")
#plt.plot(time,elapsed,c='r',label = "second_elapsed")
plt.title("Orientation data ",fontsize =20)
plt.xlabel('Time',fontsize=20)
plt.ylabel("Output values",fontsize=20)
plt.legend()
plt.show()