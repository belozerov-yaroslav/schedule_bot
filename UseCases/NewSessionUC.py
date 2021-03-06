from random import choice

from ORM.SqlalchemyOperator import SqlalchemyOperator
from controllers.message import Message
from UseCases.UseCase import UseCase


class NewSessionUC(UseCase):
    with open('../UseCases/tips.txt', encoding='utf8') as file:
        tips = list(map(lambda tip: tip.strip(), file.readlines()))

    def new_user(self):
        self.message.set_text('''Привет! Вы можете создать напоминание с помощью команды
                              "Алиса, создай напоминание на дата время, текст напоминания"
                              Если вы хотите узнать, что у вас запланировано на день, то попросите:
                            "Алиса, что у меня запланировано на дата"''')
        self.repository.add_user(self.message.user_id())

    def old_user(self):
        self.message.set_text(f'Здравствуйте. {choice(self.tips)} Я вас слушаю...')
        self.repository.update_user_info(self.repository.get_user(self.message.user_id()))

    def handle(self):
        if self.repository.user_is_created(self.message.user_id()):
            self.old_user()
        else:
            self.new_user()
