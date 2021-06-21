import os
from . import searchManga, byUrl
import argparse
name=os.path.dirname(__file__).split('/')[-1]
parse = argparse.ArgumentParser(prog=name, description="KOMIKU DOWNLOADER")
parse.add_argument("--query", help="query")
parse.add_argument("--index", help="index number of result")
parse.add_argument('--url', help='komiku url')
parse.add_argument("--out", help="output file")
pars=parse.parse_args()
try:
    def url(res):
        do=res.download()
        print(f"title: {res.title}")
        print(f"{do.images.__len__()} url")
        out = pars.out or res.title+".pdf"
        do.generate_pdf
        do.save(out)
        print(f"SAVE AS {out}")

    if pars.url:
        url(byUrl(pars.url))
    elif pars.query and pars.index.isnumeric():
        res = searchManga(pars.query).fetch
        for i in enumerate(res):
            print(f"{i[0]}. {i[1].title}")
        assert int(pars.index) < len(res)
        url(res[int(pars.index)])
    else:
        print(f"Try `python -m {name} -h' for more information.")
except Exception:
    print(f"Try `python -m {name} -h' for more information.")

