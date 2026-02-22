# ML-based Heart Rate Anomaly Detector for RISC-V

This repository contains a machine learning-based heart rate anomaly detection application designed to run on a custom RISC-V processor. It demonstrates how wearable AI applications can leverage a general-purpose RISC-V CPU. This low-power, wearable heart-rate anomaly detector designed to predict expected resting heart rate using age, gender, and measured heart rate as inputs. A simple linear regression model trained in Python estimates the expected resting heart rate, and an anomaly threshold is defined to detect deviations. To make the model FPGA-friendly, it is converted to fixed-point representation, avoiding slow and power-hungry floating-point operations, enabling efficient real-time implementation on a RISC-V processor for wearable applications.

## Features
- Load and preprocess heart rate dataset (`Medicaldataset.csv`)
- Linear regression-based model to detect heart rate anomalies
- Interactive anomaly checker for user inputs
- Fixed-point model implementation for RISC-V integration
- Visual regression plots for sanity checking
- Assembly program for running detection on RISC-V core
- Designed for wearable AI and embedded applications


## Author
- **Afroz Sahar** — Electrical (Electronics & Communications) Engineer
- **Focus:** RISC-V, Digital Design, FPGA, Embedded Systems, Computer Architecture, RTL Design, VLSI Circuit Design, Hardware/Software Co-Design, Application-specific processor, Machine learning, AI
