import psycopg2
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

def db_connection():
    conn = psycopg2.connect(
        dbname="flask",
        user="postgres",
        password="root",
        host="localhost"
    )

    return conn

@app.route('/')
def index():
    try:
        conn = db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM public.usuarios")
        rows = cur.fetchall()
        conn.close()

        response = []
        for row in rows:
            response.append({
                "id": row[0],
                "nombres": row[1],
                "apellidos": row[2],
                "edad": row[3],
                "correo": row[4],
                "password": row[5],
                "status": row[6],
                "created_at": row[7],
                "updated_at": row[8]
            })

        return response
    except Exception as e:
        return {
            "ok": False,
            "message": "Error al obtener los usuarios",
            "error": str(e)
        }, 500

@app.route('/create', methods=['POST'])
def create():
    try:
        json = request.get_json()
        print(json)
        conn = db_connection()
        cur = conn.cursor()
        query = "INSERT INTO public.usuarios (nombres, apellidos, edad, correo, password, status) VALUES (%s, %s, %s, %s, %s, %s)"
        cur.execute(
            query,
            (
                json['nombres'],
                json['apellidos'],
                json['edad'],
                json['correo'],
                json['password'],
                json['status']
            )
        )
        conn.commit()
        conn.close()

        return {
            "ok": True,
            "message": "Usuario creado correctamente"
        }, 201
    except Exception as e:
        conn.rollback()
        return {
            "ok": False,
            "message": "Error al crear el usuario",
            "error": str(e)
        }, 500
    
@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    try:
        conn = db_connection()
        cur = conn.cursor()
        json = request.get_json()
        query = "UPDATE public.usuarios SET nombres=%s, apellidos=%s, edad=%s, correo=%s, password=%s, status=%s WHERE id=%s"
        cur.execute(
            query,
            (
                json['nombres'],
                json['apellidos'],
                json['edad'],
                json['correo'],
                json['password'],
                json['status'],
                id
            )
        )
        conn.commit()
        conn.close()

        return {
            "ok": True,
            "message": "Usuario actualizado correctamente"
        }, 200
    except Exception as e:
        return {
            "ok": False,
            "message": "Error al actualizar el usuario",
            "error": str(e)
        }, 500

if __name__ == '__main__':
    app.run(debug=True)
