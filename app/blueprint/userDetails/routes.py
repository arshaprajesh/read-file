
from flask import jsonify,request
#from sqlalchemy import select

from . import user_bp
from ...models import  File,Users
from app.extensions import db
import os



          
@user_bp.route("/userFile", methods=["POST"])
def create_user_and_file():
    print("create file invoked")
    path ="/Users/kunip004/Documents/arsha/docs/project"
    Created_by = "arsha"
    Created_at = "2025-08-01"
    
    
    #uploaded_file = request.files.get('file-path') #arsha.txt --> /users/docs/arsha.txt
    data = request.get_json()
    print("data:",data)
    file_path = data.get('file-path')  # This should be a string
    print("file_path",file_path)#file_path should be same what we giving in postman json data
    name = data.get('user-name')
    print("name",name)
    date = data.get('user-date')
    print("date",date)
    state = data.get('user-state')
    print("state",state)
    
    
    if not all:
        return jsonify({"error": "No datas uploaded"}), 400
    
    print("data is not empty")
    full_filepath = os.path.join(path, os.path.basename(file_path))
    print("full file path",full_filepath)
    with open(full_filepath, 'r', encoding='utf-8') as f:
     description = f.read()
    print("description",description)


    
    new_user = Users(name=name, date=date ,state=state,Created_by=Created_by,Created_at=Created_at)
    new_file = File(title=file_path, description=description)
    
    new_user.files.append(new_file)#list of file is adding in user so need to add user only 

    db.session.add(new_user)
    db.session.commit() 
    
    
    """ this is also working when append data in formdata(in upload.jsx file)
    
    uploaded_file = request.files.get('file')
    name = request.form.get('user-name')
    date = request.form.get('user-date')
    state = request.form.get('user-state')

    if not uploaded_file or not name or not date or not state:
     return jsonify({"error": "Missing required data"}), 400

    full_filepath = os.path.join(path, uploaded_file.filename)
    uploaded_file.save(full_filepath)

    with open(full_filepath, 'r', encoding='utf-8') as f:
        description = f.read()

    new_user = Users(name=name, date=date, state=state, Created_by=Created_by, Created_at=Created_at)
    new_file = File(title=uploaded_file.filename, description=description)

    new_user.files.append(new_file)
    db.session.add(new_user)
    db.session.commit() """

    
    return jsonify({
        "user": {
            "name": new_user.name,
            "date": new_user.date,
            "state": new_user.state
        },
        "file": {
            "title": new_file.title,
            "description": new_file.description
        }
    }), 201


    

@user_bp.route("/userFile/<int:userId>", methods=["GET"])
def read_user(userId):
    user = db.session.get(Users, userId)
    print("user",user)
    if not user:
        return jsonify({"error": "user not found"}), 404
    try:
      
        return jsonify({
            
            "userID": user.userID,
            "name":user.name,
            "date":user.date,
            "state":user.state}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500 
    
    
    

@user_bp.route("/userFile/search", methods=["GET"])

def search_user_by_name():
    
    print("Query string:", request.args)
    name = request.args.get("name")
    
    print("name:", name)
    

    if not name:
        return jsonify({"error": "Name parameter is required"}), 400

    users = Users.query.filter_by(name=name).all()
    print("Users found:", users)
    if not users:
        return jsonify({"error": "No users found with that name"}), 404

    result = []
    for user in users:
        user_data = {
            "userID": user.userID,
            "name": user.name,
            "date": user.date,
            "state": user.state,
            "files": [{"title": f.title, "description": f.description} for f in user.files]
        }
        result.append(user_data)

    return jsonify(result), 200
