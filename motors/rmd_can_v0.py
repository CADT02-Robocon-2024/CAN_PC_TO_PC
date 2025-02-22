import com.can as com

def ratio(mid, ang, velo):
    if mid == 1:
        ang *= 6.0
        velo *= 6.0
    elif mid == 2:
        ang *= 6.0
        velo *= 6.0
    elif mid == 3:
        ang *= 6.0
        velo *= 6.0
    elif mid == 4:
        ang *= 6.0
        velo *= 6.0
    elif mid == 5:
        ang *= 9.0
        velo *= 9.0
    elif mid == 6:
        ang *= 9.0
        velo *= 9.0
    else:
        ang *= 30.0
        velo *= 30.0
    return int(ang * 100), int(velo * 100)

def int_byte(int_data):
    return int_data & 0xFF


def run_speed(mid, velo):
    result = 0
    # chsum = 0
    degree, speed = ratio(mid, 0, velo)
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x40 + mid)
    m_data.append(0x01)
    m_data.append(0x00)
    m_data.append(0x00)
    m_data.append(0x00)
    m_data.append(0x00)
    for i in range(8, 12):
        m_data.append(int_byte(speed >> 8 * (i - 8)))
    m_data.append(0x55)
    # print("moving")
    # m_data_hex = [hex(i) for i in m_data]
    com.uca.frame_send(m_data)
    # print(type(m_data_hex[0]))
    #com.uca.inject_data_frame(0x40 + mid, m_data_hex)
    #print(com.uca.extract_data(m_data))
    
def test_degree(mid):
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x40 + mid)
    m_data.append(0x04)
    m_data.append(0xa4)
    m_data.append(0x00)
    m_data.append(0xf4)
    m_data.append(0x01)
    m_data.append(0xa0)
    m_data.append(0x8c)
    m_data.append(0x00)
    m_data.append(0x00)
    m_data.append(0x55)
    com.uca.frame_send(m_data)
    # com.uca.inject_data_frame(0x40 + mid, ['a4', '00', 'f4', '01', 'a0', '8c', '00', '0x00'])

def run_boolean (mid, boolean_value):
    boolean_bytes = [0x01 if val else 0x00 for val in boolean_value]
    m_data = []
    m_data.append(0xAA) # Header byte
    m_data.append(0xC8) # Command Byte
    m_data.append(0x00 + mid) # Device ID
    m_data.append(0x00)
    # 4 to 12 is free space allocated for control boolean data 
    for i in range(4,8):
        m_data.append(boolean_bytes[i-4])
    for i in range(8,12):
        m_data.append(0x00)
    m_data.append(0x55) # Tail byte
    com.uca.frame_send(m_data)
    