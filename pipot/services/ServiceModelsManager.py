from __future__ import print_function
import os
import sys
import importlib
import inspect
from database import Base

models_storage = './pipot/services/models.txt'

def add_models(service):
    models = get_models()
    cls_members = inspect.getmembers(importlib.import_module('pipot.services' + '.' + service + '.' + service), inspect.isclass)
    cls_info = list(filter(lambda x: Base in inspect.getmro(x[1]) and x[0] not in ('IModel', 'IModelIP'), cls_members))
    models.extend([service + '.' + name for name, _ in cls_info])
    save_models(models)

def rm_models(service):
    models = get_models()
    models = list(filter(lambda x: not x.startswith(service), models))
    with open(models_storage, 'w') as f:
        for model in models:
            print(model, file=f)

def get_models():
    with open(models_storage, 'r') as f:
        return [line.strip('\n') for line in f.readlines()]

def save_models(models):
    with open(models_storage, 'w') as f:
        for model in models:
            print(model, file=f)
