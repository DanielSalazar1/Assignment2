
import os

def get_command_input():
   print("Indoor Air Quality Monitoring Command Console\n")
   print("Please select from the following options:")
   print("(A) Add reading")
   print("(B) List readings")
   print("(C) Calculate")
   print("(D) Exit\n")
   command == input("input: ")
   os.system("clear")
   return command

def get_readings():
    print("Please input info: ")
    temperature = input("Temperature (degrees): ")
    humidity = input("humidity (%): ")
    pressure = input("pressure (kPa): ")
    altitude = input("altitude (ft): ")
    tvoc = input("tvoc (ppb): ")
    co2 = input("co2 (ppm): ")
    readings = {
       "temperature" : temperature,
       "humidity" : humidity,
       "pressure" : pressure,
       "altitude" : altitude,
       "tvoc" : tvoc,
       "co2" : co2
    }
    os.system("clear")
    print("*******************")
    print("Readings succesfully saved")
    print("*******************")
    print("\nHit enter to return to the menu")
    input()

    os.system("clear")
    return readings

    def main():
        main_loop_is_running = True

    readings = []

    while main_loop_is_running:
        command = get_command_input()
        if command == "A":
            data_reading = get_readings()
            readings.append(data_reading)
        elif command == "B":
            print("TODO: List readings GUI page")
        elif command == "C":
            print("TODO: Calculate")
        elif command in ["d", "D"]:
            main_loop_is_running = False
