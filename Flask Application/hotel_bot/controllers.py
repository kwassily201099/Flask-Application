from flask import (
    Blueprint, render_template
)

import random
import string
from .default import DEFAULT_SOURCE

controllers = Blueprint('controllers', __name__, url_prefix='/')
MAX_SOURCE_SIZE = 64000


@controllers.route("")
def index():
    return render_template("index.html", source=DEFAULT_SOURCE)


def make_unique_id(length):
    """Make a random string of any length."""
    return "".join(random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits) for _
                   in range(length))
