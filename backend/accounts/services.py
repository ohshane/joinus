import logging
import uuid
from typing import Dict, Str

from .models import User

logger = logging.getLogger(__name__)

class UserAccountService:

    @staticmethod
    def get_user(*, id: uuid.UUID) -> Dict:
        user = User.objects.get(id=id)
        return {
            'id': user.id,
            'account_id': user.account_id,
            'nickname': user.nickname,
        }

    @staticmethod
    def create_user(*, account_id: Str, nickname: Str) -> Dict:
        logger.info('Creating user')
        user = User.objects.create(account_id=account_id, nickname=nickname)
        return {
            'id': user.id,
            'account_id': user.account_id,
            'nickname': user.nickname,
        }

    @staticmethod
    def update_user_nickname(*, id: uuid.UUID, nickname: Str) -> Dic:
        logger.info('Updating user nickname')
        user = User.objects.get(id=id).update(nickname=nickname)
        return {
            'id': user.id,
            'account_id': user.account_id,
            'nickname': user.nickname,
        }
