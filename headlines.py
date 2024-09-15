# headlines.py
#
import feedparser
import time
import sys
from datetime import datetime
import pytz

# Define the RSS feed URL
rss_url = "https://www.nu.nl/rss/Algemeen"

# Parse the RSS feed and get the headline text and link for each entry
feed = feedparser.parse(rss_url)
headlines = [(entry.title, entry.link) for entry in feed.entries]

# Define a set to store the previous headlines
previous_headlines = set()

while True:
    # Parse the RSS feed and get the headline text and link for each entry
    feed = feedparser.parse(rss_url)
    new_headlines = [(entry.title, entry.link) for entry in feed.entries if entry.title not in previous_headlines]

    # Display the new headlines with a bullet point, timestamp, and link in front of each line
    for headline, link in new_headlines:
        timestamp = datetime.now(pytz.timezone('CET')).strftime("%H:%M:%S")
        print("{0} - {1} - {2}".format(timestamp, headline, link))
        # time.sleep(1)

    # Add the new headlines to the set of previous headlines
    previous_headlines.update([title for title, link in new_headlines])

    # Wait 120 seconds before checking for new headlines again
    time.sleep(120)
