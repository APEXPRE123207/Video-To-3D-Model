# 📦 From Video to 3D Model – Setup Guide

## Project Description

This project was undertaken as part of a Summer Internship at **Garden Reach Shipbuilders and Engineers Ltd (GRSE)**. The repository provides a comprehensive, step-by-step pipeline for converting a video of a real-world object into a detailed 3D model using state-of-the-art photogrammetry and neural rendering techniques.

The workflow leverages [COLMAP](https://colmap.github.io/) for camera pose estimation and structure-from-motion, and [Instant-NGP](https://github.com/NVlabs/instant-ngp) for fast neural radiance field (NeRF) training and mesh extraction. The resulting 3D model can be exported and loaded into Blender or MeshLab for further analysis, including accurate volume measurement of the reconstructed object.

### Key Features

- **End-to-End Pipeline:** Automates the process from video frame extraction, camera calibration, and scene reconstruction to neural rendering and mesh export.
- **State-of-the-Art Tools:** Utilizes COLMAP for robust photogrammetric reconstruction and Instant-NGP for real-time NeRF training and mesh conversion.
- **Easy Export:** The generated 3D model can be seamlessly imported into Blender, where you can analyze, edit, and compute the object's volume.
- **Documentation \& Scripts:** Includes scripts and detailed instructions for each stage, making the process accessible for both research and industrial applications.


### Typical Workflow

1. **Video Capture:** Record a video of the target object.
2. **Frame Extraction:** Extract frames from the video for processing.
3. **Camera Pose Estimation:** Use COLMAP to estimate camera positions and reconstruct the scene geometry.
4. **NeRF Training:** Train a neural radiance field using Instant-NGP for high-quality 3D reconstruction and mesh export.
5. **Mesh Export \& Analysis:** Load the exported 3D model into Blender or MeshLab to visualize, edit, and measure properties such as volume.

### Applications

- Industrial reverse engineering
- Digital archiving of physical assets
- Rapid prototyping and design validation
- Educational and research projects in computer vision and graphics

---

**This repository demonstrates how modern AI-powered photogrammetry and neural rendering can be applied in a real-world industrial context, enabling fast, accurate, and interactive 3D modeling from simple video data.**

---

## ✅ Prerequisites

Download and install the following:


| Tool | Purpose | Download Link |
| :-- | :-- | :-- |
| Anaconda | Managing Python virtual environments | [Anaconda](https://www.anaconda.com/products/distribution) |
| CUDA Toolkit (v12.4 or compatible) | GPU support for Instant-NGP | [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) |
| CMake | Building Instant-NGP | [CMake](https://cmake.org/download/) |
| Visual Studio 2022 Community Edition | Building C++ projects | [Visual Studio](https://visualstudio.microsoft.com/vs/community/) |
| Instant-NGP | Rendering of 3D Model | [Instant-NGP](https://github.com/NVlabs/instant-ngp) |
| COLMAP | Structure-from-Motion and MVS pipeline | [COLMAP GitHub](https://github.com/colmap/colmap) |
| MeshLab | Mesh viewing and editing | [MeshLab](https://www.meshlab.net/) |


---

## 🔧 Setup Instructions

### 1. Anaconda (Recommended)
- Download and setup Anaconda.
- Create a new virtual environment with
  ```bash
  conda create -n your_env_name python==3.8
    ```
- Now download the required python libraries from the requirement.txt.
  ```bash
  conda install --file requirementsconda.txt
  pip install -r requirementspip.txt
  ```

### 2. CUDA Installation

- Launch the CUDA installer and choose **Custom Installation**.
- Select only:
    - CUDA Toolkit
    - CUDA Compiler
    - CUDA Visual Studio Integration
    - Development
- After installation, verify with:

```bash
nvcc --version
```

---

### 3. Visual Studio Setup

Install **Visual Studio 2022 Community Edition** with the following components:

- Desktop development with C++
- MSVC v143 - VS 2022 C++ x64/x86 build tools
- C++ CMake tools for Windows
- Windows SDK (choose based on your OS):
    - Windows 11 SDK (10.0.22000.0)
    - Windows 10 SDK (10.0.x)

---

### 4. Instant-NGP Installation \& Build

Clone and build Instant-NGP:

```bash
git clone --recursive https://github.com/NVlabs/instant-ngp
cd instant-ngp
```

**Using CMake GUI:**

- Source: `C:/path/to/instant-ngp`
- Build: `C:/path/to/instant-ngp/build`
- Click **Configure** → Choose *Visual Studio 17 2022* → Finish
- Click **Generate** → Open Project

**In Visual Studio:**

- Set to **Release Mode**
- Go to *Build > Build Solution*

**Alternative Command Line Build:**

```bash
cd C:\path\to\instant-ngp\build
cmake --build . --config RelWithDebInfo
```


---
## Convert Video to 3D Model  
### 1. Copy the files
- After downloading and installing the [Instant-NGP](https://github.com/NVlabs/instant-ngp) project, copy and paste the current project files into the Instant-NGP directory:
* [video_to_frames](video_to_frames.py)
* [video_to_COLMAP](video_to_COLMAP.py)
* [visualize_COLMAP_output](visualize_COLMAP_output.py)
* 
### 2. Run [video_to_COLMAP.py](video_to_COLMAP.py)

- You will be asked for the path to the source video file.
-You will be given the current fps of the video the total number of frames, and be asked for the preferred frame sample rate per second - for example: 2 fps. (Recommended - 1 frame/second)
- Type `y` to view the COLMAP graph (optional).
- The generated `transforms.json` will be saved in your current working root directory (i.e. if current working directory is W:\Project\.. it will get stored in W:).

---

### 3. Prepare Instant-NGP Scene

- Copy `transforms.json` into:

```
instant-ngp/build/instant-ngp/data/v2obj/ (Only if you built instant-ngp inside the original folder )
```

- Ensure the following files are inside the `v2obj` folder:
    - Frame images (from video)
    - `transforms.json`
    - `correction1.py`
    - `correction2.py`
- Run the correction scripts:

```bash
python correction1.py
python correction2.py
```


---

### 4. Launch Instant-NGP Viewer

From Anaconda Prompt, run:

```bash
.\instant-ngp.exe --scene "path\to\instant-ngp\data\v2obj"
```


### 5. From rendered scene into 3D (.STL) object - Instant-ngp and MeshLab:
- To extract a 3D object from the rendered scene - follow [Export 3D Object from Nvidia (instant-ngp) NeRF and load it into Blender and MeshLab](https://www.youtube.com/watch?v=55XKtYOIB7Y)
This video demonstrates how to use the Instant-NGP built-in API to produce a 3D object from the scene.


---
## Purpose of each file

| File Name | Purpose |
| :-- | :-- |
| `video_to_frames.py` | Extracts frames from video as images |
| `video_to_COLMAP.py` | Orchestrates the full pipeline: extraction, COLMAP, and visualization |
| `visualize_COLMAP_output.py` | Visualizes camera positions/orientations from COLMAP output |
| `correction1.py` | Fixes image paths in `transforms.json` for Instant-NGP compatibility |
| `correction2.py` | Verifies that image files are valid and not corrupted |


---

## 🧩 Troubleshooting / FAQ

**CMake cannot find CUDA**

- Go to *System Properties > Environment Variables*
- Under *System Variables*, click **New**:
    - Variable name: `CUDAToolkit_ROOT`
    - Variable value: `C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v12.4`
- Restart your terminal or Visual Studio.

**CMake Error at fmt/CMakeLists.txt:234**

If you see:

```
target_compile_features no known features for CXX compiler "MSVC"
```

Run:

```bash
git submodule update --init --recursive
```

Ensure the following structure exists:

```
instant-ngp/
└── dependencies/
    └── tiny-cuda-nn/
        └── dependencies/
            └── fmt/
                └── CMakeLists.txt
```


---

## 🧠 Notes

- This pipeline is optimized for GPU-based rendering.
- Ensure you have a compatible NVIDIA GPU with CUDA support.
- Use `RelWithDebInfo` for faster runtime and debugging support.
- Feel free to suggest improvements or raise issues via GitHub.

---

**Happy 3D modeling! 🧊📹🧠**

