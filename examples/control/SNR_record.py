import os
import time
import random
import numpy as np
from scipy import stats
from datetime import datetime
import data_interface

current_file_path = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file_path)
parent_dir = os.path.dirname(current_dir)
print(parent_dir)


radar_log_path      = os.path.join(parent_dir, 'data', 'radar_log.csv')
comm_log_path       = os.path.join(parent_dir, 'data', 'comm_log.csv')
packet_log_path     = os.path.join(parent_dir, 'data', 'packet_log.csv')
plot_log_path     = os.path.join(parent_dir, 'data', 'plot_log.csv')

radar_data_path     = os.path.join(parent_dir, 'data', 'radar_data.csv')
packet_data_path    = os.path.join(parent_dir, 'data', 'packet_data.csv')


# Testing
current_time = '22:10:39.001'
peak_power = 0.0239202
snr_est = 23
range_val = 5.10998
angle_val = -55.599
packet_type = 1 # 1 for NDP, 2 for Data
packet_size = 100
test_packet_type = 1


#create radar_data
test_radar = data_interface.RadarData(current_time, peak_power, snr_est, range_val, angle_val)

#create comm_data
test_comm = data_interface.CommData(current_time, 0, packet_type, snr_est, snr_est, 1, 0,0)

#create packet_data
test_packet = data_interface.PacketData(current_time, packet_type, packet_size)


last_timestamp = None
last_data_timestamp = None
data_array = []
snr_array = []
mode_variable = None
ave_snr = None
ndp_flag = 0
data_flag = 0

while True:

    time.sleep(0.005)
    test_radar = data_interface.load_radar_data(radar_log_path)
    test_comm = data_interface.load_comm_data(comm_log_path)
    current_time = datetime.now()
    test_packet.timestamp =  current_time.strftime("%H:%M:%S") + ':' + current_time.strftime("%f")[:3]  

    while ndp_flag <= 20:
        test_packet.packet_type = 1
        test_packet.packet_size = 7
        test_radar = data_interface.load_radar_data(radar_log_path)
        current_time = datetime.now()
        last_timestamp = datetime.now()
        test_packet.timestamp =  current_time.strftime("%H:%M:%S") + ':' + current_time.strftime("%f")[:3]

        if last_timestamp != test_radar.timestamp: # record radar angle
            ndp_flag += 1
            last_timestamp = test_radar.timestamp
            data_array.append(test_radar.est_angle)
        
        data_interface.write_packet_data(test_packet,packet_data_path)
        data_interface.write_radar_data(test_radar, radar_data_path)

    mode_variable = stats.mode(np.array(data_array))[0][0]
    print(f"the mode of the angle is: {mode_variable}")
    test_packet.timestamp =  current_time.strftime("%H:%M:%S") + ':' + current_time.strftime("%f")[:3]
    
    while data_flag <= 20:
        test_packet.packet_type = 2
        test_packet.packet_size = 300
        current_time = datetime.now()
        last_data_timestamp = datetime.now()
        test_comm = data_interface.load_comm_data(comm_log_path)
        test_packet.timestamp =  current_time.strftime("%H:%M:%S") + ':' + current_time.strftime("%f")[:3]

        if last_data_timestamp != test_comm.timestamp: # record comm SNR
            data_flag += 1
            last_data_timestamp = test_comm.timestamp
            snr_array.append(test_comm.data_snr)

        test_radar.est_angle = mode_variable
        data_interface.write_packet_data(test_packet,packet_data_path)
        data_interface.write_radar_data(test_radar, radar_data_path)
        
    ave_snr = np.mean(snr_array)
    print(f"the average SNR is: {ave_snr}, beamforming angle is: {test_radar.est_angle}")
    data_interface.write_plot_log(2, mode_variable, mode_variable, ave_snr, test_comm.CRC, test_comm.throughput, plot_log_path)
    data_flag = 0
    ndp_flag = 0
    data_array.clear()
    snr_array.clear()
    print("Go to next angle")


    #data_interface.write_radar_data(test_radar, radar_data_path)
    #data_interface.write_radar_log(test_radar, radar_log_path)
    #data_interface.write_plot_log(test_comm.packet_type, test_radar.est_angle, test_radar.est_angle, test_comm.data_snr, test_comm.CRC, test_comm.throughput, plot_log_path)

    #data_interface.write_packet_data(test_packet, packet_data_path)
    #data_interface.write_packet_log(test_packet, packet_log_path)

    #test_comm = data_interface.load_comm_data(comm_log_path)
    #print(test_comm.rx_snr)


 