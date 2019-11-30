from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('input.html')

# to enter a new record
@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            nmbr = request.form['nmb']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute(
                    "INSERT INTO students (name,nmbr) VALUES (?,?)", (nm, nmbr))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


# to display normal list
@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)

# to display sorted list alphabetically asc
@app.route('/list_sort')
def list_sort():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students order by name asc")

    rows = cur.fetchall()
    return render_template("list_sort_asc.html", rows=rows)

# to display sorted list alphabetically desc
@app.route('/list_sort_d')
def list_sort_d():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students order by name desc")

    rows = cur.fetchall()
    return render_template("list_sort_dsc.html", rows=rows)


# search a record
@app.route('/search',  methods=["GET", "POST"])
def search():
    if request.method == "POST":
        username = request.form["snm"]
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students where name ='Raju'")

    rows = cur.fetchall()
    return render_template("search_res.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)
