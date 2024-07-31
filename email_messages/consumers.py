import json
from channels.generic.websocket import AsyncWebsocketConsumer

class EmailConsumer(AsyncWebsocketConsumer):
    # async def connect(self):
    #     await self.accept()
        
    #     # Логика получения писем и обновления прогресс-бара
    #     total_emails = 100  # Замените на актуальное количество писем
    #     for i in range(total_emails):
    #         await self.send(json.dumps({'progress': i + 1, 'total': total_emails}))
    #         # Логика задержки для имитации обработки
    #         await asyncio.sleep(0.1)

    # async def disconnect(self, close_code):
    #     pass

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Обработка получения сообщений и отправка данных на фронтенд
        await self.send(text_data=json.dumps({
            'message': f'Checked {data["checked"]} messages.',
            # Отправка данных о сообщениях, если они найдены
        }))

    