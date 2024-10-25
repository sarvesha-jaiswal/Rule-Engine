from app.utils import create_rule, evaluate_rule

def test_create_rule():
    rule = create_rule("(age > 30 AND department == 'Sales')")
    assert rule.left.value == "AND"
    assert rule.left.left.value == "age > 30"

def test_evaluate_rule():
    rule = create_rule("(age > 30 AND department == 'Sales')")
    user_data = {"age": 35, "department": "Sales"}
    assert evaluate_rule(rule, user_data) == True
