# 3dmmDotComScraper
Scrapes recent movies from 3dmm.com's New Release section into a movie.json file.

Based on [Scrapy](http://doc.scrapy.org/en/latest/) and [Docker](https://www.docker.com/).

Example use:

    docker build -t foone/scraper .
    docker run -v $(readlink -f threedmmcom):/threedmmcom foone/scraper bash -c "cd /threedmmcom && scrapy crawl s3dmmcom"
