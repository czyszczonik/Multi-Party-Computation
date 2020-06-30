import os
import connexion

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=os.path.join(basedir, "swagger/"))

# Get the underlying Flask app instance
app = connex_app.app
# Initialize login module
app.config['SECRET_KEY'] = b'\x99l\xdcT\xfb@\x87\x9ce\x15_k\x0e\x7f\x02\xa4'
app.config['JWT_SECRET_KEY'] = b'\x9ce\x15_k\x0e\x7f\x02\xa4\x99l\xdcT\xfb@\x87'