from flask import Flask ,session ,render_template, flash, redirect , url_for , request , jsonify , make_response
from flask_sqlalchemy import SQLAlchemy
import datetime
from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, EqualTo, Length

app = Flask(__name__)
# Config
app.secret_key="abaderfreildfa"
app.config['SECRET_KEY'] = "my ss no efergtrththe is supposedhhtyeh to know"
# local host
userpass = 'mysql+pymysql://root:@'
basedir  = '127.0.0.1'
dbname   = '/index2'
app.config['SQLALCHEMY_DATABASE_URI'] = userpass + basedir + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(50))
    mois = db.Column(db.Integer)
    date_prestation =  db.Column(db.DateTime)
    demandeur = db.Column(db.String(50))
    bcn = db.Column(db.Integer)
    type_camion = db.Column(db.String(50))
    depart = db.Column(db.String(50))
    arrive = db.Column(db.String(50))
    taches = db.Column(db.String(50))
    facture_n = db.Column(db.Integer)

class Camion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proprietaire =db.Column(db.String(50))
    matricule = db.Column(db.String(50))
    nom_chauffeur =db.Column(db.String(50))
    nombre_site_visite = db.Column(db.Integer)
    km_parcouru = db.Column(db.Integer)
    bl  = db.Column(db.Integer)
    frais_depl = db.Column(db.Integer)
    achat_ht = db.Column(db.Integer)
    mode_achat = db.Column(db.String(50))
    type_reglement_achat = db.Column(db.String(50))

class Facture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vente_ht = db.Column(db.Integer)
    mode_vente = db.Column(db.String(10))
    folio = db.Column(db.String(50))
    facture_n = db.Column(db.Integer)
    date_facture = db.Column(db.DateTime)
    montant_ht = db.Column(db.Integer)
    tva_14 = db.Column(db.Integer)
    tva_20 = db.Column(db.Integer)
    montant_ttc = db.Column(db.Integer)




client_columns = [('id',False),('client','Client'),('mois','Mois'),('demandeur','Demandeur'),('bcn','BC N'),('date_prestation','Date Prestation'),('type_camion','Type Camion'),('depart','Depart'),('arrive','Arrive'),('taches','Taches'),('facture_n','Facture N')]
camion_columns = [('id',False),('client','Client'),('proprietaire','Proprietaire'),('matricule','Matricule'), ('nom_chauffeur','Chauffeur Nom') ,('nombre_site_visite','Nombre Site Visite'), ('km_parcouru','Km Parcouru') ,('bl','BL') ,('frais_depl','Frais Depl'),('achat_ht','Achat HT'), ('mode_achat','Mode Achat') ,('type_reglement_achat','Type Reglement Achat')]
facture_columns = [('id',False),('facture_n','Facture N'),('client','Client'),('vente_ht','ENTE HT'),('mode_vente','Mode Vente'),('folio','Folio'),('date_facture','Date Facture'),('montant_ht','Montant H'),('tva_14','TVA 14%'),('tva_20','TVA 20%'),('montant_ttc','Montant TTC')]

l=[('client', 'Client'), ('mois', 'Mois'), ('demandeur', 'Demandeur'), ('bcn', 'BC N'), ('date_prestation', 'Date Prestation'), ('type_camion', 'Type Camion'), ('depart', 'Depart'), ('arrive', 'Arrive'), ('taches', 'Taches'), ('facture_n', 'Facture N'), ('proprietaire', 'Proprietaire'), ('matricule', 'Matricule'), ('nom_chauffeur', 'Chauffeur Nom'), ('nombre_site_visite', 'Nombre Site Visite'), ('km_parcouru', 'Km Parcouru'), ('bl', 'BL'), ('frais_depl', 'Frais Depl'), ('achat_ht', 'Achat HT'), ('mode_achat', 'Mode Achat'), ('type_reglement_achat', 'Type Reglement Achat'), ('vente_ht', 'ENTE HT'), ('mode_vente', 'Mode Vente'), ('folio', 'Folio'), ('date_facture', 'Date Facture'), ('montant_ht', 'Montant H'), ('tva_14', 'TVA 14%'), ('tva_20', 'TVA 20%'), ('montant_ttc', 'Montant TTC')]

def clien_print():
    clients=Client.query.all()
    output=[]
    for client in clients :
        data={}
        data['id']=client.id
        data['client']=client.client
        data['mois'] = client.mois
        data['date_prestation']=client.date_prestation
        data['demandeur' ]=client.demandeur
        data['bcn' ]=client.bcn
        data['type_camion'] =client.type_camion
        data['depart']  =client.depart
        data['arrive'] =client.arrive
        data['taches']=client.taches
        data['facture_n']=client.facture_n
        output.append(data)
    return output
def facture_print(id):
    factures=Facture.query.filter_by(id=id).first()
    clients=Client.query.filter_by(id=id).first()
    data={}
    data['id']=factures.id
    data['client'] = clients.client
    data['vente_ht']=factures.vente_ht
    data['facture_n']=factures.facture_n
    data['mode_vente'] = factures.mode_vente
    data['folio' ]=factures.folio
    data['facture_n'] =factures.facture_n
    data['date_facture']  =factures.date_facture
    data['montant_ht']=factures.montant_ht 
    data['tva_14']=factures.tva_14
    data['tva_20']=factures.tva_20
    data['montant_ttc']=factures.montant_ttc
    return data


def camion_print(id):
    camions=Camion.query.filter_by(id=id).first()
    clients=Client.query.filter_by(id=id).first()
    data={}
    data['id']=camions.id
    data['client'] = clients.client
    data['proprietaire']=camions.proprietaire
    data['matricule'] = camions.matricule
    data['nom_chauffeur']=camions.nom_chauffeur
    data['nombre_site_visite' ]=camions.nombre_site_visite
    data['km_parcouru'] =camions.km_parcouru
    data['bl']  =camions.bl
    data['frais_depl'] =camions.frais_depl
    data['achat_ht']=camions.achat_ht
    data['mode_achat']=camions.mode_achat
    data['type_reglement_achat']=camions.type_reglement_achat
    return data
def print_all():
    clients=Client.query.all()
    output=[]
    for client in clients :
        data={}
        data['id']=client.id
        data['client']=client.client
        data['mois'] = client.mois
        data['date_prestation']=client.date_prestation
        data['demandeur' ]=client.demandeur
        data['bcn' ]=client.bcn
        data['type_camion'] =client.type_camion
        data['depart']  =client.depart
        data['arrive'] =client.arrive
        data['taches']=client.taches
        data['facture_n']=client.facture_n
        camions=Camion.query.filter_by(id=client.id).first()
        if camions is not None:
            data['proprietaire']=camions.proprietaire
            data['matricule'] = camions.matricule
            data['nom_chauffeur']=camions.nom_chauffeur
            data['nombre_site_visite' ]=camions.nombre_site_visite
            data['km_parcouru'] =camions.km_parcouru
            data['bl']  =camions.bl
            data['frais_depl'] =camions.frais_depl
            data['achat_ht']=camions.achat_ht
            data['mode_achat']=camions.mode_achat
            data['type_reglement_achat']=camions.type_reglement_achat
        else:
            data['proprietaire']= "-"
            data['matricule'] = "-"
            data['nom_chauffeur']="-"
            data['nombre_site_visite' ]="-"
            data['km_parcouru'] ="-"
            data['bl']  ="-"
            data['frais_depl'] ="-"
            data['achat_ht']="-"
            data['mode_achat']="-"
            data['type_reglement_achat']="-"
        factures=Facture.query.filter_by(id=client.id).first()
        if factures is not None:
            data['vente_ht']=factures.vente_ht
            data['facture_n']=factures.facture_n
            data['mode_vente'] = factures.mode_vente
            data['folio' ]=factures.folio
            data['facture_n'] =factures.facture_n
            data['date_facture']  =factures.date_facture
            data['montant_ht']=factures.montant_ht
            data['tva_14']=factures.tva_14
            data['tva_20']=factures.tva_20
            data['montant_ttc']=factures.montant_ttc
        else :
            data['vente_ht']="-"
            data['facture_n']="-"
            data['mode_vente'] = "-"
            data['folio' ]="-"
            data['facture_n'] ="-"
            data['date_facture']  ="-"
            data['montant_ht']="-"
            data['tva_14']="-"
            data['tva_20']="-"
            data['montant_ttc']="-"

        output.append(data)
    return output
def trans(r):
    output=[]
    for i in print_all() :
        data={}
        for j in r:
            data[j[0]]=i[j[0]]
        output.append(data)
    return output







@app.route("/")
def root():
    return render_template('home.html')

# show/adding/edit
@app.route("/show/<adding>/<edit_id>")
def show(adding,edit_id):
    data=clien_print()
    return render_template("commande.html",data=data,Columns=client_columns,adding=adding,edit_id=int(edit_id))

# add_commande
@app.route("/add_commande", methods=['GET', 'POST'])
def add_commande():
    if request.method == "POST":
        client = request.form.get("client")
        mois = request.form.get("mois")
        demandeur = request.form.get("demandeur")
        date_prestation = request.form.get("date_prestation")
        type_camion = request.form.get("type_camion")
        depart = request.form.get("depart")
        arrive = request.form.get("arrive")
        taches = request.form.get("taches")
        bcn = request.form.get("bcn")
        facture_n = request.form.get("facture_n")
        new_client = Client(client=client,mois=mois,facture_n=facture_n,demandeur=demandeur,date_prestation=date_prestation,type_camion=type_camion,depart=depart,arrive=arrive,taches=taches)
        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('show',adding=False,edit_id=-1))
    return redirect(url_for('show',adding=True,edit_id=-1))

# edit_commande/id
@app.route("/edit_commande/<id>", methods=['GET', 'POST'])
def edit_commande(id):
    if request.method == "POST":
        new_client = Client.query.filter_by(id=id).first()
        new_client.client = request.form.get("client")
        new_client.mois = request.form.get("mois")
        new_client.demandeur = request.form.get("demandeur")
        new_client.date_prestation = request.form.get("date_prestation")
        new_client.type_camion = request.form.get("type_camion")
        new_client.depart = request.form.get("depart")
        new_client.arrive = request.form.get("arrive")
        new_client.taches = request.form.get("taches")
        new_client.bcn = request.form.get("bcn")
        new_client.facture_n = request.form.get("facture_n")
        db.session.commit()
        return redirect(url_for('show',adding=False,edit_id=-1))
    return redirect(url_for('show',adding=False,edit_id=id))


# delete_commande/id
@app.route("/delete_commande/<id>", methods=['GET', 'POST'])
def delete_commande(id):
    client = Client.query.filter_by(id=id).first()
    db.session.delete(client)
    db.session.commit()
    factures = Facture.query.filter_by(id=id).first()
    if factures is not None :
        db.session.delete(factures)
        db.session.commit()
    camions = Camion.query.filter_by(id=id).first()
    if camions is not None :
        db.session.delete(camions)
        db.session.commit()
    return redirect(url_for('show',adding=False,edit_id=-1))



#Facture

#show_facture/id
@app.route("/show_facture/<id>/<edit_id>", methods=['GET', 'POST'])
def show_facture(id,edit_id):
    factures=Facture.query.filter_by(id=id).first()
    if factures is not None:
        return render_template('facture.html',data = facture_print(id), Columns = facture_columns,adding=False,edit_id=int(edit_id))
    else :
        clients = Client.query.filter_by(id=id).first()
        data={}
        data["client"] = clients.client
        data["id"] = clients.id
        data["facture_n"] = clients.facture_n
        return render_template('facture.html',data = data, Columns = facture_columns,adding=True,edit_id=int(edit_id))

@app.route("/add_facture/<id>", methods=['GET', 'POST'])
def add_facture(id):
    if request.method == "POST":
        clients = Client.query.filter_by(id=id).first()
        vente_ht = request.form.get("vente_ht")
        mode_vente = request.form.get("mode_vente")
        folio = request.form.get("folio")
        facture_n= clients.facture_n
        date_facture = request.form.get("date_facture")
        montant_ht = request.form.get("montant_ht")
        tva_14 = request.form.get("tva_14")
        tva_20 = request.form.get("tva_20")
        montant_ttc = request.form.get("montant_ttc")
        new_facture = Facture(id=id ,vente_ht=vente_ht,mode_vente=mode_vente,folio=folio,facture_n=facture_n,date_facture=date_facture,montant_ht=montant_ht,tva_14=tva_14,tva_20=tva_20,montant_ttc=montant_ttc)
        db.session.add(new_facture)
        db.session.commit()
        return redirect(url_for('show_facture',id=id,edit_id=-1))

@app.route("/edit_facture/<id>", methods=['GET', 'POST'])
def edit_facture(id):
    if request.method == "POST":
        new_facture = Facture.query.filter_by(id=id).first()
        new_facture.vente_ht = request.form.get("vente_ht")
        new_facture.mode_vente = request.form.get("mode_vente")
        new_facture.folio = request.form.get("folio")
        new_facture.date_facture = request.form.get("date_facture")
        new_facture.montant_ht = request.form.get("montant_ht")
        new_facture.tva_14 = request.form.get("tva_14")
        new_facture.tva_20 = request.form.get("tva_20")
        new_facture.montant_ttc = request.form.get("montant_ttc")
        db.session.commit()
        return redirect(url_for('show_facture',id =id , edit_id = -1))
    return redirect(url_for('show_facture',id =id , edit_id= id))





#Camion

#show_camion/id
@app.route("/show_camion/<id>/<edit_id>", methods=['GET', 'POST'])
def show_camion(id,edit_id):
    camions=Camion.query.filter_by(id=id).first()
    if camions is not None:
        return render_template('camion.html',data = camion_print(id), Columns = camion_columns,adding=False,edit_id=int(edit_id))
    else :
        clients = Client.query.filter_by(id=id).first()
        data={}
        data["client"] = clients.client
        data["id"] = clients.id
        return render_template('camion.html',data = data, Columns = camion_columns,adding=True,edit_id=int(edit_id))

#ad_camion
@app.route("/add_camion/<id>", methods=['GET', 'POST'])
def add_camion(id):
    if request.method == "POST":
        proprietaire = request.form.get("proprietaire")
        matricule = request.form.get("matricule")
        nom_chauffeur = request.form.get("nom_chauffeur")
        nombre_site_visite = request.form.get("nombre_site_visite")
        km_parcouru = request.form.get("km_parcouru")
        bl = request.form.get("bl")
        frais_depl = request.form.get("frais_depl")
        achat_ht = request.form.get("achat_ht")
        mode_achat = request.form.get("mode_achat")
        type_reglement_achat = request.form.get("type_reglement_achat")
        new_camion = Camion(id=id ,proprietaire=proprietaire,matricule=matricule,nom_chauffeur=nom_chauffeur,nombre_site_visite=nombre_site_visite,km_parcouru=km_parcouru,bl=bl,frais_depl=frais_depl,achat_ht=achat_ht,mode_achat=mode_achat,type_reglement_achat=type_reglement_achat)
        db.session.add(new_camion)
        db.session.commit()
        return redirect(url_for('show_camion',id=id,edit_id=-1))

@app.route("/edit_camion/<id>", methods=['GET', 'POST'])
def edit_camion(id):
    if request.method == "POST":
        new_camion = Camion.query.filter_by(id=id).first()
        new_camion.proprietaire = request.form.get("proprietaire")
        new_camion.matricule = request.form.get("matricule")
        new_camion.nom_chauffeur = request.form.get("nom_chauffeur")
        new_camion.nombre_site_visite = request.form.get("nombre_site_visite")
        new_camion.km_parcouru = request.form.get("km_parcouru")
        new_camion.bl = request.form.get("bl")
        new_camion.frais_depl = request.form.get("frais_depl")
        new_camion.achat_ht = request.form.get("achat_ht")
        new_camion.mode_achat = request.form.get("mode_achat")
        new_camion.type_reglement_achat = request.form.get("type_reglement_achat")
        db.session.commit()
        return redirect(url_for('show_camion',id =id , edit_id = -1))
    return redirect(url_for('show_camion',id =id , edit_id= id))

@app.route("/costomized", methods=['GET', 'POST'])
def costomized():
    if request.method == "POST":
        r=[]
        for i in l :
            if request.form.get(i[0]) != None :
                r.append(i)
        print(trans(r))
        return render_template("costomized.html" ,l=l,serche=False,data=trans(r),r=r)

    return render_template("costomized.html" ,l=l,serche=True,data=None,r=None)

if __name__ == '__main__':
    app.run(debug=True)
