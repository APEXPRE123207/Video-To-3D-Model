<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# 📦 From Video to 3D Model – Setup Guide

This repository provides a step-by-step guide to convert a video into a 3D object using [Instant-NGP](https://github.com/NVlabs/instant-ngp), [COLMAP](https://colmap.github.io/), and supporting tools.

---

## ✅ Prerequisites

Download and install the following:


| Tool | Purpose | Download Link |
| :-- | :-- | :-- |
| CUDA Toolkit (v12.4 or compatible) | GPU support for Instant-NGP | [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) |
| Visual Studio 2022 Community Edition | Building C++ projects | [Visual Studio](https://visualstudio.microsoft.com/vs/community/) |
| CMake | Building Instant-NGP | [CMake](https://cmake.org/download/) |
| COLMAP | Structure-from-Motion and MVS pipeline | [COLMAP GitHub](https://github.com/colmap/colmap) |
| Anaconda | Managing Python virtual environments | [Anaconda](https://www.anaconda.com/products/distribution) |
| MeshLab | Mesh viewing and editing | [MeshLab](https://www.meshlab.net/) |


---

## 🔧 Setup Instructions

### 1. CUDA Installation

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

### 2. Visual Studio Setup

Install **Visual Studio 2022 Community Edition** with the following components:

- Desktop development with C++
- MSVC v143 - VS 2022 C++ x64/x86 build tools
- C++ CMake tools for Windows
- Windows SDK (choose based on your OS):
    - Windows 11 SDK (10.0.22000.0)
    - Windows 10 SDK (10.0.x)

---

### 3. Instant-NGP Installation \& Build

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

### 4. Run `video_to_COLMAP.py`

- Set the path to your video and desired frame count (recommended: 1 frame/sec).
- Type `y` to view the COLMAP graph (optional).
- The generated `transforms.json` will be saved in your current working directory.

---

### 5. Prepare Instant-NGP Scene

- Copy `transforms.json` into:

```
instant-ngp/build/instant-ngp/data/v2obj/
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

### 6. Launch Instant-NGP Viewer

From Anaconda Prompt, run:

```bash
.\instant-ngp.exe --scene "path\to\instant-ngp\data\v2obj"
```


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

