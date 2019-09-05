from flask import abort
from flask_restful import Resource
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError

from .. import api, db
from ..models import User
from ..oauth import twitch_blueprint

@api.resource('/api/me')
class ApiMe(Resource):
    def get(self):
        if not twitch_blueprint.session.authorized:
            abort(401, 'Not Authorized')

        tb_users = None
        try:
            tb_users = twitch_blueprint.session.get("users")
            if not tb_users.ok:
                abort(401, 'Not Authorized')
        except TokenExpiredError:
            abort(401, 'Token Expired')

        twitch_id = tb_users.json().get('data')[0].get('id')
        user = User.query.filter_by(twitch_id=twitch_id).first()
        if user:
            return user.json()
        user = User(twitch_id=twitch_id)
        db.session.add(user)
        db.session.commit()
        return user.json()
