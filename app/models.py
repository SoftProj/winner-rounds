from . import db
import datetime


class Integrante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    equipo = db.relationship('Equipo', backref='integrante')


class Tiempo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tiempo = db.Column(db.DateTime, nullable=True)

    equipo = db.relationship('Equipo', backref='tiempo')
    ronda = db.relationship('Ronda')

class Equipo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), unique=True)
    passw = db.Column(db.String(40))
    activo = db.Column(db.Boolean, default=False)

    integrante = db.Column(db.Integer, db.ForeignKey('integrante.id'), nullable=True)
    tiempo = db.Column(db.Integer, db.ForeignKey('tiempo.id'))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<Equipo %r>' % (self.user)

class Ronda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))

    equipo_win = db.relationship('Equipo')

