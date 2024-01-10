# Address Classification Model for Cairo Government

## Overview

This project implements a deep learning model to classify whether a given input address is located within the Cairo government or not. The model is deployed as part of a Django web application, providing a user-friendly interface for address classification.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Django App](#django-app)
- [test App](#test-app)


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AhmedSameh210/adress_classification.git
   cd address-classification
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage



1. Run the Django migrations:

   ```bash
   python manage.py migrate
   ```

2. Start the development server:

   ```bash
   python manage.py runserver
   ```

   The application will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Model Details

The deep learning model used for address classification is based on bidirectional lstm. It has been trained on a labeled dataset containing addresses within and outside the Cairo government area.

## Django App

The Django web application provides a simple user interface for users to input an address. The input address is then sent to the deployed deep learning model, and the result is displayed on the web page indicating whether the address is in the Cairo government or not.

## Testing using Test.py file 
```bash
   python test_script.py
   ```

