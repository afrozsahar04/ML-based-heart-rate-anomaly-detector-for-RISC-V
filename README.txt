# ML-based Heart Rate Anomaly Detector for RISC-V

This repository contains a machine learning-based heart rate anomaly detection application designed to run on a custom RISC-V processor. It demonstrates how wearable AI applications can leverage a general-purpose RISC-V CPU.

## Features
- Load and preprocess heart rate dataset (`Medicaldataset.csv`)
- Linear regression-based model to detect heart rate anomalies
- Interactive anomaly checker for user inputs
- Fixed-point model implementation for RISC-V integration
- Visual regression plots for sanity checking
- Assembly program for running detection on RISC-V core
- Designed for wearable AI and embedded applications

## Folder Structure
ml/
├── load_dataset.py
├── preprocessing.py
├── resting_hr_model.py
├── interactive_anomaly_checker.py
└── fixed_point_model.py

asm/
└── HR_anomaly_detector.asm

mem/
└── IM_HR_anomaly_detector.mem  # Optional: memory initialization for RISC-V

figures/
├── anomaly_detected_hr.jpg

README.md

## Figures

![Anomaly Detected](figures/anomaly_detected_hr.jpg)

## Author
- **Afroz Sahar** — Electrical (Telecommunication) Engineering  
- **Focus:** RISC-V, Digital Design, FPGA, Embedded Systems, Computer Architecture, RTL Design, VLSI Circuit Design, Hardware/Software Co-Design, Application-specific processor, Machine learning, AI