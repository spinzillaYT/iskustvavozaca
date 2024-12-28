from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/cars_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    models = db.relationship('Model', backref='brand', lazy=True)

class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year_start = db.Column(db.Integer, nullable=False)
    year_end = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    engines = db.relationship('Engine', backref='model', lazy=True)
    pros = db.Column(db.JSON, default=list)
    cons = db.Column(db.JSON, default=list)
    rating = db.Column(db.Integer)
    description = db.Column(db.Text)
    reliability = db.Column(db.Integer)  # 1-100
    comfort = db.Column(db.Integer)      # 1-100
    performance = db.Column(db.Integer)  # 1-100
    running_costs = db.Column(db.Integer) # 1-100

class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)  # benzin, dizel, hibrid, elektro
    displacement = db.Column(db.Float, nullable=False)  # in liters
    power = db.Column(db.Integer, nullable=False)  # in horsepower
    model_id = db.Column(db.Integer, db.ForeignKey('model.id'), nullable=False)
    
    # New fields for detailed engine information
    advantages = db.Column(db.JSON, default=list)
    disadvantages = db.Column(db.JSON, default=list)
    common_issues = db.Column(db.JSON, default=list)
    
    # Fuel consumption
    fuel_consumption_city_declared = db.Column(db.Float)
    fuel_consumption_highway_declared = db.Column(db.Float)
    fuel_consumption_combined_declared = db.Column(db.Float)
    fuel_consumption_city_real = db.Column(db.String(20))
    fuel_consumption_highway_real = db.Column(db.String(20))
    fuel_consumption_combined_real = db.Column(db.String(20))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/brands')
def get_brands():
    brands = Brand.query.all()
    return jsonify([{'id': b.id, 'name': b.name} for b in brands])

@app.route('/api/models/<int:brand_id>')
def get_models(brand_id):
    models = Model.query.filter_by(brand_id=brand_id).all()
    return jsonify([{
        'id': m.id,
        'name': m.name,
        'year_start': m.year_start,
        'year_end': m.year_end
    } for m in models])

@app.route('/api/engines/<int:model_id>')
def get_engines(model_id):
    engines = Engine.query.filter_by(model_id=model_id).all()
    return jsonify([{
        'id': e.id,
        'type': e.type,
        'displacement': e.displacement,
        'power': e.power
    } for e in engines])

@app.route('/api/search')
def search():
    brand_id = request.args.get('brand_id', type=int)
    model_id = request.args.get('model_id', type=int)
    engine_type = request.args.get('engine_type')
    min_power = request.args.get('min_power', type=int)
    max_power = request.args.get('max_power', type=int)
    
    query = db.session.query(Model, Engine).join(Engine)
    
    if brand_id:
        query = query.filter(Model.brand_id == brand_id)
    if model_id:
        query = query.filter(Model.id == model_id)
    if engine_type:
        query = query.filter(Engine.type == engine_type)
    if min_power:
        query = query.filter(Engine.power >= min_power)
    if max_power:
        query = query.filter(Engine.power <= max_power)
        
    results = query.all()
    return jsonify([{
        'model': {
            'id': m.id,
            'name': m.name,
            'year_start': m.year_start,
            'year_end': m.year_end
        },
        'engine': {
            'type': e.type,
            'displacement': e.displacement,
            'power': e.power
        }
    } for m, e in results])

@app.route('/model/<int:model_id>')
def model_detail(model_id):
    model = Model.query.get_or_404(model_id)
    return render_template('model_detail.html', model=model)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
