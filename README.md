# Scraping Google News

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

- [Free Google News Scraper](#free-google-news-scraper)
    + [Prerequisites](#prerequisites)
    + [Installation](#installation)
    + [Getting the topic to scrape](#getting-the-topic-to-scrape)
    + [Scraping](#scraping)
    + [Notes](#notes)
- [Oxylabs Google News API](#oxylabs-google-news-api)
    + [Request sample](#request-sample)


## Free Google News Scraper

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

`make install`

### Getting the topic to scrape

This tool is used to scrape Google News articles based on the topic they're listed in. 

First of all, open up Google News, and look through the topics listed in the top header of the webpage. 

<img width="1388" alt="image" src="https://github.com/oxylabs/google-news-scraper/assets/44357929/c30be402-90cb-41ba-95a4-b2f63cdf5a7f">

Click on a topic you wish to scrape. 
In this example we'll be using the `Business` topic. 

Next, look at the URL in your browser and copy the string of characters that come after `/topics/`, that's your topic ID.

<img width="831" alt="image" src="https://github.com/oxylabs/google-news-scraper/assets/44357929/cc3efc01-e719-4497-80f9-45710cb47977">

In the URL shown in the screenshot, the topic ID would be `CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB`. 

Save this value, you'll need it for scraping the articles.

### Scraping 

To scrape articles from your selected topic, run this command in your terminal:
`make scrape TOPIC_ID=<your_selected_topic_id>`

With the `Business` topic ID selected before, the command should look like this:

`make scrape TOPIC_ID=CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB`

After running the command, you should see this in your terminal:

<img width="1177" alt="image" src="https://github.com/oxylabs/google-news-scraper/assets/44357929/ad3e8211-043d-40fe-87e3-89fc9fea2381">

When the tool has finished running, you should see a file named `articles.csv` in the directory you were running the tool.

If you open the generated CSV file, the data should look something like this:

<img width="1277" alt="image" src="https://github.com/oxylabs/google-news-scraper/assets/44357929/7127198e-1aa9-468d-a6e6-b989a68085f3">


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

Read More Google Scraping Related Repositories: [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How to Scrape Google Shopping Results](https://github.com/oxylabs/scrape-google-shopping), [Google Play Scraper](https://github.com/oxylabs/google-play-scraper), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights), [How To Scrape Google Images](https://github.com/oxylabs/how-to-scrape-google-images), [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)
