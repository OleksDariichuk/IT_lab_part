from flask import Flask, render_template, request
from classes import Database, Table, IntegerDataColumn, TextDataColumn, Row

app = Flask(__name__)

db = Database("MyDatabase")

table1 = Table("Table1")
table1.add_column(IntegerDataColumn("ID"))
table1.add_column(TextDataColumn("Name"))
db.tables.append(table1)

table1.rows.append(Row(table1, [1, "Alex"]))
table1.rows.append(Row(table1, [2, "Dimasik"]))
table1.rows.append(Row(table1, [3, "Bogdan"]))

table2 = Table("Table2")
table2.add_column(IntegerDataColumn("ID"))
table2.add_column(TextDataColumn("Name"))
db.tables.append(table2)

table2.rows.append(Row(table2, [1, "Bieber"]))
table2.rows.append(Row(table2, [2, "Jordan"]))
table2.rows.append(Row(table2, [3, "Mydryk"]))

@app.route('/table1')
def table1_page():
    return render_template('app.html', table=table1)

@app.route('/table2')
def table2_page():
    return render_template('app.html', table=table2)

@app.route('/product', methods=['POST', 'GET'])
def product():
    if request.method == 'POST':
        result_table = Table("ProductTable")
        result_table.add_column(IntegerDataColumn("ID"))
        result_table.add_column(TextDataColumn("Name"))

        for row1 in table1.rows:
            for row2 in table2.rows:
                product_row = [row1[0] * row2[0], f"{row1[1]} - {row2[1]}"]
                result_table.rows.append(Row(result_table, product_row))

        return render_template('app.html', table=result_table)

    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
