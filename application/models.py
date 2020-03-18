from application import db


class Hobby(db.Model):
    h_id = db.Column(db.Integer, primary_key=True)
    h_name = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    plan = db.relationship('Location',backref='plans', lazy=True)
    

    def __repr__(self):
        return ''.join([
            'Name: ', self.name,'\r\n',
            'Hobby: ', self.h_name])



class Location(db.Model):
    l_id = db.Column(db.Integer, primary_key=True)
    l_name = db.Column(db.String(30), nullable=False)
    time = db.Column(db.String(30), nullable=False)
    h_id = db.Column(db.Integer, db.ForeignKey('h_id'), nullable=False)
    


    def __repr__(self):
        return ''.join([
            'UserID: ', str(self.id), '\r\n' ,
            'Email: ',self.email, '\r\n',
            'Name: ',self.first_name, '', self.last_name])