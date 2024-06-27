# Makefile for running the Google News scraper


.PHONY: install
install:
	pip install poetry==1.8.2
	poetry install


.PHONY: scrape
scrape:
	@if [ -z "$(TOPIC)" ]; then \
		echo "Error: An ID of a topic to scrape is required. Use make scrape TOPIC=<topic_id>"; \
		exit 1; \
	else \
		poetry run python -m google_news_scraper --topic=$(TOPIC); \
	fi
