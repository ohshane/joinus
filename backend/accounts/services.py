import logging
import uuid
from typing import Dict, Str

from .models import User

logger = logging.getLogger(__name__)

def get_user(*, id: uuid.UUID) -> Dict:
    user = User.objects.get(id=id)
    return {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
