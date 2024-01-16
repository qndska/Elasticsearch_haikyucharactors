from flask import Flask, request, render_template
from elasticsearch import Elasticsearch
import math

es = Elasticsearch("https://localhost:9200", http_auth=("elastic", "test123"), verify_certs=False)
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    page_size = 10
    keyword = request.args.get('keyword')
    if request.args.get('page'):
        page_no = int(request.args.get('page'))
    else:
        page_no = 1

    body = {
    "query": {
        "function_score": {
            "query": {
                "multi_match": {
                    "query": keyword,  # Specify the query term here
                    "fields": ["name^13", "AKA^12", "gender^11", "birthday^10", "age^9", "height^8", "weight^7", "occupation^6", "team^5", "number^4", "position^3", "personality^2", "background^1"],
                    "fuzziness": "AUTO",
                    "lenient": True
                }
            },
            "score_mode": "sum"
        }
    }
}

    res = es.search(index='characters', body=body)
    hits = [{'PIC': doc['_source']['PIC'], 'name': doc['_source']['name'], 'AKA': doc['_source']['AKA'], 'gender': doc['_source']['gender'], 'birthday': doc['_source']['birthday'],
             'age': doc['_source']['age'], 'height': doc['_source']['height'], 'weight': doc['_source']['weight'], 'occupation': doc['_source']['occupation'],
             'team': doc['_source']['team'], 'number': doc['_source']['number'], 'position': doc['_source']['position'], 'personality': doc['_source']['personality'], 'background': doc['_source']['background']} for doc in res['hits']['hits']]
    page_total = math.ceil(res['hits']['total']['value'] / page_size)
    return render_template('search.html', keyword=keyword, hits=hits, page_no=page_no, page_total=page_total)
