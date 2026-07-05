# Copyright 2025 by Alon Gil-Ad
# Center for Intelligent Systems (CIS), Faculty of Computer Science
# Technion - Israel Institute of Technology
# https://github.com/AlonGil-Ad/simple_mocap

import logging
from time import sleep
from simple_mocap import SimpleMocap

if __name__ == "__main__":
    logger = logging.getLogger()
    logging.basicConfig(encoding='utf-8')
    logger.setLevel('DEBUG')
    mocap = SimpleMocap(local_ip="10.240.10.123", server_ip="10.240.10.0")

    for i in range(5):
        print(f'Frame number: {mocap.get_frame_number()}')                      # Get frame number
        print(f'Target: {mocap.get_location("IOT_car")}')                        # Get rigid body "Target" by name
        print(f'Target: {mocap.get_location(600)}')                             # Get rigid body "Traget" by ID
        sleep(1)

    mocap.shutdown()        # Always call shutdown before script end

