# lala



# How to start

Clone project

```
git clone https://github.com/pythondigest/vulyk-pythondigest
```

Create `virtualenv` and install dependencies:

```
virtualenv --python=python3 ./env
source ./env/bin/activate
cd vulyk-pythondigest
pip install -r requirements.txt
```



Init database and install some fixtures:

```
python control.py init pythondigest_moderator_task
7z e ./dataset/example_dataset.7z 
python control.py db load pythondigest_moderator_task --batch 01_pythondigest "./8bc7b.json" 
```



Runserver:

```
python run.py
```