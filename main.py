from flask import Flask, render_template, request

app = Flask(__name__)
receptes = {}

@app.route('/',methods=['GET', 'POST'])
def index():
    receptes = llegir_receptes()  

    if request.method == 'POST':
        nom_recepta = request.form.get('nom_recepta')
        ingredients = request.form.getlist('ing_recepta') #Llista
        quantitats = request.form.getlist('quant_recepta')  
        passos = request.form.getlist('pas_recepta')  
        tipus = request.form.get('tipus')

        
        ingredients_combinats = [{"ingredient": ing, "quantitat": quant} for ing, quant in zip(ingredients, quantitats)]

        nova_recepta = None  

        if tipus == 'Primer Plat':
            nova_recepta = PrimerPlat(nom_recepta, ingredients_combinats, passos)
        elif tipus == 'Segon Plat':
            nova_recepta = SegonPlat(nom_recepta, ingredients_combinats, passos)
        elif tipus == 'Postres':
            nova_recepta = Postres(nom_recepta, ingredients_combinats, passos)

        if nova_recepta:
            receptes.append(nova_recepta.to_dict())
            desar_receptes(receptes)  

    return render_template('index.html', receptes=receptes)


if __name__ == '__main__':
    	app.run(debug=True)

#cOMENT

