"""
index (main) view.

URLs include:
/
"""
import flask
from markupsafe import escape
import search
from pyserini.search import SimpleSearcher
import pandas as pd

@search.app.route('/')
def show_index():
    """Display / route."""
    # print(flask.request.args)
    if not flask.request.args:
        return flask.render_template("index.html")

    query = flask.request.args.get("q", type=str)
    print(query)

    # Put our model below
    CUSTOMIZE_BM25 = True
    QUERY_EXPANSION = False

    # Parameters for BM25
    BM25_k1 = 0.9 
    BM25_b = 0.4

    # Parameters for RM3 query_expansion
    RM3_fb_terms = 10 # number of expansion terms.
    RM3_fb_docs = 10 # number of expansion documents.
    RM3_original_query_weight = 0.5 # weight to assign to the original query.

    searcher = SimpleSearcher('indexes/')

    if CUSTOMIZE_BM25:
        searcher.set_bm25(BM25_k1, BM25_b)
    if QUERY_EXPANSION:
        searcher.set_rm3(RM3_fb_terms, RM3_fb_docs, RM3_original_query_weight, True)

    hits = searcher.search(query)

    results = []
    data_filename = search.app.config['DATA_FILENAME']
    df = pd.read_csv(data_filename)
    base_URL = "http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID="
    for i in range(10):
        row = df[df.id == hits[i].docid].iloc[0]
        # print(row['Title'])
        results.append({"url": base_URL + row['id'], "title": row['Title']})
        # print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')


    context = {"results": results, "query": query}
    return flask.render_template("results.html", **context)

@search.app.route("/id/<id>")
def record(id):
   # TODO: check id exists in db
   return flask.render_template("record.html", id=escape(id))

