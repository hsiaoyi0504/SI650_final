"""
index (main) view.

URLs include:
/
"""
import flask
from flask import url_for
from markupsafe import escape
import search
from pyserini.search import SimpleSearcher
import pandas as pd

data = pd.read_csv("./preprocess/data_new.csv") 
ids = data['id'].tolist()


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
        results.append({"url": url_for('record', id=row['id']), "id": row['id'], "title": row['Title'], 
        "keyword": row['Keyword'], "date": row['AnnounceDate'], "instrument": row['Instrument']})
        # print(f'{i+1:2} {hits[i].docid:4} {hits[i].score:.5f}')


    context = {"results": results, "query": query}
    return flask.render_template("results.html", **context)

@search.app.route("/id/<id>")
def record(id):
   # TODO: check id exists in db
   if id in ids:
       row = data[data['id'] == id]
       related_records = data[(data['PublicationURL'] == row['PublicationURL'].values[0]) & (data['id'] != id)]['id'].tolist()
       return flask.render_template("record.html", id=escape(id),
        title=row['Title'].values[0], description=row['Description'].values[0],
        repo=row['HostingRepository'].values[0], date=row['AnnounceDate'].values[0],
        xml_url=row['AnnouncementXML'].values[0],
        doi=row['DigitalObjectIdentifier'].values[0],
        review_level=row['ReviewLevel'].values[0],
        dataset_origin=row['DatasetOrigin'].values[0],
        repo_support=row['RepositorySupport'].values[0],
        primary_submitter=row['PrimarySubmitter'].values[0],
        species_list=row['SpeciesList'].values[0],
        modification_list=row['ModificationList'].values[0],
        instrument=row['Instrument'].values[0],
        publication=row['Publication'].values[0],
        publication_url=row['PublicationURL'].values[0],
        keyword=row['Keyword'].values[0],
        related_records=related_records)
   return f"record id: {escape(id)} not found"

