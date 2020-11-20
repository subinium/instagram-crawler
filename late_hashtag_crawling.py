from crawler import output
from inscrawler.fetch import fetch_details
from inscrawler.browser import Browser
import pandas as pd
import json
import argparse


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Instagram Crawler")

    parser.add_argument("-st", "--start", type=int, default=0)
    parser.add_argument("-ed", "--end", type=int, default=10)
    parser.add_argument("-s", "--save", type=int, default=0)

    args = parser.parse_args()
    st, ed = args.start, args.end
    save = args.save
    posts = []
    browser = Browser(False)
    print(f'Start Crawling #{st} to #{ed}')
    data = pd.read_csv('./jeju.csv')
    for idx in range(st, ed):
        key = data['key'][idx]
        dict_post = {"key": key}
        if idx % 100 == 0:
            percentage = (idx - st + 1) / (ed - st) * 100
            print(
                f'> End : #{idx} ({percentage:.2f})\r', end='')

        if save and idx and idx % save == 0:
            pd.DataFrame(posts).to_csv(f'{st}_{idx}.csv', index=False)

        fetch_details(browser, dict_post)
        posts.append(dict_post)

    pd.DataFrame(posts).to_csv(f'{st}_{ed}.csv', index=False)
