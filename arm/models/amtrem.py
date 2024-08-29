import subprocess
import time
import sys
import serial
import logging
#lsblk --output TYPE, MOUNTPOINT | grep 'rom'

LOADER_PATH = "/dev/ttyUSB0"
# SERIAL_DRIVE_PATH = "src/serial_drive"

# Check if /src/serial_drive is vaild
# def check_serial_drive(compile_if_missing=True):
#     if not os.path.exists(SERIAL_DRIVE_PATH):
#         if compile_if_missing:
#             subprocess.run(["/usr/bin/gcc", "src/serial_drive.c", "-o",SERIAL_DRIVE_PATH])
#     else:
#         raise FileNotFoundError(f"Serial Device: {SERIAL_DRIVE_PATH} not found")




class DiscLoader:
      
    @staticmethod
    def _loader(options: str):
        '''
        Core Commands:
        V: Signup or version(sometimes required as first command)
        C: Reset or Calibrate unit
        I: Input disc from bin to drive
        A: Accept disc from drive to output bin
        G: Get disc from drive and hold in picker(required before R and sometimes A)
        R: Move disc from picker to Reject bin
        S: Status of mechanis Trial and Error:
        B: 'G'rab from Printer
        H: If 'G'rabbing, put in CD Tray
        P: Same as G
        K: Input stack -> Printer,
        If currently 'G'rabbing,
        it will move that to the input queue,
        drop it, and then move it to the printer.
        D: Down
        U: Up
        L: Load Printer
        M: Drop
        N: Get from Printer
        Q: Accept from Printer
        T: Test(input -> cd_tray, cd_tray -> accept_bin)
        W: some type of 3 number status
        '''

        def write_port(device_name, command):
            buf = bytearray(255)
            try:
                # Open serial port
                ser = serial.Serial(device_name, 9600, timeout=1)
                
                # Write command to serial port
                ser.write(command.encode())
                # time.sleep(20)
                # Read response from serial port
                m = ser.readinto(buf)
                ser.close()
                
                return buf[:m].decode()
            except serial.SerialException as e:
                logging.error(f"AMTREM Serial Error: {e}\n")

        if options not in ["V", "C", "I", "A", "G", "R", "S", "B", "H", "P", "K", "D", "U", "L", "M", "N", "Q", "T", "W"]:
            raise ValueError("Invaild option selected in _loader function")

        logging.debug(f"Discloader Option selected: {options}")
        # command = [f".{SERIAL_DRIVE_PATH}", LOADER_PATH , options]
        # print(command)
        # p1 = subprocess.run(command, capture_output=True)
        
        time.sleep(5)
        return write_port(device_name=LOADER_PATH, command=options)

    @staticmethod
    def calibrate_unit():
        '''Reset or Calibrate unit'''
        DiscLoader._loader("C")
        
    @staticmethod
    def version():    
        '''Signup or version(sometimes required as first command)'''
        DiscLoader._loader("V")
    
    @staticmethod
    def insert_disc_to_from_bin():
        '''Insert put disc from bin to drive'''
        DiscLoader._loader("I")
    
    @staticmethod
    def send_disc_from_drive_to_output_bin():
        '''Accept disc from drive to output bin'''
        DiscLoader._loader("A")

    @staticmethod
    def status():
        '''Status of Mechinisim'''
        DiscLoader._loader("S")


if __name__ == "__main__":
    # check_serial_drive()
    DiscLoader.version()
    DiscLoader.calibrate_unit()
    # DiscLoader.insert_disc_to_from_bin()