# physio-calc
Perform physiological calculations and conversions, with an easy-to-use interface.

### Prerequisites 
In order to run the app, you must have the prerequisites defined in **requirements.txt** installed in your environment.

To install *PyQt5*, run one of the following commands:
~~~
pip install pyqt5
~~~

or

~~~
pip3 install pyqt5
~~~

To install *Sympy*, run the following command:
~~~
pip install sympy
~~~

### Installation and Usage
To install and use Physio Calc, you have two options.

1.) Just clone the repository to your computer and run **PhysioCalc.py** from your terminal. Alternatively, run it from an IDE of your choice, such as PyCharm.
~~~
$ python PhysioCalc.py
~~~

2.) You can download the executable from the *releases* page. It was built using PyInstaller and Python 3.6.12.

Physio Calc was developed and tested on linux (Ubuntu 20.04.1 LTS). However, if you have all requirements met, you should have no issue running it on Windows or MacOS.

### Building from source
If you wish to build an executable yourself from the source code provided you can do so as outlined here.

1.) Install PyInstaller into your environment (that also has PyQt5 and Sympy). I highly recommend making a Conda environment with those packages installed and using Python 3.6 for best results. Switch to that environment in your terminal and run the following command.
~~~
pip install pyinstaller
~~~

2.) Create a spec file in the root project directory by running the following command that will use --onefile mode, to include all files in a single executable.
~~~
pyi-makespec --onefile PhysioCalc.py
~~~

Add the following lines of code to the beginning of the **PhysioCalc.spec** file. If you do not, you will likely encounter a recursion error.
~~~
# -*- mode: python ; coding: utf-8 -*-
import sys
sys.setrecursionlimit(5000)
~~~

3.) Build the executable.
~~~
pyinstaller PhysioCalc.spec
~~~
A *build* and *dist* folder will be created. The executable is located under *dist* with the name **PhysioCalc**.

### Screenshots
![Main Menu](/screenshots/MainMenu.png)
![Nernst](/screenshots/Nernst.png)
![GHK](/screenshots/GHK.png)

### License

Copyright (C) 2020 Stuart Clayton

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
