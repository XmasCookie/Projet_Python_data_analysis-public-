import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

#Ouverture du modèle
model = pickle.load(open('model.pickle','rb'))

#API
@app.route('/api',methods=['POST'])
def predict():
    data = request.get_json()
    #Prédiction et retour
    prediction = np.bool(model.predict(data)[0])
    if prediction == False:
        prediction = "Sober person"
    if prediction == True:
        prediciton = "Drunk person"
    output = prediction
    return jsonify(output)

#Retour du résultat
if __name__ == '__main__':
    modelfile = 'model.pickle'
    model = pickle.load(open(modelfile, 'rb'))
    app.run(port=5000, debug=True)