# 🐸 Pepe Helper
Бот, который реагирует на определенные сообщения (ошибки в ходе установки или использования ```telegram-raid-botnet``` и ```vk-raid-botnet```), ответами на эти ошибки))


![photo_2022-08-30_17-34-15](https://user-images.githubusercontent.com/85753549/187475924-369c6d4e-94ad-4204-9e55-6aa9b7767040.jpg)


### Установка

```bash
pip install aiogram  # Установить aiogram
```

Далее

```bash
pip install logging  # Установить logging
```

Затем

```bash
python3 bot.py # Запуск бота на сервере.
```

### Помощь
Если вы хотите добавить больше вариантов ответов, то можете написать мне в [Telegram](https://t.me/qqCommit) или напишите в Issues этого репозитория.


> Спасибо, за помощь Xi1se(y) с Aiogram.

### Функции

- [+] ```/admin``` - команда для админов
- [+] ```/help``` - команда, которая покажет ```help-list``` с командами и помощью.
- [+] Рассылка через бота, всем пользователям


## Примеры

```python
@dp.message_handler(text=['Ошибка'])
async def stats(message):
	await message.answer("Ответ")  
```
