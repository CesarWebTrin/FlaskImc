from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/imc', methods=['POST'])

def calculateImc(weight, height):
    return weight / (height * height)

def obtainImcResult(imc):
    if imc < 18.5:
        return 'Magreza'
    elif imc >= 18.5 and imc < 24.9:
        return 'Normal'
    elif imc >= 24.9 and imc < 30:
        return 'Sobrepeso'
    else:
        return 'Obesidade'

def handleCalculateImc():
    data = request.get_json()
    weight = data['weight']
    height = data['height']

    imc = calculateImc(weight, height)
    result = obtainImcResult(imc)

    return jsonify({
        'imc': imc,
        'result': result
    })


    
if __name__ == '__main__':
    app.run()