from application import db


class Hobby(db.Model):
    h_id = db.Column(db.Integer, primary_key=True)
    h_name = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    l_id = db.Column(db.Integer, db.ForeignKey('location.l_id'), nullable=False)
    
    

    def __repr__(self):
        return ''.join([
            'Name: ', self.name,'\r\n',
            'Hobby: ', self.h_name,'\r\n',
            'Hobby No: ', str(self.h_id)])



class Location(db.Model):
    l_id = db.Column(db.Integer, primary_key=True)
    l_name = db.Column(db.String(30), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    plan = db.relationship('Hobby',backref='plans', lazy=True)
    
    


    def __repr__(self):
        return ''.join([
            'Location: ',self.l_name,'\r\n',
            'Time: ',self.time])