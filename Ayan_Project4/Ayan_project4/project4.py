def generate_flask_service(entity_name, action):
    code = f"""
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    @app.route('/{entity_name}', methods=['POST'])
    def {action}_{entity_name}():
        data = request.get_json()
        return jsonify(data), 201

    if __name__ == '__main__':
        app.run(debug=True)
    """
    return code

# Example usage
entity = "order"
action = "add"
service_code = generate_flask_service(entity, action)
print(service_code)
