"""main run file"""
# import necessary dependencies
import praw
from twilio.rest import Client
def automation(subreddit):
    """main run funciton"""
    keywords = ['cherry','mx','red']
    account_sid = 'AC71e3a0aa9d3be350e856f929966cc40e'
    auth_token = '87b67a1a7b988771ae74d4445e954fb8'
    # comment_stream = subreddit.stream.comments(pause_after=-1)
    # submission_stream = subreddit.stream.submissions(pause_after=-1)
    # comment_stream_title = comment_stream.title.lower()
    # submission_stream_title = submission_stream.title.lower()
    for submission in subreddit.stream.submissions(skip_existing=True):
        if all(x in submission.selftext for x in keywords) or all(y in submission.title for y in keywords):
            twilio_sns(account_sid, auth_token, keywords, submission=None,
                       comment=None)



    # do something with submission


def twilio_sns(account_sid, auth_token, keywords, submission, comment):
    """
    possibilites:

    -no submission of comment
    - submission
    -comment

    """
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+16478634626",
        from_="+16043734540",
        body="salutations nigger")
    print(message.sid)


if __name__ == '__main__':
    reddit = praw.Reddit(client_id='OYrnA4NEhz22ug',
                         client_secret='Xb8ObUWFsvdCZDEDGYsiEhL-21c',
                         password='biboscape',
                         user_agent='bot by /u/theyoungkai',
                         username='theyoungkai'
                         )
    subreddit = reddit.subreddit('bapcsalescanada')
    automation(subreddit)



