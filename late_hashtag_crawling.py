from crawler import output
from inscrawler.fetch import fetch_details
from inscrawler import InsCrawler
import pandas as pd
import json
import argparse
from time import sleep


def get_posts_by_keys(keys, save, path, debug=False):
    ins_crawler = InsCrawler(has_screen=debug)
    return ins_crawler.get_posts_by_keys(keys, save, path)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Instagram Crawler")

    parser.add_argument("-st", "--start", type=int, default=0)
    parser.add_argument("-ed", "--end", type=int, default=10)
    parser.add_argument("-s", "--save", type=int, default=100)

    args = parser.parse_args()
    st, ed = args.start, args.end
    save = args.save
    wait_time = 1.5
    posts = []
    print(f'Start Crawling #{st} to #{ed}')
    data = pd.read_csv('./jeju.csv')

    output(
        get_posts_by_keys(
            data['key'][st:ed], save, f'./output_{st}_{ed}.json'), f'./output_{st}_{ed}.json'
    )
