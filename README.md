# Scraping Google News

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

## Google News Scraper

A free tool for scraping articles from Google News. 

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

`make install`

### Usage

This tool is used to scrape Google News articles based on the topic they're listed in. 

First of all, go to [Google News](https://news.google.com/) and select a topic, such as U.S., World, Sports, etc.

Look at the URL in your browser and copy the string of characters that come after `/topics/`, that's your topic ID.

For example, in this URL:

`https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE?hl=en-US&gl=US&ceid=US%3Aen` 

The topic ID would be `CAAqIggKIhxDQkFTRHdvSkwyMHZNRGxqTjNjd0VnSmxiaWdBUAE`.

Scrape articles from your selected topic by running:
`make scrape TOPIC_ID=<your_selected_topic_id>`

After running, you should see a file named `articles.csv`. 

The data should look something like this:

| title          | url                               |
|----------------|-----------------------------------|
| First Article  | https://news.google.com/articles/ |
| Second Article | https://news.google.com/articles/ |


### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs Scraper API.

## Oxylabs Google News API

You can get a [7-day trial for Oxylabs Google News API](https://oxylabs.io/products/scraper-api/serp/google/news) and get **free 5K results**.  The tool will deliver a list of **sources, titles, URLs, and dates from published articles** all over the Google News portal. This API returns real-time data and gives access to localized results, all while avoiding blocks. 

After you claim your trial, using Google News API consists of three main steps:
1. Create your API user via our [dashboard](https://dashboard.oxylabs.io)
2. Send a request
3. Retrieve the data in JSON or HTML

### Request sample
In the example below, we use Google News API and make a request to collect search result pages for the search term `adidas` on the `google.nl` domain: 

```
import requests
from pprint import pprint

# Structure payload.
payload = {
    'source': 'google_search',
    'domain': 'nl',`
    'query': 'adidas',
    'parse': True,
    'context': [
        {'key': 'tbm', 'value': 'nws'},
    ],
}

# Get response.
response = requests.post(
    'https://realtime.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'),
    json=payload,
)

# Print prettified response to stdout.
pprint(response.json())
```

To see **request samples in other languages** and **parameter values** along with their **descriptions**, please take a look at our extensive [Google News API documentation](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/google/news-search). 
