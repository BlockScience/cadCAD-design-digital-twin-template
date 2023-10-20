# cadCAD-design-digital-twin-template

## How to run it

- Option 1 (CLI): Just pass `python -m prey_predator_model`
This will generate an pickled file at `data/simulations/` using the default single run
system parameters & initial state.
    - To perform a multiple run, pass `python -m prey_predator_model -e`
- Option 2 (cadCAD-tools easy run method): Import the objects at `prey_predator_model/__init__.py`
and use them as arguments to the `cadCAD_tools.execution.easy_run` method. Refer to `prey_predator_model/__main__.py` to an example.

## File structure

```
.
├── LICENSE
├── README.md
├── SPEC.md
├── prey_predator_model: the `cadCAD` model as encapsulated by a Python Module
│   ├── __init__.py
│   ├── __main__.py
│   ├── experiment.py: Code for running experiments
│   ├── logic.py: All logic for substeps
│   ├── params.py: System parameters
│   ├── structure.py: The PSUB structure
│   └── types.py: Types used in model
├── notebooks: Notebooks for aiding in development
├── requirements-dev.txt: Dev requirements
├── requirements.txt: Production requirements
```

## What is cadCAD
## Installing cadCAD for running this repo

### 1. Pre-installation Virtual Environments with [`venv`](https://docs.python.org/3/library/venv.html) (Optional):
It's a good package managing practice to create an easy to use virtual environment to install cadCAD. You can use the built in `venv` package.

***Create** a virtual environment:*
```bash
$ python3 -m venv ~/cadcad
```

***Activate** an existing virtual environment:*
```bash
$ source ~/cadcad/bin/activate
(cadcad) $
```

***Deactivate** virtual environment:*
```bash
(cadcad) $ deactivate
$
```

### 2. Installation: 
Requires [>= Python 3.6](https://www.python.org/downloads/) 

**Install Using [pip](https://pypi.org/project/cadCAD/)** 
```bash
$ pip3 install cadcad==0.4.28
```

**Install all packages with requirement.txt**
```bash
$ pip3 install -r requirements.txt
