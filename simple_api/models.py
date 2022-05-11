from . import db

class Apps(db.Model):
    class Meta:
        fields = ('id', 'app_name', 'category')
        
    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.Text)
    category = db.Column(db.Text)
    rating = db.Column(db.Float)
    rating_count = db.Column(db.Float)
    installs = db.Column(db.Text) 
    min_installs = db.Column(db.Integer)
    max_installs = db.Column(db.Integer)
    free = db.Column(db.Integer)
    price = db.Column(db.Float) 
    currency = db.Column(db.Text) 
    size = db.Column(db.Text)  
    released = db.Column(db.Text)  
    last_updated = db.Column(db.Text) 
    content_rating = db.Column(db.Text) 
    scraped_time = db.Column(db.Text)  
    price_zscore = db.Column(db.Text) 

    