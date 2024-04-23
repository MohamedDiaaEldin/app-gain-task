
from flask import jsonify

def not_found_handler(message='Not Found'):
    return jsonify({
        'message':message
    }), 404

def unauthorized_handler(message='Unauthorized'):
    return jsonify({
        'message':message
    }), 401

def success_handler(message='Success'):
    return jsonify({
        'message':message
    }), 200
    
def conflict_handler(message='Conflict'):
    return jsonify({
        'message':message
    }), 409
    
def server_error_handler(message='Server Error'):
    return jsonify({
        'message':message
    }), 500
    
    
def invalid_request_handler(message='Invalid Request'):
    return jsonify({
        'message':message
    }), 400
    