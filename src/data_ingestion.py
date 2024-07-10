import logging
import splitfolders
import requests

logging.basicConfig(
    filename= 'data_ingestion_logs.log',
    level= logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)


split_ratio = (0.7, 0.2, 0.1)


# Use the praw (Reddit API)
