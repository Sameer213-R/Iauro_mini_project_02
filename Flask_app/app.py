from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)


# Database connection
def get_connection():
    return psycopg2.connect(
        host="my_postgres_container",
        database="iauro",
        user="root",
        password="2020"
    )


# Home
@app.route("/")
def home():
    return "Flask application is connected"


# Get all users
@app.route("/users", methods=["GET"])
def get_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)


# Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE user_id = %s",
        (user_id,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if user is None:
        return jsonify({"message": "User not found"}), 404

    return jsonify(user)


# Add user
@app.route("/users", methods=["POST"])
def add_user():

    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO users (user_name, user_city, gender)
        VALUES (%s, %s, %s)
        RETURNING user_id
        """,
        (
            data["user_name"],
            data["user_city"],
            data["gender"]
        )
    )

    user_id = cursor.fetchone()[0]

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "User added",
        "user_id": user_id
    }), 201


# Update user by ID
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):

    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET user_name = %s,
            user_city = %s,
            gender = %s
        WHERE user_id = %s
        """,
        (
            data["user_name"],
            data["user_city"],
            data["gender"],
            user_id
        )
    )

    if cursor.rowcount == 0:

        conn.close()

        return jsonify({
            "message": "User not found"
        }), 404

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "User updated",
        "user_id": user_id
    })


# Delete user by ID
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE user_id = %s",
        (user_id,)
    )

    if cursor.rowcount == 0:

        conn.close()

        return jsonify({
            "message": "User not found"
        }), 404

    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({
        "message": "User deleted",
        "user_id": user_id
    })


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )