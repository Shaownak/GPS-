import serial
from serial import Serial

class GPS:
    def __init__(self, port, baud_rate):
        self.gps_serial_port = serial.Serial(port, baud_rate)

    def get_lat_long(self):
        s = self.gps_serial_port.read(500)
        s = s.decode('utf-8')
        data = s.splitlines()
        for i in range(len(data)):
            d = data[i].split(',')
            if d[0] == "$GPGGA" and len(d) == 15:
                if d[2] == '' or d[4] == '':
                    return "N/A", "N/A"
                else:
                    lat = float(d[2]) / 100
                    long = float(d[4]) / 100
                    return lat, long

    def get_time(self):
        s = self.gps_serial_port.read(500)
        s = s.decode('utf-8')
        data = s.splitlines()
        for i in range(len(data)):
            d = data[i].split(',')
            if d[0] == "$GPGGA" and len(d) == 15:
                if d[1] == '':
                    return "N/A"
                else:
                    time_val = int(float(d[1]) / 100)
                    time_val = time_val / 100
                    return time_val

    def get_quality_indicator(self):
        s = self.gps_serial_port.read(500)
        s = s.decode('utf-8')
        data = s.splitlines()
        for i in range(len(data)):
            d = data[i].split(',')
            if d[0] == "$GPGGA" and len(d) == 15:
                return d[6]

    def get_no_of_satellites(self):
        s = self.gps_serial_port.read(500)
        s = s.decode('utf-8')
        data = s.splitlines()
        for i in range(len(data)):
            d = data[i].split(',')
            if d[0] == "$GPGGA" and len(d) == 15:
                return d[7]

    def get_raw_data(self):
        s = self.gps_serial_port.read(500)
        s = s.decode('utf-8')
        data = s.splitlines()
        for i in range(len(data)):
            d = data[i].split(',')
            if d[0] == "$GPGGA" and len(d) == 15:
                return d

if __name__ == '__main__':
    x = GPS(port="COM13", baud_rate=9600)
    while True:
        p = x.get_lat_long()
        print(p)
    
