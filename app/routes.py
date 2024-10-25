from flask import Blueprint, request, jsonify
from app.utils import create_rule, evaluate_rule, dict_to_node  # Ensure this matches the functions in utils.py
from app.database import get_db
import json

rule_engine = Blueprint('rule_engine', __name__)

@rule_engine.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule_string = data['rule_string']
    ast = create_rule(rule_string)

    # Convert Node object to a dictionary using to_dict before serializing
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_text, ast_structure) VALUES (?, ?)", 
                   (rule_string, json.dumps(ast.to_dict())))  # Use to_dict here
    conn.commit()
    conn.close()

    return jsonify({"message": "Rule created successfully", "ast": ast.to_dict()})  # Use to_dict here as well


@rule_engine.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    ast_dict = data['ast']  # Get the AST dictionary
    user_data = data['user_data']

    # Convert the dictionary back to a Node object
    ast = dict_to_node(ast_dict)

    # Evaluate the rule using the Node object
    result = evaluate_rule(ast, user_data)

    return jsonify({"result": result})

