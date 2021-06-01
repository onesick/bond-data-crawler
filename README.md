Steps to run and create a CSV file

1. Read https://docs.scrapy.org/en/latest/intro/install.html page for installation guide.
    1-1. Try to run it in conda environment so that you don't overwirte base python
2. In the directory where scrappy is installed, run this command
    ```
    scrapy crawl first -o data.csv -t csv
    ```
    this will create a data.csv file.
3. If you want to modify the script, go to 'spiders' directory, and modify 'bond.spider.py' file