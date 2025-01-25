# How to run the web server
> [!NOTE]
> If you have prior experience with using python environments and installing dependencies, you shouldn't really need this, it won't be anything new.
### 1. Virtual Environment
You need to create a python virtual to install the dependencies. You can do this by typing:
```commandline
python3 -m venv .venv
```
This will the virtual environment in the directory `.venv`.
To then source the environment, you need to run the following:
<br>Linux:
```commandline
source .venv/bin/activate
```
Windows:
```commandline
.\.venv\Scripts\activate
```
Congrats! You've created the environment.

### 2. Installing Dependencies 
Run the following:
```commandline
pip3 install -r requirements.txt
```
This will install of the required things, all form the requirements file, so you don't have to do much. 
The dependencies required by the program are `Flask` and `chess`.

### 3. Run it
Type the following:
```commandline
python3 run.py
```
From there, you should be able to run the web server. 
> [!TIP]
> Go to http://127.0.0.1:5000 in your browser, that is where the flask app will be hosted.