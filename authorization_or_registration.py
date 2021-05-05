import sqlite3
from hashlib import sha256


def registration(cursor, login, password, check_user):
    if check_user is None:
        cursor.execute(
            """
              INSERT INTO user (login, password)
              VALUES (?, ?)""", (login, password)
        )
    else:
        print("Thy another user!")


def authorization(login, password, check_user, cursor):
    if check_user is not None:
        while True:
            if check_user['login'] == login:
                if password == check_user['password']:

                    print(f"Welcome, {login}")
                    note(cursor, check_user)
                    break
                else:
                    print("Please login or password incorrect, try again!!")
                    main()
    else:
        print("Unknown user")


def note(cursor, check_user):
    while True:
        user_choice = input("Do you want to create a note or sign out:")
        if user_choice == "create a note":
            note_title = input("Enter the names for the task: ")
            note_text = input("Enter text of the task: ")
            cursor.execute(
                """
                  INSERT INTO notes (user_id, note_title,note_text)
                  VALUES(?, ?, ?)
              """, (check_user['id'], note_title, note_text))
            continue
        else:
            break


def main():
    login = input("Input login: ")
    password = sha256(input("Input password: ").encode()).hexdigest()
    input_task = input("You want registration or authorization?: ")

    conn = sqlite3.connect("mydatabase.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute(
        """
          CREATE TABLE
          IF NOT EXISTS user
          (
              id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
              login,
              password
          )
      """
    )

    cursor.execute(
        """
          CREATE TABLE
          IF NOT EXISTS notes
          (
              user_Id Integer not null,
              note_title,
              note_text,
              FOREIGN KEY (user_id) REFERENCES information (id)
          )
      """
    )

    check_user = cursor.execute(
        """
          SELECT id, login, password
          FROM user
          WHERE login = ?""", (login,)
    ).fetchone()
    print(check_user)

    if input_task == "registration":
        registration(cursor, login, password, check_user)
    elif input_task == "authorization":
        authorization(login, password, check_user, cursor)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()