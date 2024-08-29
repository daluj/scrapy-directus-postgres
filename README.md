# Intro

This repo is for the purpose of demonstrating how to deploy a scraper using scrapy, scrapyd, scrapydweb, a PostgreSQL database and Directus together, with docker-compose.

## How to run it on local

docker compose up --build -d

# Scrapyd Web

Go to http://localhost:5000/ and you should be able to run your spiders

# Directus

Go to http://localhost:8055/ and login with the admin user on the .env file. 

# Info

## Database

The database table structure is on database/init.sql. Create a table with the same name for each spider as the spiders save the data in this way.

## Spiders

The spiders are located in scrapyd/getexampledata/spiders.

Each spider saves it's data in it's own table as defined on scrapyd/getexampledata/pipelines.py

### exampleapidata Spider

This spider fetches data from [Chuck Norris Jokes API](https://api.chucknorris.io/), and saves the data to the database.

You can set a category attribute to the Spider to filter by category:
    `-d category=val1`

### examplewebdata Spider

This spider scraps [toscrape](https://toscrape.com/) looking for the required data and saves the data to the database. 