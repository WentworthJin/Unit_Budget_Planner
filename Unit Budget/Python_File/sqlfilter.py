from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def query():
    data = request.args.to_dict()
    params = data.keys()
    s1 = 'U.UnitCode ="{}" '.format(data['unitcode']) if 'unitcode' in params else ''
    s2 = 'U.Year = ' + data['year'] if 'year' in params else ''
    s3 = 'U.Semester = ' + data['semester'] if 'semester' in params else ''
    s = list()
    for x in [s1, s2, s3]:
        if x:
            s.append(x)
    sql1 = ' and '.join(s)
    sql = '''select * from Activities A JOIN Staff S USING (StaffID)
                               JOIN Session E USING (SessionID)
                               JOIN Unit U USING (UnitID) where ''' + sql1
    print(sql)
    try:
        conn = sqlite3.connect('BudgetSample.db')
        c = conn.cursor()
        c.execute(sql)
        col_name_list = [tuple[0] for tuple in c.description]
        content = c.fetchall()
        conn.commit()
        conn.close()
        r = {'success':'ture','data':list()}
        for row in content:
            d = dict(zip(col_name_list, row))
            r['data'].append(d)
        return jsonify(r)
    except:
        return {'success':'false'}

@app.route('/sqlquery', methods=['POST'])
def sqlquery():
    try:
        sql = request.form['sql']
        conn = sqlite3.connect('BudgetSample.db')
        c = conn.cursor()
        c.execute(sql)
        col_name_list = [tuple[0] for tuple in c.description]
        content = c.fetchall()
        conn.commit()
        conn.close()
        r = {'success':'ture','data':list()}
        for row in content:
            d = dict(zip(col_name_list, row))
            r['data'].append(d)
        return jsonify(r)
    except:
        return {'success':'false'}



if __name__ == "__main__":
    app.run(debug=True)


# conn = sqlite3.connect('BudgetSample.db')
# sql = '''select * from Activities A JOIN Staff S USING (StaffID)
#                                JOIN Session E USING (SessionID)
#                                JOIN Unit U USING (UnitID) where U.UnitCode = 'CITS4401'
# '''

# c = conn.cursor()
# c.execute(sql)
# content = c.fetchall()
# conn.commit()
# conn.close()

# print(content)