import numpy as np
import matplotlib.pyplot as plt

#################### Reading Sensory Data from the Given Text File############
sensor_readings = []
Open_Data=open('imudata.txt')
for line in Open_Data:
    print(line)
    line=line.rstrip()
    line=line.split()
    sensor_readings.append(int(line[4]))
    # print(sensor_readings)

# print(sensor_readings)
sens_arr = np.asarray(sensor_readings)
# print(sens_arr)


# ###################### Plotting the data#############
plt.subplot(331)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
plt.title('Raw Data Corresponding to the Pitch Angle')
plt.legend()
plt.show()
# ############## Moving Point Averages #############

def mov_avg(array,window_size):
    es=[]
    size=window_size-1
    for i in range(len(array)-size):
        data=array[i:i+window_size]
        avg_mean=np.mean(data)
        es.append(avg_mean)
    return es, i

######################## 2POINT WEIGHTED AVERAGE ##############
plt.subplot(332)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
# plt.title('Raw Data Corresponding to the Pitch Angle')
ps1, i1 = mov_avg(sens_arr,2)
# print(len(ps1))
msd_1 = 'Mean: {0:.4f} \n SD: {1:.4f}'.format(np.mean(ps1), np.std(ps1))
plt.annotate(msd_1,xy=(0.05,0.05))
x1 = np.arange(0, i1 + 1, 1)
plt.plot(x1, ps1,label='2pt Moving Average Data')
plt.legend()

############### 4 POINT WEIGHTED AVERAGE ###################
plt.subplot(333)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
# plt.title('Raw Data Corresponding to the Pitch Angle')
ps2, i2 = mov_avg(sens_arr,4)
# print(len(ps2))
msd_2 = 'Mean: {0:.4f} \n SD: {1:.4f}'.format(np.mean(ps2), np.std(ps2))
plt.annotate(msd_2,xy=(0.05,0.05))
x2=np.arange(0,i2+1,1)
plt.plot(x2,ps2,label='4pt Moving Average Data')
plt.legend()

############## 8 POINT WEIGHHTED AVERAGE #######################
plt.subplot(334)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
# plt.title('Raw Data Corresponding to the Pitch Angle')
ps3, i3 = mov_avg(sens_arr,8)
# print(len(ps3))
msd_3 = 'Mean: {0:.4f} \n SD: {1:.4f}'.format(np.mean(ps3), np.std(ps3))
plt.annotate(msd_3,xy=(0.05,0.05))
x3=np.arange(0,i3+1,1)
plt.plot(x3,ps3,label='8pt Moving Average Data')
plt.legend()


################# 16 POINT WEIGHTED AVERAGE ##################
plt.subplot(335)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
# plt.title('Raw Data Corresponding to the Pitch Angle')
ps4, i4 = mov_avg(sens_arr,16)
# print(len(ps4))
msd_4 = 'Mean: {0:.4f} \n SD: {1:.4f}'.format(np.mean(ps4), np.std(ps4))
plt.annotate(msd_4,xy=(0.05,0.05))
x4=np.arange(0,i4+1 ,1)
plt.plot(x4,ps4,label='16pt Moving Average Data')
plt.legend()

###################### 64 POINT WEIGHTED AVERAGE ####################
plt.subplot(336)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
# plt.title('Raw Data Corresponding to the Pitch Angle')
ps5, i5 = mov_avg(sens_arr,64)
# print(len(ps5))
msd_5 = 'Mean: {0:.4f} \n SD: {1:.4f}'.format(np.mean(ps5), np.std(ps5))
plt.annotate(msd_5,xy=(0.05,0.05))
x5=np.arange(0,i5+1,1)
plt.plot(x5,ps5,label='64pt Moving Average Data')
plt.legend()

################### 128 POINT WEIGHTED AVERAGE ######################
plt.subplot(337)
x=np.arange(0,371,1)
plt.plot(x,sens_arr,label='Pitch Angle (Degrees)')
plt.xlabel('Range of Sensory Data')
plt.ylabel('Accelerometer Data (Degrees)')
# plt.title('Raw Data Corresponding to the Pitch Angle')
ps6, i6 = mov_avg(sens_arr,128)
# print(len(ps6))
msd_6 = 'Mean: {0:.4f} \n SD: {1:.4f}'.format(np.mean(ps6), np.std(ps6))
plt.annotate(msd_6,xy=(0.05,0.05))
x6=np.arange(0,i6+1,1)
plt.plot(x6,ps6,label='128pt Moving Average Data')
plt.legend()