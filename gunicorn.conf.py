from dotenv import load_dotenv
from common.utils import get_env_var

load_dotenv()


wsgi_app = "simplex_api.wsgi"
bind = f"0.0.0.0:{get_env_var('PORT')}"
