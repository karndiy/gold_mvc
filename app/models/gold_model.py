from app import db

class GoldPrice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    asdate = db.Column(db.String(50))
    nqy = db.Column(db.String(10))
    blbuy = db.Column(db.String(20))
    blsell = db.Column(db.String(20))
    ombuy = db.Column(db.String(20))
    omsell = db.Column(db.String(20))
    goldspot = db.Column(db.String(20))
    bahtusd = db.Column(db.String(20))
    diff = db.Column(db.String(20))

    def to_dict(self):
        return {
            "asdate": self.asdate,
            "nqy": self.nqy,
            "blbuy": self.blbuy,
            "blsell": self.blsell,
            "ombuy": self.ombuy,
            "omsell": self.omsell,
            "goldspot": self.goldspot,
            "bahtusd": self.bahtusd,
            "diff": self.diff,
        }

def insert_gold_data(data):
    inserted = []
    for item in data:
        # Check if the record with same date already exists
        exists = GoldPrice.query.filter_by(asdate=item['asdate']).first()
        if not exists:
            new_entry = GoldPrice(
                asdate=item['asdate'],
                nqy=item['nqy'],
                blbuy=item['blbuy'],
                blsell=item['blsell'],
                ombuy=item['ombuy'],
                omsell=item['omsell'],
                goldspot=item['goldspot'],
                bahtusd=item['bahtusd'],
                diff=item['diff']
            )
            db.session.add(new_entry)
            inserted.append(item)
    db.session.commit()
    return inserted

def get_all_gold():
    return GoldPrice.query.order_by(GoldPrice.id.desc()).limit(5).all()

def get_limit_gold(limits = 10):
    return GoldPrice.query.order_by(GoldPrice.id.desc()).limit(limits).all()



def get_latest_asdate():
    return GoldPrice.query.order_by(GoldPrice.asdate.desc()).first()
