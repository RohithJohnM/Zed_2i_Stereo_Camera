#basic script to capture a single photo using the ZED camera's left lens and save it to your computer.
import pyzed.sl as sl
import cv2
import numpy as np

def main():
    # Create a Camera object
    zed = sl.Camera()

    # Set configuration parameters
    init_params = sl.InitParameters()
    init_params.camera_resolution = sl.RESOLUTION.HD720
    init_params.camera_fps = 30

    # Open the camera
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"Camera Failed to Open: {err}")
        exit(1)

    # Prepare a container to hold the image (sl.Mat)
    image_zed = sl.Mat()

    print("Camera is open. Press 's' to save an image, 'q' to quit.")

    # Loop to wait for a frame
    runtime_parameters = sl.RuntimeParameters()
    
    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        # Retrieve the left image
        zed.retrieve_image(image_zed, sl.VIEW.LEFT)
        
        # Convert to a numpy array for OpenCV
        image_ocv = image_zed.get_data()
        
        # Save the image
        cv2.imwrite("zed_capture.png", image_ocv)
        print("Success! Image saved as 'zed_capture.png'")

    # Close the camera
    zed.close()

if __name__ == "__main__":
    main()