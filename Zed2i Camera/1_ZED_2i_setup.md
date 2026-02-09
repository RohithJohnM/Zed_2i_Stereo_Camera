# ZED 2i Camera Setup Guide: From Zero to Hero

**Target Audience:** Beginners with no prior knowledge.  
**System:** Windows 10/11 with NVIDIA GPU (RTX 2050 or similar).  
**Goal:** Set up a professional development environment for the ZED 2i camera using Anaconda.

---

## 🛑 READ THIS FIRST
We need to install specific older versions of software because the latest versions (like Python 3.14 or CUDA 12.9) **do not work** with the ZED camera yet.

**Do not deviate from these versions.**

---

## Part 1: Downloads (Get these 3 files)

Download all three files before you start installing.

1.  **NVIDIA CUDA Toolkit 12.1** (The "Math Engine")
    * **Why:** The camera needs this to do AI calculations on your GPU.
    * **Download:** [Click Here for CUDA 12.1 Archive](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Windows&target_arch=x86_64&target_version=11&target_type=exe_local)
    * *Note:* Select "Windows" -> "x86_64" -> "11" -> "exe (local)".

2.  **ZED SDK 5.1** (The "Camera Drivers")
    * **Why:** These are the official drivers from Stereolabs.
    * **Download:** [Click Here for ZED SDK](https://www.stereolabs.com/developers/release/)
    * *Note:* Look for **ZED SDK for Windows 10/11 (CUDA 12)**.

3.  **Anaconda Distribution** (The "Python Manager")
    * **Why:** This creates a safe "bubble" for your code so it doesn't break your computer's main Python.
    * **Download:** [Click Here for Anaconda Installer](https://www.anaconda.com/download)
    * *Note:* Download the Windows Graphical Installer.

---

## Part 2: Installation (Follow Exact Order)

### Step 1: Install CUDA 12.1
1.  Double-click the CUDA installer you downloaded.
2.  It will ask to "Extract". Click **OK**.
3.  When the big NVIDIA screen appears, check the **Agree** box.
4.  Select **Express (Recommended)**.
5.  Wait for it to finish and close it.

### Step 2: Install ZED SDK
1.  Double-click the `ZED_SDK_...exe` file.
2.  **Important Question:** "CUDA 12.x not found. Do you want to install it?"
    * **Action:** If you just did Step 1, it might skip this. If it asks, say **No** (since you already installed 12.1).
3.  **CRITICAL QUESTION:** "Do you want to install the Python API?"
    * **Action:** **UNCHECK THIS BOX (NO).**
    * *Why?* The installer is not smart enough to find our Anaconda environment. We will do this manually later.
4.  Let the installation finish.

### Step 3: Install Anaconda
1.  Run the Anaconda installer.
2.  Click **Next** -> **I Agree** -> **Just Me** -> **Next**.
3.  Finish the installation.

### Step 4: RESTART YOUR COMPUTER
**Do not skip this.** Windows needs to register the new NVIDIA drivers. Restart now.

---

## Part 3: Setting Up Your Environment

Now we create the "safe bubble" (Conda Environment) for your project.

1.  Press the **Windows Key**, type `Anaconda Prompt`, and press **Enter**.
2.  You will see a black window. Type the following commands one by one (press Enter after each):

### Command A: Create the environment**
(We specifically ask for Python 3.10, which is compatible with ZED)
```bash
conda create -n zed_env python=3.10 -y

**Command B: Activate the environment (This enters the bubble. You must do this every time you work!)**

In your Anaconda Prompt, run:

```bash
conda activate zed_env
```

You should see `(zed_env)` appear on the left side of your command line prompt.

## Command C: Install Basic Tools

While in the activated environment, install the necessary Python packages:

```bash
pip install numpy opencv-python requests
```

## Part 4: The "Bridge" (Linking ZED to Conda)
We need to tell your new Conda environment where the ZED drivers are located.

1. In the same Anaconda Prompt (with the environment activated), navigate to the ZED installation folder:

   ```bash
   cd "C:\Program Files (x86)\ZED SDK"
   ```

2. Run the connection script (get_python_api.py-official script that already exists inside the ZED SDK folder you installed earlier-When this file is executed, it goes to the internet and fetches the specific "translator" file (called a .whl file) that allows the environment to talk to the sdk drivers):

   ```bash
   python get_python_api.py 
   ```

   **What you should see:**
   ```
   Detected platform: win_amd64, Python 3.10 ... Successfully installed pyzed-5.1
   ```

If you see the success message, you are done with the installation!

## Part 5: Testing Your Setup
Create a folder on your Desktop called ZED_Project.

Create a file named hello_zed.py inside it with this code:
To run it, open Anaconda Prompt and type:

    ```bash
    conda activate zed_env
    cd %USERPROFILE%\Desktop\ZED_Project
    python hello_zed.py
    ```
## Part 6: Live Depth View:

Before writing more Python, let’s verify the camera's 3D capabilities using the tools you already installed.

Press Windows Key.

Type ZED Depth Viewer and open it.

What to look for:

You should see a live video feed.

Click on "Depth" (top left) or "3D View".

Move your hand in front of the camera. You should see it glow different colors based on how close it is (Red = Close, Blue = Far).

If this works, your hardware is 100% perfect. Close the app and let's code
