import config
from flask_jwt_extended import JWTManager

# Get the application instance
connex_app = config.connex_app
flask_app = connex_app.app
flask_app = JWTManager(flask_app)


# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yaml')

if __name__ == '__main__':
    connex_app.run(debug=True, host='0.0.0.0', port=5000)
