# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 18:31:36 2020

@author: lenovo
"""

from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))



@app.route("/")
@cross_origin()
def home():
    return render_template("webpage.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Area
        area = int(request.form["Area"])

        # bhk_count
        bhk_count = int(request.form["BHK"])
        
        # bathroom
        bathroom = int(request.form["bathroom"])
        
        # status_ready_to_move
        status_ready_to_move = int(request.form["status_ready_to_move"])
        
        # floor_number
        floor_number = int(request.form["floor"])
        #print(floor_number)
        
        # balcony
        balcony = int(request.form["balcony"])
        
        # area_type
        area_type = int(request.form["area_type"])
        
        # transaction_resale
        transaction_resale = int(request.form["transaction"])

        # Society
        Society = request.form['Society']
        
        society_ng = 0
        society_sushma_grande= 0
        society_joynest_zrk_1= 0
        society_bella_homes= 0
        society_others= 0

        if Society == 'society_ng':
            society_ng = 1
        elif Society == 'society_sushma_grande':
            society_sushma_grande = 1
        elif Society == 'society_joynest_zrk_1':
            society_joynest_zrk_1 = 1
        elif Society == 'society_bella_homes':
            society_bella_homes = 1
        elif Society == 'society_others':
            society_others = 1
        


        
        prediction=model.predict([[area, bhk_count, bathroom, status_ready_to_move, floor_number,
       society_ng, balcony, area_type, transaction_resale,
       society_sushma_grande, society_joynest_zrk_1, society_bella_homes,
       society_others]])

        output=round(prediction[0],2)

        return render_template('webpage.html',prediction_text="Your House price is Rs. {}".format(output))

    else:   
        return render_template("webpage.html")




if __name__ == "__main__":
    app.run(debug=True)