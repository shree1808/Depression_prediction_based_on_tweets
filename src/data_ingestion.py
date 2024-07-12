import praw
import pandas as pd
import os
import time
import logging

logging.basicConfig(
    filename= 'logs\data_ingestion_logs1.log',
    level= logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s'
)

# Creating the reddit instance
reddit = praw.Reddit(
    user_agent= True,
    client_id="",
    client_secret="",
    username = '',
    password = ''
)


submission_url = 'https://www.reddit.com/r/mentalhealth/comments/18s64uc/mental_health/'  

def fetch_1000_comments(submission_url):
    submission = reddit.submission(url=submission_url)


    submission.comments.replace_more(limit=None)
    comments_data = []
    try:

        while len(comments_data) < 3000:
            for comment in submission.comments.list():
                if len(comments_data) >= 3000:
                    break
                comments_data.append({
                    'comment_id' : comment.id,
                    'comment_body': comment.body
                    })
    except Exception as e:
        print('Error occured : {e}')
        logging.info(f'Error occured : {e}')

    return submission.title, comments_data[5:3005]  

logging.info('Started fetching data from the submission with the Reddit API!!')
submission_title, comments_data = fetch_1000_comments(submission_url)


df = pd.DataFrame(comments_data)
df['title'] = submission_title
output_dir = 'Data'
os.makedirs(output_dir, exist_ok=True)

output_file = os.path.join(output_dir, 'mentalhealth_comments.csv')
df.to_csv(output_file, index=False)

print(f"Finished extracting {len(comments_data)} comments from the submission.")
print(f"Data saved to {output_file}")
