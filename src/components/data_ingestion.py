import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from exception import CustomException
from logger import logging
from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig
from model_trainer import ModelTrainerConfig
from model_trainer import ModelTrainer
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass