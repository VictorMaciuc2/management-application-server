from flask import Blueprint

deps = Blueprint('deps',__name__)


@deps.route('/departments',methods=['GET'])
def getall():
    #return jsonify(...)
    return 'im getting here ok'