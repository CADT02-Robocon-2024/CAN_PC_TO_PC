import com.can as com

def send_data(mid, data):
    m_data = []
    m_data.append(0xAA)
    m_data.append(0xC8)
    m_data.append(0x00+ mid)
    m_data.append(0x01)
    for i in range(4, 12):
        m_data.append(0x00)
    m_data.append(0x55)
    com.uca.frame_send(data)
    print("Data sent")
def receive_data():
    while True:
        frame = com.uca.frame_receive()
        
        if frame:
            print("Data received")
            print(frame)
        else:
            print("No data received")