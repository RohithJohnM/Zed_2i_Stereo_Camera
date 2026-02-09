#To verify whether computer and Python actually see the ZED camera"
import pyzed.sl as sl

def main():
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.sdk_verbose = 1

    print("Opening ZED Camera...")
    err = zed.open(init_params)
    
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"Camera Failed to Open. Error Code: {err}")
        exit(1)

    info = zed.get_camera_information()
    print(f"Success! Connected to {info.camera_model}")
    print(f"Serial Number: {info.serial_number}")
    zed.close()

if __name__ == "__main__":
    main()
