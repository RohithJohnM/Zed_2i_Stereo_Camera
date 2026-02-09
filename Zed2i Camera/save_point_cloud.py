import pyzed.sl as sl
import sys

def main():
    # 1. Create and Open the Camera
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE 
    init_params.coordinate_units = sl.UNIT.METER  # Use Meters
    init_params.coordinate_system = sl.COORDINATE_SYSTEM.RIGHT_HANDED_Y_UP

    print("Opening ZED Camera...")
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(f"Error: {err}")
        exit(1)

    # 2. Prepare the container
    # A Point Cloud is huge (millions of points), so we use a specific MAT type
    point_cloud = sl.Mat()

    print("Camera is open. Point the camera at your scene.")
    print("Press 'Enter' to capture the 3D Point Cloud...")
    input() # Wait for user

    # 3. Capture the Data
    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        print("Capturing... (This might take a second)")
        
        # We use MEASURE.XYZRGBA to get (X, Y, Z) position + (R, G, B) color for every pixel
        zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA)

        # 4. Save to a .PLY file
        # PLY is a standard 3D file format (like .JPG but for 3D)
        save_path = "my_room_3d.ply"
        err = point_cloud.write(save_path)

        if err == sl.ERROR_CODE.SUCCESS:
            print(f"✅ Success! Saved 3D Point Cloud to: {save_path}")
            print("You can now open this file in ZED Depth Viewer or MeshLab.")
        else:
            print(f"❌ Failed to save file: {err}")

    zed.close()

if __name__ == "__main__":
    main()