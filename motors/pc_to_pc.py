import com.can as com

def silo_data_convert(data):
    if data == 1:
        return 0x01
    elif data == 2:
        return 0x02
    elif data == 3:
        return 0x03
    elif data == 4:
        return 0x04
    elif data == 5:
        return 0x05
def send_data_can(mid, data):
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x00 + mid)
    m_data.append(0x01)
    m_data.append(silo_data_convert(data))
    for i in range(5, 12):
        m_data.append(0x00)
    m_data.append(0x55)
    com.uca.frame_send(m_data)
    print("Data sent")
