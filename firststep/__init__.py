from flask import Flask
from flask import render_template

def create_app():
    print("run: create_app()")
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/klook?charset=utf8'

    """ ROUTES INIT """
    from firststep.routes.base_route import base_bp
    from firststep.routes.pred_route import pred_bp

    app.register_blueprint(base_bp)
    app.register_blueprint(pred_bp)

    """ ERROR PAGE"""
    @app.errorhandler(404)
    def page_404(error):
        return render_template('/404.html'),404

    return app