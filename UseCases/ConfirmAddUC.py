from random import choice

from ORM.SqlalchemyOperator import SqlalchemyOperator
from controllers.message import Message
from UseCases.UseCase import UseCase


def had_cmd(message: str, cmd_list):
    if isinstance(cmd_list, list):
        for cmd in cmd_list:
            if message.startswith(cmd):
                return True
        return False
    else:
        return message.startswith(cmd_list)


class ConfirmAddUC(UseCase):
    def confirm(self, sessionStorage):
        if had_cmd(self.message.get_cmd(), ['алиса да', 'да']):
            self.message.set_text('Напоминание добавлено.')
            sessionStorage[self.message.session['session_id']]['wait_for_confirm'] = False
            del sessionStorage[self.message.session['session_id']]['event']
        elif had_cmd(self.message.get_cmd(), ['алиса нет', 'нет']):
            self.message.set_text('Напоминание отменено.')
            sessionStorage[self.message.session['session_id']]['wait_for_confirm'] = False
            self.repository.delete_user_event(sessionStorage[self.message.session['session_id']]['event'])
            del sessionStorage[self.message.session['session_id']]['event']
        else:
            self.message.set_text('Пожалуйста, подтвердите добавление напоминания.')