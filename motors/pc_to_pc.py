import com.can as com

def send_data_can(mid):
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x00 + mid)
    m_data.append(0x01)
    m_data.append(0x01)
    for i in range(5, 12):
        m_data.append(0x00)
    m_data.append(0x55)
    com.uca.frame_send(m_data)
    print("Data sent")
