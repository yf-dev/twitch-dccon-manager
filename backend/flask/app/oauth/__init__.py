from flask import redirect, url_for
from flask_dance import OAuth2ConsumerBlueprint
from flask_dance.consumer.storage.sqla import SQLAlchemyStorage

from .. import app, db
from ..models import TwitchOAuth

twitch_blueprint = OAuth2ConsumerBlueprint(
    "twitch",
    __name__,
    client_id=app.config.get("TWITCH_CLIENT_ID"),
    client_secret=app.config.get("TWITCH_CLIENT_SECRET"),
    base_url="https://api.twitch.tv/helix/",
    token_url="https://id.twitch.tv/oauth2/token",
    authorization_url="https://id.twitch.tv/oauth2/authorize",
    redirect_url=app.config.get('FRONTEND_HOME'),
    token_url_params={"include_client_id": True},
    scope=("user:read:email",),
    storage=SQLAlchemyStorage(TwitchOAuth, db.session),
)

app.register_blueprint(twitch_blueprint, url_prefix="/login")


@app.route("/login")
def login():
    return redirect(url_for("twitch.login"))

@app.route("/logout")
def logout():
    return redirect(url_for("logout_twitch"))

@app.route("/logout/twitch")
def logout_twitch():
    token = twitch_blueprint.token["access_token"]

    resp = twitch_blueprint.session.post(
        "https://id.twitch.tv/oauth2/revoke",
        params={"client_id": twitch_blueprint.client_id, "token": token}
    )
    assert resp.ok, resp.text
    del twitch_blueprint.token
    return redirect(app.config.get('FRONTEND_HOME'))
