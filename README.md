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
1. Segment the original IMU gait signals into IMU sequences of equal length: **python "./main/main_DataSegmentation.py"**
2. Transform segmented IMU signals into hand-crafted features: **python "./main/main_IMU2ManualFeature.py"**
3. Transform segmented IMU signals into autocorrelation features: **python "./main/main_IMU2AutoCorrFeature.py"**
4. Transform segmented IMU signals into AE-GDI features: **python "./main/main_IMU2AEGDI.py"**
5. Evaluate the performance of included algorithms for soft biometrics: **python "./main/main_Benchmark.py"**
## Example Results
### Age Group Classification (IMU Location: Center)
| **Method**                          | **Age Group Classification**                 |
|:-----------------------------------:|:-----------------------------:|
| Hand\-crated Feature \+ KNN         | 82\.97\%                     |
| Hand\-crated Feature \+ NB          | 42\.20\%                     |
| Hand\-crated Feature \+ SVM         | 71\.30\%                     |
| Hand\-crated Feature \+ Ensemble    | 71\.89\%                     |
| Hand\-crated Feature \+ DT          | 44\.48\%                     |
| Hand\-crated Feature \+ DA          | 48\.93\%                     |
| Hand\-crated Feature \+ KAM         | 62\.39\%                     |
| Autocorrelation Feature \+ KNN      | 86\.72\%                     |
| Autocorrelation Feature \+ NB       | 40\.92\%                     |
| Autocorrelation Feature \+ SVM      | 73\.24\%                     |
| Autocorrelation Feature \+ Ensemble | 67\.79\%                     |
| Autocorrelation Feature \+ DT       | 43\.01\%                     |
| Autocorrelation Feature \+ DA       | 49\.06\%                     |
| Autocorrelation Feature \+ KAM      | 69\.98\%                     |
| Combined Feature \+ KNN             | **91\.86\% \(3rd\)**
| Combined Feature \+ NB              | 47\.07\%                     |
| Combined Feature \+ SVM             | 80\.90\%                     |
| Combined Feature \+ Ensemble        | 77\.35\%                     |
| Combined Feature \+ DT              | 51\.19\%                     |
| Combined Feature \+ DA              | 59\.31\%                     |
| Combined Feature \+ KAM             | 73\.92\%                     |
| AE\-GDI \+ 2D\-CNN                  | 53\.76\%                     |
| Original Signal \+ 1D\-CNN          | 57\.54\%                     |
| Original Signal \+ InceptionTime    | **95\.55\% \(1st\)**
| HYDRA                               | **92\.35\% \(2nd\)**
### Gender Estimation (IMU Location: Center)
| **Method**                          | **Gender Estimation**                 |
|:-----------------------------------:|:-----------------------------:|
| Hand\-crated Feature \+ KNN         | 88\.43\%                     |
| Hand\-crated Feature \+ NB          | 62\.83\%                     |
| Hand\-crated Feature \+ SVM         | 83\.16\%                     |
| Hand\-crated Feature \+ Ensemble    | 83\.32\%                     |
| Hand\-crated Feature \+ DT          | 67\.98\%                     |
| Hand\-crated Feature \+ DA          | 73\.12\%                     |
| Hand\-crated Feature \+ KAM         | 79\.66\%                     |
| Autocorrelation Feature \+ KNN      | 92\.65\%                     |
| Autocorrelation Feature \+ NB       | 77\.00\%                     |
| Autocorrelation Feature \+ SVM      | 86\.80\%                     |
| Autocorrelation Feature \+ Ensemble | 84\.67\%                     |
| Autocorrelation Feature \+ DT       | 75\.51\%                     |
| Autocorrelation Feature \+ DA       | 79\.77\%                     |
| Autocorrelation Feature \+ KAM      | 86\.41\%                     |
| Combined Feature \+ KNN             | **96\.48\% \(3rd\)** |
| Combined Feature \+ NB              | 71\.42\%                     |
| Combined Feature \+ SVM             | 83\.41\%                     |
| Combined Feature \+ Ensemble        | 88\.14\%                     |
| Combined Feature \+ DT              | 77\.99\%                     |
| Combined Feature \+ DA              | 82\.35\%                     |
| Combined Feature \+ KAM             | 89\.38\%                     |
| AE\-GDI \+ 2D\-CNN                  | 60\.69\%                     |
| Original Signal \+ 1D\-CNN          | 85\.42\%                     |
| Original Signal \+ InceptionTime    | **98\.69\% \(1st\)** |
| HYDRA                               | **96\.97\% \(2nd\)** |
### Age Estimation (IMU Location: Center)
| **Method**                          | **Age Estimation**        |
|:-----------------------------------:|:-------------------------:|
| Hand\-crated Feature \+ GPR         | 7\.99                     |
| Hand\-crated Feature \+ LR          | 14\.17                    |
| Hand\-crated Feature \+ SVM         | 9\.25                     |
| Hand\-crated Feature \+ Ensemble    | 10\.59                    |
| Hand\-crated Feature \+ DT          | 12\.91                    |
| Hand\-crated Feature \+ KAM         | 10\.41                    |
| Autocorrelation Feature \+ GPR      | **6\.98 \(3rd\)**         |
| Autocorrelation Feature \+ LR       | 12\.86                    |
| Autocorrelation Feature \+ SVM      | 8\.82                     |
| Autocorrelation Feature \+ Ensemble | 10\.97                    |
| Autocorrelation Feature \+ DT       | 13\.21                    |
| Autocorrelation Feature \+ KAM      | 10\.17                    |
| Combined Feature \+ GPR             | **5\.58 \(2nd\)**         |
| Combined Feature \+ LR              | 16\.90                    |
| Combined Feature \+ SVM             | 7\.05                     |
| Combined Feature \+ Ensemble        | 9\.30                     |
| Combined Feature \+ DT              | 12\.18                    |
| Combined Feature \+ KAM             | 8\.43                     |
| AE\-GDI \+ 2D\-CNN                  | 16\.04                    |
| Original Signal \+ 1D\-CNN          | 16\.59                    |
| Original Signal \+ InceptionTime    | 19\.63                    |
| HYDRA                               | **0\.46 \(1st\)**         |
### Contact
If you have any questions, please feel free to contact me through email (shuoli199909@outlook.com)!
## Authors and acknowledgment
This master thesis was supervised by Dr. Mohamed Elgendi (ETH Zurich), Prof. Dr. Carlo Menon (ETH Zurich), and Prof. Dr. Rosa Chan (City University of Hong Kong). The code was developed by Shuo Li. Also thank to all my colleagues and providers of datasets for the continuous help!
## License - MIT License.
