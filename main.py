from bs4 import BeautifulSoup
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram import Bot, Dispatcher, types
from kb import Main_keyboard, Color_keyboard, Digit_keyboard, Gis_keyboard
import g4f, requests, logging

color_map = {
    "🟦": "Бумаги и картона", 
    "🟩": "Органические отходы или пищевые отходы", 
    "🟥": "Опасные отходы, такие как батарейки, лампы и медицинские отходы", 
    "🟧": "Опасные отходы, такие как батарейки, лампы и медицинские отходы", 
    "🟨": "Пластиковые бутылки, контейнеры и упаковка",
    }

digit_map = {
   "1️⃣": {
        "description": "Полиэтилен терефталата (PET) - широко используется в производстве бутылок для напитков, упаковок для продуктов питания, контейнеров для косметических средств и прочих товаров. Также может использоваться для производства волокон для одежды и домашнего текстиля. ",
        "image": "./img/1.png",
    },
    "2️⃣": {
        "description": "Полипропилен низкой плотности (ПНД) - используется в производстве пищевых пленок, мешков для мусора, пакетов для упаковки продуктов, пакетов для хранения одежды, игрушек и т.д.",
        "image": "./img/2.png",
    },
    "3️⃣": {
        "description": "Поливинилхлорид (PVC) - используется в производстве оконных профилей, труб, кабельных изделий, пленок для упаковки, сумок, обуви, мебели, стеновых панелей, каркасов для зонтиков и прочих товаров.",
        "image": "./img/3.png",
    },
    "4️⃣": {
        "description": "Полиэтилен высокой плотности (ПВХ) - широко используется в производстве пластиковых бутылок для молока, воды, сока, а также в упаковке косметических средств, бытовой химии и прочих товаров.",
        "image": "./img/4.png",
    },
    "5️⃣": {
        "description": "Полипропилен (PP) - широко используется в производстве упаковочных материалов, в том числе контейнеров, пищевых коробок, пакетов, крышек, крышек для бутылок, косметических бутылок, автомобильных деталей и т.д.",
        "image": "./img/5.png",
    },
    "6️⃣": {
        "description": "Полистирол (PS) - часто используется в производстве различных пластиковых изделий, включая пищевые контейнеры, стаканы, крышки для стаканов, игрушки, упаковки, изделия для медицины, бытовые принадлежности и т.д.",
        "image": "./img/6.png",
    },
    "7️⃣": {
        "description": "Акрилонитрил-бутадиен-стирол (ABS) - применяется в производстве автомобильных деталей, электроники, бытовых приборов, игрушек, мебели, бутылок и прочих изделий.",
        "image": "./img/7.png",
    },
}

API_TOKEN = "6232142718:AAGtjHPrJJPfAWGztHk-RzwKiTeMWHH4xFc"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.answer(
        "Привет! Я бот для работы с экологическим продуктом. "
        "Отправьте мне свой запрос, чтобы начать работу.",
        reply_markup=Main_keyboard,
    )

@dp.message_handler(lambda message: message.text == "🔄 Вернуться в главное меню")
async def back_menu(message: types.Message):
    await message.answer("Назад в главное меню", reply_markup=Main_keyboard)

@dp.message_handler(lambda message: message.text == "♻️ Узнать цветовой маркер отходов")
async def Marker(message: types.Message):
    await message.answer("Выберите цвет урны", reply_markup=Color_keyboard)
    await message.delete()

@dp.message_handler(lambda message: message.text in color_map.keys())
async def handle_color(message: types.Message):
    color = color_map[message.text]
    await message.answer(color)
    await message.delete()


@dp.message_handler(lambda message: message.text == "❔ Задать вопрос экспертам")
async def send_random_value(message: types.Message):
    response = f'Вы можете задать свой вопрос экспертам по экологии, указав команду и написав в нем ваш вопрос. К примеру: " /q Можете подсказать, как правильно разделять мусор?"'
    await message.answer(response)
    await message.delete()

@dp.message_handler(commands=["q"])
async def send_q_expert(message: types.Message):
    question = message.text.split(maxsplit=1)
    response = f"Вопрос от пользователя {message.from_user.full_name} : {question}"
    await bot.send_message("@ecologisticsexpert", response)
    await message.answer("Ваш вопрос отправлен эксперту, ожидайте ответа.")

@dp.message_handler(lambda message: message.text == "🔢 Коды переработки")
async def send_random_value(message: types.Message):
    await message.answer(
        "♻️ Для обеспечения утилизации одноразовых предметов была разработана система маркировки для всех видов пластика и идентификационные коды. "
        "Маркировка пластика состоит из 3-х стрелок в форме треугольника, внутри которых находится число, обозначающая тип пластика.",
        reply_markup=Digit_keyboard,
    )
    await message.delete()

@dp.message_handler(lambda message: message.text in digit_map.keys())
async def handle_digit(message: types.Message):
    digit_key = message.text

    if digit_key in digit_map:
        item = digit_map[digit_key]
        description = item['description']
        image_path = item['image']
        with open(image_path, 'rb') as photo:
            # Send the photo with the description as caption
            await bot.send_photo(chat_id=message.from_user.id, photo=photo, caption=description)
    else:
        # Если товар не найден, отправляем сообщение об ошибке
        await message.answer("Извините, я не знаю такой товар.")
    await message.delete()


@dp.message_handler(lambda message: message.text == "Узнать качества воздуха")
async def msg_air_quality(message: types.Message):
    url = "https://www.iqair.com/kazakhstan/astana"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        aqi_value = soup.find('p', class_='aqi-value__value').text
        air_quality_status = soup.find('span', class_='aqi-status__text').text
        website_url = url

        result = f"Индекс качества: {aqi_value}\nКачество воздуха: {air_quality_status}\nСсылка на [сайт]({website_url})"
    else:
        result = {f"Ошибка при запросе: {response.status_code}"}
    
    await message.answer(result, parse_mode='Markdown')

@dp.message_handler(commands=["gpt"])
async def cmd_gpt(message: types.Message):
    try:
        typing_message = await message.answer("Печатает...") 
        user_text = message.text.split("/gpt ", 1)[1]
        response = await g4f.ChatCompletion.create_async(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Напиши короткий ответ {user_text}"}],
        )
        
        await typing_message.delete()
        await message.answer(response) 
        
    except Exception as e:
        print(f"Ошибка: {e}")
        await typing_message.delete()

@dp.message_handler(lambda message: message.text == "💡 Советы")
async def send_cafe_location(message: types.Message):
    await message.answer("Для того чтобы написать ИИ напишите команду и ваш текст, к примеру"
                         "'/gpt Какие есть экологические проблемы каспийского море, и как их решить'") 


@dp.message_handler(lambda message: message.text == "📍 Узнать ближайшие пункты приема вторсырья")
async def Gis_to_map(message: types.Message):
    await message.answer("Пожалуйста выберите сырье, которое нужно сдать",
        reply_markup=Gis_keyboard,
    )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)