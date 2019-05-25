from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

list = [
    {
        'id': 1,
        "name": "Luke Skywalker",
    },
    {
        'id': 2,
        "name": "C-3PO",
    },
    {
        'id': 3,
        "name": "Darth Vader",
    }
]

# create
@app.route('/create/<username>')
def createPerson(username):

    list.append(
        {
            'id': random.randint(1, 101),
            'name': '%s' % username,
        }
    )

    return jsonify(list)
  
# read
@app.route('/read')
def listPerson():

  return jsonify(list)

# read
@app.route('/read/<int:person_id>')
def listAPerson(person_id):

    for i in range(0, len(list)):
        if list[i]['id'] == person_id:
            return jsonify(list[i])

# update
@app.route('/update/<int:person_id>/<username>')
def UpdateAPerson(person_id, username):

    for i in range(0, len(list)):
        if list[i]['id'] == person_id:
            list[i]['name'] = '%s' % username
            return jsonify(list[i])


# delete
@app.route('/delete/<int:person_id>')
def deletePerson(person_id):

    for i in range(0, len(list)):
        if list[i]['id'] ==  person_id:
            del list[i]

    return jsonify(list)


if __name__ == '__main__':
    port = int( os.environ.get('PORT', 5000) )
    app.run(host='127.0.0.1', port=port)