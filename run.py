"""main run file"""

import praw
from twilio.rest import Client
def automation(subreddit):
    """main run funciton"""
    keywords = ['cherry', 'mx', 'red']
    account_sid = 'AC71e3a0aa9d3be350e856f929966cc40e'
    auth_token = '87b67a1a7b988771ae74d4445e954fb8'
    comment_stream = subreddit.stream.comments(pause_after=-1)
    submission_stream = subreddit.stream.submissions(pause_after=-1)
    comment_stream_title = comment_stream.title.lower()
    submission_stream_title = submission_stream.title.lower()
    # for submission in reddit.subreddit('all').stream.submissions():

    while True:
        for comment in comment_stream:
            if comment is None:
                break
            elif all(x in comment_stream_title for x in keywords):
                twilio_sns(account_sid, auth_token, keywords, submission=None,
                           comment=None)
        for submission in submission_stream:
            if submission is None:
                break
            elif all(y in submission_stream_title for y in keywords):
                twilio_sns(account_sid, auth_token, keywords, submission=None,
                           comment=None)


def twilio_sns(account_sid, auth_token, keywords, submission, comment):
    client = Client(account_sid, auth_token)
    """
    possibilites:
    
    -no submission of comment
    - submission
    -comment
        
    """
    if submission is None and comment is None:
        pass
    elif submission and not comment:
        message = client.messages.create(
            body="Hey, it's your bot. The items " + ', '.join(keywords) +
                 'have recently been mentioned on' + subreddit.display_name +
            ' under the thread ' + submission.title,
            from_='+16043734540',
            to='+16478634626'
                                        )
        return message.sid

    elif comment and not submission:
        comment_thread_title = comment.submission.title
        message = client.messages.create(
            body="Hey, it's your bot. The items " + ', '.join(keywords) +
                 'have recently been mentioned on' + subreddit.display_name +
            ' under the thread ' + comment_thread_title,
            from_='+16043734540',
            to='+16478634626'
                                        )
        return message.sid


if __name__ == '__main__':
    reddit = praw.Reddit(client_id='OYrnA4NEhz22ug',
                         client_secret='Xb8ObUWFsvdCZDEDGYsiEhL-21c',
                         password='biboscape',
                         user_agent='bot by /u/theyoungkai',
                         username='theyoungkai'
                         )
    subreddit = reddit.subreddit('bapcsalescanada')
    automation(subreddit)

