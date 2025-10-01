
from flask import Flask
from app.extensions import db

from .blueprint.userDetails import user_bp
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.config.from_object("config.DevelopmentConfig")
    CORS(app,resources={r"/*": {"origins": "*"}}) #Your frontend  run on localhost:5176 and 
            #your backend on localhost:5000. Without CORS,the browser blocks requests between them. 
            
    
  
    db.init_app(app) 
    
    
    app.register_blueprint(user_bp,url_prefix = '/userDetails')
    
    
    return app