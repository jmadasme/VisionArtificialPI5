import cv2

def list_cameras(max_index=10):
    """
    Attempts to open camera devices from index 0 up to max_index
    and prints which ones are available.
    """
    print("Searching for connected cameras...")
    found_cameras = []
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"  Camera found at index: {i}")
            found_cameras.append(i)
            cap.release() # Release the camera immediately
        else:
            print(f"  No camera at index: {i}")
    
    if not found_cameras:
        print("\nNo cameras found. Please ensure your USB camera is properly connected.")
    else:
        print("\nTo use a specific camera, replace '0' with its index (e.g., '1', '2') in your script.")
    return found_cameras

if __name__ == "__main__":
    available_cameras = list_cameras()

    # You can then use the index of your desired camera in your main script:
    # if available_cameras:
    #     # For example, to open the first found camera:
    #     # camara = cv2.VideoCapture(available_cameras[0])
    #     # Or if you know your new camera is at index 1:
    #     # camara = cv2.VideoCapture(1)
    #     pass # Do nothing here, just demonstrating
