# Shopping Cart Project

[Original project description](https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/projects/shopping-cart.md)
With this application, user's will able to create a receipt based on user inputted shopping cart selections.

## PREREQUISITES
Python 3.x

## INSTALLATION

Clone or download from [GitHub source](https://github.com/sambeyda/shopping-cart),then navigate to project repository

No need to install any packages for initial usage!

## USAGE

Navigate to app folder and run the shopping cart script:

```
python app/shopping_cart.py
```

Within the script, you will be prompted to select products based on their ID. When happy with your selection, click 'DONE' to exit

## TESTING

To test, install the `pytest` package if necessary, perhaps within a virtual environment
```
pip install pytest
``` 
And invoke it from the root directory of this repository to run tests:

```py
pytest
```

##Monitor Build Status

[![Build Status](https://travis-ci.org/sambeyda/shopping-cart.svg?branch=master)](https://travis-ci.org/sambeyda/shopping-cart)