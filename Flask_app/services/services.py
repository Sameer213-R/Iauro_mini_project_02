from db.connection import get_connection


def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users

    finally:
        cursor.close()
        conn.close()


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "SELECT * FROM users WHERE user_id = %s",
            (user_id,)
        )

        user = cursor.fetchone()
        return user

    finally:
        cursor.close()
        conn.close()


def add_user(user_name, user_city, gender):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users (user_name, user_city, gender)
            VALUES (%s, %s, %s)
            RETURNING user_id
            """,
            (
                user_name,
                user_city,
                gender
            )
        )

        user_id = cursor.fetchone()[0]

        conn.commit()

        return user_id

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


def update_user(user_id, user_name, user_city, gender):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            UPDATE users
            SET user_name = %s,
                user_city = %s,
                gender = %s
            WHERE user_id = %s
            """,
            (
                user_name,
                user_city,
                gender,
                user_id
            )
        )

        if cursor.rowcount == 0:
            return False

        conn.commit()

        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "DELETE FROM users WHERE user_id = %s",
            (user_id,)
        )

        if cursor.rowcount == 0:
            return False

        conn.commit()

        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()