from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import path
import zipfile
import argparse
import logging

DATASET_SLUG = "rohitrox/healthcare-provider-fraud-detection-analysis"
EXPECTED_FILES = ['Test-1542969243754.csv',
                'Test_Beneficiarydata-1542969243754.csv',
                 'Test_Inpatientdata-1542969243754.csv',
                 'Test_Outpatientdata-1542969243754.csv',
                 'Train-1542865627584.csv',
                 'Train_Beneficiarydata-1542865627584.csv',
                 'Train_Inpatientdata-1542865627584.csv',
                 'Train_Outpatientdata-1542865627584.csv'
                ]


def setup_logging():
    """Configure logging format and level."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')