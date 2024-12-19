# mop_concessions_dashboard

Dashboard to present the status for public work concessions in Chile.

## execution:

### 1.- Spiders

#### Spiders list

```
 /mopscrapper$ scrapy list
mop_details_spider
mopspider
```

#### Get main routes

```
scrapy crawl mopspider -O mopspider.json
```

#### Get projects info

```
scrapy crawl mop_details_spider -O mop_details_spider.json
```

### 2.- ETL

Execute /notebooks/etl_mop_details.ipynb

### 3.- Dashboard

streamlit run src/mop_dashboard.py
