# Create Flask Application/Deploy on Heroku
## Create Virtual Envornment with conda
```
conda create -n yourenvname python=x.x anaconda
# conda create -n pycaret python=3.6 anaconda
```
1. check conda envornment list
```
conda env list
conda activate <yourenvname>
```

## Create virtual Envronment with **virtualenv**
1. `pip install virtualenv`
2. `python3 -m venv <yourenvname>`<br>
    `python3 -m venv flaskapp`
    * Activate in Windows operating system
    ```
    .\<yourenvname>\Scripts\activate
    ```
    * Activate in Ubuntu
    ```
    source <yourenvname>/bin/activate
    ```
    * check installed packages list `pip freeze`
## Install Required packages
```
pip install flask numpy pandas sckit-learn pickle5 gunicorn
```

### Step3: Create Flask App
1. Create **app.py** file
2. Create folder **static**
3. create folder **templates**

* app.py file
```
import pickle
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 


@app.route("/model", methods=['post','get'])
def model():
    num = np.int64(request.form['height'])
    result = loaded_model.predict([[num]])
    return f"<h1>Your Height: {num} & predicted Weight <label style='color:red'>{result[0]}</label></h1>"   

if __name__ == '__main__':
    app.run(debug=True)


```

## create *templates/index.html*
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>Height Vs Weight prediction Machine learning application</h1>

<form method="post" action="/model">
<h3>Enter your Height in CM</h3>
<input type="number" name="height">

<input type="submit" value="Predict now!">
</form>

</body>
</html>
```