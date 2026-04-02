
# ZED 2i Camera Setup Guide: From Zero to Hero 🤖

Comprehensive setup guide for ZED 2i camera with CUDA, PyTorch, and YOLO integration on Windows.

---

## 🛑 Important: Version Compatibility Rule

In robotics development, **newest ≠ best**.  
This guide uses **specifically tested versions** for maximum compatibility with third-party AI libraries like PyTorch.

> ⚠️ **Do NOT upgrade versions unless you know what you're doing.**

---

## 🚀 Part 0: System Verification

Verify your system's CUDA capabilities before proceeding.

### 1️⃣ Check Maximum Supported CUDA

```bash
nvidia-smi
````

Look for:

* **CUDA Version** in the top-right corner
  *(Example: `CUDA Version: 13.0`)*

---

### 2️⃣ Check Current CUDA Toolkit

```bash
nvcc --version
```

* If command not found → Proceed to **Part 1**

---

## 📥 Part 1: Required Downloads

Download these **3 components** before installation:

| Component         | Purpose                    | Download Source      | Notes                          |
| ----------------- | -------------------------- | -------------------- | ------------------------------ |
| CUDA Toolkit 12.8 | GPU acceleration for AI    | NVIDIA CUDA Archive  | Windows → x86_64 → exe (local) |
| ZED SDK 5.2       | Camera drivers & AI models | Stereolabs Developer | Must match CUDA 12             |
| Anaconda          | Python environment manager | Anaconda.org         | Graphical Installer            |

---

## ⚙️ Part 2: Installation Sequence

### 🔹 Step 1: Install CUDA 12.8

1. Run CUDA installer → **Extract → OK**
2. Accept EULA
3. ⚠️ Select **Custom (Advanced)** *(NOT Express)*
4. ❗ **UNCHECK "Display Driver"** (to preserve current drivers)
5. Complete installation

---

### 🔹 Step 2: Install ZED SDK 5.2

1. Run `ZED_SDK_*.exe`
2. SDK will auto-detect CUDA 12.8
3. Complete installation

---

### 🔹 Step 3: Install Anaconda

1. Run installer
2. Click through:

   * Next → I Agree → Just Me → Next → Finish

---

### 🔹 Step 4: Restart Computer 🔄

> ⚠️ **DO NOT SKIP THIS STEP**
> Windows must register NVIDIA paths globally.

---

## 🐍 Part 3: Conda Environment Setup

Open **Anaconda Prompt** and run:

```bash
# Create environment (Python 3.10 is required)
conda create -n John python=3.10 -y

# Activate environment (do this every session)
conda activate John

# Install PyTorch (CUDA 12.4 compatible build)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124

# Install additional packages
pip install ultralytics pyserial numpy opencv-python
```

✅ You should see `(John)` prefix in terminal

---

## 🔗 Part 4: ZED-Python Bridge

Link ZED C++ drivers with your Conda environment:

```bash
python "C:\Program Files (x86)\ZED SDK\get_python_api.py"
```

### ✅ Expected Output

```
Detected platform: win_amd64, Python 3.10 ...
Successfully installed pyzed-5.2
```

---

## 🧪 Part 5: Basic Test

### 1️⃣ Create Project Folder

```
Desktop/ZED_Project/
```

---

### 2️⃣ Create `hello_zed.py`

```python
import pyzed.sl as sl

print("✅ ZED SDK successfully imported!")
```

---

### 3️⃣ Run Test

```bash
conda activate John
cd %USERPROFILE%\Desktop\ZED_Project
python hello_zed.py
```

---

## 🔌 Part 6: Hardware Verification

1. Connect **ZED 2i via USB 3.0**
2. Open **ZED Depth Viewer**

### ✅ Verify:

* ✔ Live video feed
* ✔ Depth map (click **Depth**)
* ✔ 3D view colors:

  * 🔴 Red = Close
  * 🔵 Blue = Far

---

## 🛠️ Troubleshooting

| Issue                | Solution                                 |
| -------------------- | ---------------------------------------- |
| `nvcc` not found     | Restart after CUDA install               |
| `pyzed` import error | Re-run `get_python_api.py` in active env |
| No depth view        | Check USB 3.0 connection                 |
| CUDA mismatch        | Use exact versions in this guide         |
