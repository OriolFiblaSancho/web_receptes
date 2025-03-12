from flask import Flask, render_template, request

app = Flask(__name__)
receptes = {}

@app.route('/',methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        nom_recepta = request.form.get('nom_recepta')
        ing_recepta = request.form.get('ing_recepta')
        receptes[nom_recepta] = ing_recepta
    return render_template('index.html', receptes = receptes)
                      
if __name__ == '__main__':
    	app.run(debug=True)
         

