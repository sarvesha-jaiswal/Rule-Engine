from app.models import Node

def create_rule(rule_string):
    # Create AST for the given rule string
    root = Node("operator", "OR")
    root.left = Node("operator", "AND", 
                     Node("operand", "age > 30"), 
                     Node("operand", "department == 'Sales'"))
    root.right = Node("operand", "salary > 50000")
    return root

# Other functions like evaluate_rule and dict_to_node should also be present here


# Helper function to convert a dict back to a Node object
def dict_to_node(data):
    if data is None:
        return None

    # Create a Node object from the dictionary
    node = Node(data['type'], data['value'])

    # Only operator nodes (AND, OR) will have left and right children
    if data['type'] == "operator":
        node.left = dict_to_node(data.get('left'))  # Recursively build left child
        node.right = dict_to_node(data.get('right'))  # Recursively build right child

    return node

def evaluate_rule(node, user_data):
    if node.type == "operand":
        return eval(node.value, {}, user_data)  # Evaluate condition using user data
    elif node.type == "operator":
        if node.value == "AND":
            return evaluate_rule(node.left, user_data) and evaluate_rule(node.right, user_data)
        elif node.value == "OR":
            return evaluate_rule(node.left, user_data) or evaluate_rule(node.right, user_data)
