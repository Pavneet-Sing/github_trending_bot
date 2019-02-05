Github-Trending-Bot
-------------------
A scrappy project for demonstration and educational purposes. For more information read [Github terms of service for scrapping.](https://help.github.com/articles/github-terms-of-service/#5-scraping)


Scrapy Topics
-------------
- Data Extraction
- Xpath and CSS
- Rule
- Settings
- Item and Data Storage

Extracted data files
--------------------
Github-Trending-Bot will extract the URL and description of trending data. The collected data is stored using below commands:

    scrapy crawl GithubTrendingRepoCrawler -o extracted_data_files/links_CVS.cvs
    scrapy crawl GithubTrendingRepoCrawler -o extracted_data_files/links_JSON.json
    scrapy crawl GithubTrendingRepoCrawler -o extracted_data_files/links_XML.xml

and available at:

[CSV](extracted_data_files/links_CSV.csv "CSV data")
[Json](extracted_data_files/links_JSON.json "JSON data")
[XML](extracted_data_files/links_XML.xml "XML data")

Spiders
-------
    $ scrapy list
    GithubTrendingRepo
    GithubTrendingRepoCrawler

- GithubTrendingRepo: Demonstrate CSS, Xpath and LinkExtractor using regex.
- GithubTrendingRepoCrawler: Demonstrate recursive approach to extract data and description from extracted link.

Execute Spiders
---------------
Use the `scrappy crawl` command to execute project and particular spider:

    $ scrapy crawl GithubTrendingRepoCrawler

Run the particular spider using `runspider` command:

    $ scrapy runspider github_trending_bot/spiders/GithubTrendingRepo.py

License
-------
[MIT](LICENSE)