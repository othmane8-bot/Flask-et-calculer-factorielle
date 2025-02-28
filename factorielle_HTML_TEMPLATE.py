from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculateur de Factorielle</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 20px;
            background: #f0f2f5;
            display: flex;
            justify-content: center;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            width: 100%;
            max-width: 500px;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 15px;
        }
        input {
            padding: 12px;
            border: 2px solid #3498db;
            border-radius: 5px;
            font-size: 16px;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 12px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #e8f4fc;
            border-radius: 5px;
            color: #2c3e50;
        }
        .error {
            color: #e74c3c;
            padding: 15px;
            background: #fdeded;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🔢 Calculateur de Factorielle</h1>

        <form method="POST">
            <input type="text" 
                   name="nombre" 
                   value="{{ nombre }}"
                   placeholder="Entrez un nombre entier positif">
            <button type="submit">Calculer</button>
        </form>

        {% if error %}
            <div class="error">⚠️ {{ error }}</div>
        {% endif %}

        {% if result %}
            <div class="result">
                ✅ Résultat : {{ nombre }}! = <strong>{{ result }}</strong>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""


def calcul_factorielle(n):
    if n in (0, 1):
        return 1
    return n * calcul_factorielle(n - 1)


@app.route('/', methods=['GET', 'POST'])
def index():
    result = error = nombre = None

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()

        if not nombre:
            error = "Veuillez entrer un nombre."
        else:
            try:
                n = float(nombre)
                if not n.is_integer():
                    error = "Le nombre doit être un entier."
                else:
                    n = int(n)
                    if n < 0:
                        error = "Le nombre ne peut pas être négatif."
                    else:
                        result = calcul_factorielle(n)
            except ValueError:
                error = "Veuillez entrer un nombre valide."

    return render_template_string(HTML_TEMPLATE,
                                  result=result,
                                  error=error,
                                  nombre=nombre)


if __name__ == '__main__':
    app.run(debug=True)