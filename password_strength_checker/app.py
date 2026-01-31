from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def check_password_strength(password):
    """
    Analyze password strength and return strength level with feedback
    Levels: weak, mid, average, strong, very strong
    """
    if not password:
        return {"strength": "empty", "score": 0, "feedback": "Password cannot be empty"}
    
    score = 0
    feedback = []
    
    # Length checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")
    
    if len(password) >= 12:
        score += 1
    
    if len(password) >= 16:
        score += 1
    
    # Character variety checks
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
    
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Add numbers")
    
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Common patterns (bad signs)
    if re.search(r'(.)\1{2,}', password):  # Repeated characters
        score -= 1
        feedback.append("Avoid repeating characters")
    
    if re.search(r'(012|123|234|345|456|567|678|789|890|abc|bcd|cde|def)', password.lower()):
        score -= 1
        feedback.append("Avoid sequential patterns")
    
    # Determine strength level
    score = max(0, score)  # Ensure non-negative
    
    if score <= 1:
        strength = "weak"
    elif score <= 2:
        strength = "mid"
    elif score <= 4:
        strength = "average"
    elif score <= 6:
        strength = "strong"
    else:
        strength = "very strong"
    
    return {
        "strength": strength,
        "score": score,
        "feedback": feedback if feedback else ["Great password!"],
        "length": len(password)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json()
    password = data.get('password', '')
    result = check_password_strength(password)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
