# IMU_SoftBiometrics
## Introduction
This project provides the code for the experiments of soft biometrics based on IMU gait sequences. It serves as an important part of the author's master thesis (30ECTS) in ETH Zurich.
## Summary
This project mainly comprises five parts:
1. Segmenting the original IMU gait signals into IMU sequences of equal length. (csv format)
2. Transforming the IMU sequences into hand-crafted features. (csv format)
3. Transforming the IMU sequences into autocorrelation features. (csv format)
4. Transforming the IMU sequences into AE-GDI features. (h5 format)
5. Systematically evaluating the performance of all included algorithms for soft biometrics.
## Package Requirements
- matlabengine==23.2
- numpy==1.26.4
- pandas==2.2.2
- PyYAML==6.0.1
- scikit_learn==1.4.1.post1
- scipy==1.13.1
- statsmodels==0.14.1
- torch==2.2.1+cu118
- tqdm==4.66.2
- tsai==0.3.9
## Configuration
The experiments were runned on the author's personal laptop. The configurations are provided as the reference:
- CPU: AMD Ryzen 9 5900HX with Radeon Graphics
- GPU: NVIDIA GeForce RTX 3080 Laptop GPU
- CUDA Version: 11.7
- Operating System: Microsoft Windows 11 (version-10.0.22631)
## Code Structure
```bash
IMU_SoftBiometrics
├─config
├─data
│  └─OU_ISIR_Inertial_Sensor
│      ├─manual_IMUZCenter
│      │  ├─AE_GDI
│      │  ├─data_segmented
│      │  ├─feature_autocorr
│      │  └─feature_manual
│      ├─manual_IMUZLeft
│      │  ├─AE_GDI
│      │  ├─data_segmented
│      │  ├─feature_autocorr
│      │  └─feature_manual
│      └─manual_IMUZRight
│          ├─AE_GDI
│          ├─data_segmented
│          ├─feature_autocorr
│          └─feature_manual
├─main
├─result
│  └─OU_ISIR_Inertial_Sensor
│      ├─manual_IMUZCenter
│      ├─manual_IMUZLeft
│      └─manual_IMUZRight
└─util
```

## Datasets
1. OU-ISIR Inertial Sensor Dataset: http://www.am.sanken.osaka-u.ac.jp/BiometricDB/InertialGait.html
2. OU-ISIR Similar Action Inertial Dataset: http://www.am.sanken.osaka-u.ac.jp/BiometricDB/SimilarActionsInertialDB.html
## Usage
First, activate the local environment and then set the folder containing this README file as the current folder.  
For Windows, execute: **python (...).py**  
For Linux, execute: **python3 (...).py**  
1. Transform facial videos into raw RGB traces: **python "./main/main_DataSegmentation.py"**
2. Segment the original IMU gait signals into IMU sequences of equal length: **python "./main/main_DataSegmentation.py"**
3. Transform segmented IMU signals into hand-crafted features: **python "./main/main_IMU2ManualFeature.py"**
4. Transform segmented IMU signals into autocorrelation features: **python "./main/main_IMU2AutoCorrFeature.py"**
5. Transform segmented IMU signals into AE-GDI features: **python "./main/main_IMU2AEGDI.py"**
6. Evaluate the performance of included algorithms for soft biometrics: **python "./main/main_Benchmark.py"**
### Contact
If you have any questions, please feel free to contact me through email (shuoli199909@outlook.com)!
## Authors and acknowledgment
This master thesis was supervised by Dr. Mohamed Elgendi (ETH Zurich), Prof. Dr. Carlo Menon (ETH Zurich), and Prof. Dr. Rosa Chan (City University of Hong Kong). The code was developed by Shuo Li. Also thank to all my colleagues and providers of datasets for the continuous help!
## License - MIT License.
