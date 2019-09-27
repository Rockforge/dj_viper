import requests
from datetime import datetime

def main(query):
    engine_url = 'https://duckduckgo.com'
    params = {
        'q': query,
        'ia': 'web',
    }
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0',
    }

    res = requests.get(engine_url, params, headers=headers)
    out_file = 'search_result_{:%Y%m%d-%H%M%S}.txt'.format(datetime.now())
    out_dir = '/'

    with open(out_file, 'w') as f:
        f.write(res.text)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'query',
        help='Search term'
    )
    args = parser.parse_args()
    main(args.query)