# rehaB
Uncommon Hacks 2020! 

Team Members: David Bukowski :confounded:, Jacky Lee :horse_racing:, Alex Sheen :runner:, Maggie Zhao :rice_ball:

## How to Run

1. Clone this repo into your folder of choice 

    ```
    $ git clone git@github.com:mzhao3/rehaB.git
    ```

2. Now open your folder

    ```
    $ cd rehaB
    ```

3. Activate your virtual environment and upgrade `pip`  
<sup>Need a virtual environment? Follow the [instructions below](#dependencies)</sup>  

    ```
    $ . path/to/venv/bin/activate    # for Linux / OS
    $ source path/to/venv/Scripts/activate    # for Windows
    
    (venv) $ pip install --upgrade pip
    ```

4. Install the [dependencies](#dependencies) with [requirements.txt](requirements.txt) by running the following command  
<sup>It includes Flask, Wheel, *the stuff we use to keep your password safe*, *render your graphs*, and all that other good stuff!!</sup>


    ```
    (venv) $ pip install -r requirements.txt
    ```

6. Now you can run the python file (starting the Flask server)

    ```
    (venv) $ python app.py
    ```

7. Now type one of these into your browser of choice and start using Ambrosia!  
<sup>or copy and paste</sup>

    ```
    http://127.0.0.1:5000/
    http://localhost:5000/
    ```
    
## Dependencies 

Install the dependencies with [requirements.txt](requirements.txt) by running the following command

```
(venv) $ pip install -r requirements.txt
```

- venv  
`venv` is used to create an isolated environment for whatever version of Python (and whatever libraries you're installing) you're using to wreak havoc in. `venv` allows you to use different versions of Python so you don't need to worry about compatibility issues or somehow breaking your computer.  
`venv` is a standard Python library in Python 3 with no further action required. Run the following to make a virtual environment if you do not already have one: 

    ```
    $ python3 -m venv venv_name 
    ```
    
    For versions older than Python 3.0.0 run the following:  
    ```
    $ pip install virtualenv
    $ virtualenv venv_name  
    ```

- pip  
`pip` is used to install and manage Python packages. Usually comes installed with Python, check out [this page for instructions](https://pip.pypa.io/en/stable/installing/) if you find that further action is required. Remember to upgrade! 

    ```
    (venv) $ pip install --upgrade pip
    ```

- os  
`os` is used for miscellaneous operating system dependent functions. A standard Python library with no further action required.


- flask  
`flask` allows the app to be run on `localhost`, needs `wheel`. Installed with [requirements.txt](requirements.txt) 

    ```
    (venv) $ pip3 install flask
    ```
- pyphen
`pyphen` is used to count the syllables of words through hyphenation. Installed with [requirements.txt](requirements.txt) 

    ```
    (venv) $ pip3 install pyphen
    ```

- wheel  
`wheel` is needed to use `flask`. Installed with [requirements.txt](requirements.txt) 

    ```
    (venv) $ pip3 install wheel
    ```

- Jinja2  
`Jinja2` is used for templating HTML pages. Installed with [requirements.txt](requirements.txt), installed when you install `flask`

