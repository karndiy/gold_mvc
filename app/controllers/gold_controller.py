from flask import Blueprint, jsonify, request, render_template
from app.scraper.gold_scraper import scrape_gold_data,cjson_pythonanywhere
from app.models.gold_model import insert_gold_data, get_all_gold, get_latest_asdate

gold_bp = Blueprint('gold', __name__)

@gold_bp.route('/')
def home():
    data = get_all_gold()
    return render_template('index.html', data=data)

@gold_bp.route('/scrape', methods=['GET'])
def scrape():
    data = scrape_gold_data()
    if not data:
        return jsonify({'error': 'Failed to scrape data'}), 500

    inserted = insert_gold_data(data)
    if inserted:
        return jsonify({
            'message': f'{len(inserted)} new records inserted.',
            'data': inserted
        }), 201
    else:
        return jsonify({'message': 'No new data to insert.'}), 200

@gold_bp.route('/api/gold', methods=['GET'])
def api_gold():
    golds = get_all_gold()
    return jsonify([g.to_dict() for g in golds])

@gold_bp.route('/api/gold_date', methods=['GET'])
def api_latest_asdate():
    gold = get_latest_asdate()
    if gold:
        return jsonify(gold.to_dict())
    else:
        return jsonify({'message': 'No gold price data found'}), 404
    
@gold_bp.route('/api/sendjson', methods=['GET', 'POST'])
def api_senddata():
    data =  cjson_pythonanywhere()
    if data:
        return jsonify(data)
    else:
        return jsonify({'message': 'Not Save data json'}), 404



