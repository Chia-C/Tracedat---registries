Tracedat Registries Program

Overview

The Tracedat Registries Program is designed to automate interactions with the Spanish Corporate Registry website. This program offers functionalities for requesting a "Nota Informativa Mercantil" and submitting a "Depósito de Cuentas".

Getting Started

Prerequisites

Before running the program, ensure you have the following installed on your system:

Windows Operating System
Google Chrome browser
Python environment with the selenium library(This is required when running the source code. If you are running GUI.exe, this is not necessary)

To install Selenium, run the following command in your command prompt or terminal:

pip install selenium

Setup
1. Unzip the Program:
Unzip the Tracedat-registries-Program.zip file to your desired location.

2. Accessing the Program:
Navigate through the folders to locate the executable file:

Go to the Assessment folder.
Click on the RegistroMercantil folder.
Run the program by clicking on GUI.exe.lnk.

Alternatively, you can:

Go to the GUI folder.
Run the program by clicking on GUI.exe.

Learning How to Use the Program
Before using the program, you can refer to the provided demo files for guidance:

Watch the Tracedat-registries-demo.mp4 video.
Read the Tracedat-registries-demo.pdf document.

These files will give you a detailed overview of the functionalities and how to operate the program.

Data Management

Information regarding data management can be found in the data.txt file within the unzipped folder. Note that this project does not involve the use of a database.

Source Code

The source code for the project is available in the Tracedat-registries-source.zip file. You can extract and review the code if necessary.

Usage

The program provides a graphical user interface (GUI) to interact with the functionalities. Upon running the GUI.exe, follow these steps:

1. Nota Informativa Mercantil:

Enter the company's name.
Provide a reference text.
Optionally, refine your search by selecting a registry.
Check the option to use a captcha solver if needed.
Click "Solicitar" to submit the request.

2.Depósito de Cuentas:

Enter the company's name.
Provide a reference text.
Optionally, refine your search by selecting a registry.
Enter the fiscal year (Ejercicio).
Check the option to use a captcha solver if needed.
Click "Solicitar" to submit the request.

Notes
Ensure your Chrome browser is up-to-date to avoid compatibility issues with Selenium.
Follow the instructions in the demo files for a smooth user experience.