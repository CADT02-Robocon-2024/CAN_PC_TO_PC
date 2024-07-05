# import log_msg.logger as log
# import motors.cal_motor as mm
import threading
import motors.rmd_can_v0 as motor
import motors.movement as movement
import motors.pc_to_pc as canPC
# import motors.monent as mo
# import cv2
# new
import time
#import com.rs_485 as com
import com.can as can

# import motors.rs_485_port as rs485
# import test_distance.tracking as pos
global reload
# M = [0, 0, 0, 0]
# pwm_ = [0, 0, 0, 0]
# v = [0, 0, 0, 0]
# deltaT = 0.02




def map_range(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


def mainprog():
    global reload
    # movement.move(1000,0,0)
    while(True):
    # motor.run_boolean(6,(1,0,0,1))
    # while True:
        # canPC.send_data(10, [1, 0, 0, 0, 0])
        canPC.receive_data()
    #     movement.move(1000,0,0)
    #     motor.test_degree(2)
    #     motor.run_speed(4, 0)
        



# global reload 


def testing():
    speed = motor.read_speed_all()
    print(speed)
    # print(speed)
    # motor.runInc_speed(1, 1, 4225)  # 10
    # motor.runInc_speed(2, 1, -4225)
    # motor.runInc_speed(3, 1, 4225)
    # motor.runInc_speed(4, 1, -4225)


if __name__ == "__main__"   :
    thread3 = threading.Thread(target=mainprog)
    thread3.start()

    # thread2 = threading.Thread(target=motor.rmd)
    # thread2.start()

    # thread2 = threading.Thread(target=can.read_from_port, args=(can.uca,))
    # thread2.start()
