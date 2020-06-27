import config
from Auth.DBAuthHandler import getUser

# Get the application instance
connex_app = config.connex_app
flask_app = connex_app.app

# Configuring login functionality
config.lm.init_app(flask_app)

@config.lm.user_loader
def load_user(username):
    return getUser(username)

# Read the swagger.yml file to configure the endpoints
connex_app.add_api('swagger.yaml')

if __name__ == '__main__':
    connex_app.run(debug=True, host='127.0.0.1', port=5000)
