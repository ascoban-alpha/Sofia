from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, FSInputFile
import asyncio

 
API_TOKEN = "8397516378:AAGetkXq8aAVpFft3OyLTtPGNwazBQE1NXs"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

image = "https://www.google.com/imgres?q=pdp%20junior%20logo&imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D547656810968941&imgrefurl=https%3A%2F%2Fwww.facebook.com%2Fphoto.php%3Ffbid%3D547656810968941%26set%3Da.190118510056108%26type%3D3&docid=vSrLWcjjq9kUSM&tbnid=SaqI8LqrS9kxKM&vet=12ahUKEwin-JiA05uPAxW9FxAIHY-dAiYQM3oECBkQAA..i&w=640&h=640&hcb=2&ved=2ahUKEwin-JiA05uPAxW9FxAIHY-dAiYQM3oECBkQAA"

list_images = ["safiafill2.jpg", "safiafill3.jpg", "safiafill4.jpg", "safiafill5.jpg", "safiafill6.jpg"]

def menu():
        button = KeyboardButton(text="🏙Kompaniya haqida")
        button2 = KeyboardButton(text="📍Filiallar")
        # button3 = KeyboardButton(text="🎒Bo'sh ish o'rinlar")
        button4 = KeyboardButton(text="Menyu")
        button5 = KeyboardButton(text="🗣Yangiliklar")
        button6 = KeyboardButton(text="📞Kontaktlar/Manzil")
        button7 = KeyboardButton(text=" 🇺🇿/🏴󠁧󠁢󠁥󠁮󠁧󠁿Til")

        rkm = ReplyKeyboardMarkup(
            keyboard=[
                 [button, button2,],     [button4, button5], [button6, button7],
            ],
            resize_keyboard=True
        )
        return rkm

def menu_eng():
        button = KeyboardButton(text="🏙About company")
        button2 = KeyboardButton(text="📍Branches")
        # button3 = KeyboardButton(text="🎒Bo'sh ish o'rinlar")
        button4 = KeyboardButton(text="Menu")
        button5 = KeyboardButton(text="🗣News")
        button6 = KeyboardButton(text="📞Contacts/Address")
        button7 = KeyboardButton(text=" 🇺🇿/🏴󠁧󠁢󠁥󠁮󠁧󠁿Language")

        rkm = ReplyKeyboardMarkup(
            keyboard=[
                 [button, button2,],     [button4, button5], [button6, button7],
            ],
            resize_keyboard=True
        )
        return rkm

def menyu():
        button = KeyboardButton(text="Мини торт Вишенка")
        button2 = KeyboardButton(text="Торт Адмирал")
        button3 = KeyboardButton(text="Торт Барби")
        button4 = KeyboardButton(text="Торт Баунти")
        button5 = KeyboardButton(text="🔙Ortga")


        rkm = ReplyKeyboardMarkup(
            keyboard=[
                 [button, button2], [button3, button4], [button5]
            ],
            resize_keyboard=True
        )
        return rkm

def menyu_eng():
        button = KeyboardButton(text="Mini Cherry Cake")
        button2 = KeyboardButton(text="Admiral Cake")
        button3 = KeyboardButton(text="Barbie cake")
        button4 = KeyboardButton(text="Bounty Cake")
        button5 = KeyboardButton(text="🔙Back")


        rkm = ReplyKeyboardMarkup(
            keyboard=[
                 [button, button2], [button3, button4], [button5]
            ],
            resize_keyboard=True
        )
        return rkm

def til():
        button = KeyboardButton(text="🇺🇿 Uzbek tili")
        button2 = KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English")
        button3 = KeyboardButton(text="🔙Ortga")


        rkm = ReplyKeyboardMarkup(
            keyboard=[
                 [button, button2], [button3],
            ],
            resize_keyboard=True
        )
        return rkm

def til_eng():
        button = KeyboardButton(text="🇺🇿 Uzbek Language")
        button2 = KeyboardButton(text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English")
        button3 = KeyboardButton(text="🔙Back")


        rkm = ReplyKeyboardMarkup(
            keyboard=[
                 [button, button2], [button3],
            ],
            resize_keyboard=True
        )
        return rkm




@dp.message(Command("start"))
async def menu_handler(message: types.Message):
    image = FSInputFile("safia.jpg")
    await message.answer_photo(
        photo=image,
        reply_markup=menu()
    )

@dp.message(F.text == "🏙Kompaniya haqida")
async def menu_handler(message: types.Message):
    image = FSInputFile("safia.jpg")
    await message.answer_photo(
        photo=image,
        caption=(
            "Safia Cafe & Bakery — bu haqiqiy oilaviy afsonaga va O‘zbekistonning eng yirik qandolat brendiga "
            "aylangan pishiriqqa bo‘lgan katta muhabbat haqidagi ilhomlantiruvchi hikoya.\n\n"
            "Hammasi 2001-yilda Muxayyo Ayupova va uning qizi Madina Ayupova tomonidan tashkil etilgan "
            "kichik oilaviy ustaxonadan boshlandi. Ularning shirin durdonalarni yaratishga bo‘lgan ishtiyoqi "
            "tezda birinchi mijozlarning qalbini zabt etdi. Olti yil o‘tgach, Madina o‘zining birinchi do‘konini ochdi, "
            "u yerda u butun oilani jalb qilib, sevimli kasbini ruh va ilhom bilan rivojlantirdi."
        ),
        reply_markup=menu()
    )

@dp.message(F.text == "🏙About company")
async def menu_handler(message: types.Message):
    image = FSInputFile("safia.jpg")
    await message.answer_photo(
        photo=image,
        caption=(
    "\"Safia Cafe & Bakery\" is an inspiring story about a great love for pastries "
    "that has turned into a true family legend and one of Uzbekistan’s largest confectionery brands.\n\n"
    "It all began in 2001, when Mukhayyo Ayupova and her daughter Madina Ayupova founded "
    "a small family workshop. Their passion for creating sweet masterpieces quickly won "
    "the hearts of their first customers. Six years later, Madina opened her first store, "
    "where she involved the whole family and continued to grow her beloved craft with spirit and inspiration."
        ),
        reply_markup=menu_eng()
    )


@dp.message(F.text == "📍Filiallar")
async def filiallar_handler(message: types.Message):
    image = FSInputFile("safiafill1.jpg")
    caption_text = (
        "🧁 <b>SAFIA BAKERY</b> — O‘zbekistonda mashhur qandolatlar tarmog‘i.\n\n"
        "Hozirda <b>145 dan ortiq filial</b> faoliyat yuritmoqda: Toshkent markazidagi "
        "Chorsu, Sebzor, Ko‘kcha, Xast Imom va boshqa ko‘plab joylarda. "
        "Har kuni ertalabdan kechgacha yangi shirinliklar pishiriladi va "
        "mijozlarimizga iliq xizmat ko‘rsatiladi.\n\n"
        "🕒 Ish vaqti: <b>08:00–23:00</b>\n"
        "🚗 Yetkazib berish: <b>09:00–22:00</b>\n\n"
        "🌐 Bizning sayt: <a href='https://www.safiabakery.uz'>safiabakery.uz</a>\n"
        "📲 Telegram: @safiabakery"
    )

    await message.answer_photo(
        photo=image,
        caption=caption_text,
        parse_mode="HTML",
        reply_markup=menu()
    )


@dp.message(F.text == "📍Branches")
async def filiallar_handler(message: types.Message):
    image = FSInputFile("safiafill1.jpg")
    caption=(
        "🧁 <b>SAFIA BAKERY</b> — one of the most famous confectionery chains in Uzbekistan.\n\n"
        "Today, we have <b>over 145 branches</b> operating across the country — including locations "
        "in central Tashkent such as Chorsu, Sebzor, Ko‘kcha, Khast Imom, and many others. "
        "Every day from morning till night, we bake fresh pastries and provide warm, friendly service "
        "to our valued customers.\n\n"
        "🕒 Working hours: <b>08:00–23:00</b>\n"
        "🚗 Delivery: <b>09:00–22:00</b>\n\n"
        "🌐 Our website: <a href='https://www.safiabakery.uz'>safiabakery.uz</a>\n"
        "📲 Telegram: @safiabakery"
)


    await message.answer_photo(
        photo=image,
        caption=caption,
        parse_mode="HTML",
        reply_markup=menu_eng()
    )


@dp.message(F.text == "🔙Ortga")
async def menu_handler(message: types.Message):
    await message.answer("🔙Ortga",reply_markup=menu())

@dp.message(F.text == "🔙Back")
async def menu_handler(message: types.Message):
    await message.answer("🔙Back",reply_markup=menu_eng())


@dp.message(F.text == "Menyu")
async def menu_handler(message: types.Message):
    image = FSInputFile("menubosganda.png")
    await message.answer_photo(
        photo=image,
        caption=("Tortlar"),
        reply_markup=menyu()
    )

@dp.message(F.text == "Menu")
async def menu_handler(message: types.Message):
    image = FSInputFile("menubosganda.png")
    await message.answer_photo(
        photo=image,
        caption=("Cakes"),
        reply_markup=menyu_eng()
    )

@dp.message(F.text == "Мини торт Вишенка")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "🍒 <b>Мини торт Вишенка</b>\n\n"
            "Песочное тесто с классическим ганашом и вишней сверху.\n"
            "💰 Цена: <b>115 000 сум</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu()
    )

@dp.message(F.text == "Mini Cherry Cake")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "🍒 <b>Mini Cake “Cherry”</b>\n\n"
            "Shortcrust pastry with classic ganache and a cherry on top.\n"
            "💰 Price: <b>115,000 UZS</b>"
        ),        
        parse_mode="HTML",
        reply_markup=menyu_eng()
    )

@dp.message(F.text == "Торт Адмирал")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort2.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>Торт Адмирал</b>\n\n"
            "4 вида бисквита: ванильный, ореховый, маковый и\n"
            "💰 Цена: <b>299 000 сум</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu()
    )

@dp.message(F.text == "Admiral Cake")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort2.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>Admiral Cake</b>\n\n"
            "Four types of sponge cake: vanilla, nut, and poppy seed.\n"
            "💰 Price: <b>299,000 UZS</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu_eng()
    )

@dp.message(F.text == "Торт Барби")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort3.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>Торт Барби</b>\n\n"
            "Белый бисквит, пропитанный ягодной\n"
            "💰 Цена: <b>299 000 сум</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu()
    )

@dp.message(F.text == "Barbie cake")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort3.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>Barbie Cake</b>\n\n"
            "White sponge cake soaked in berry syrup.\n"
            "💰 Price: <b>299,000 UZS</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu_eng()
    )

@dp.message(F.text == "Торт Баунти")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort4.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>Торт Баунти</b>\n\n"
            "Шоколадный бисквит, пропитанный шоколадной\n"
            "💰 Цена: <b>259 000 сум</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu()
    )

@dp.message(F.text == "Bounty Cake")
async def menu_handler(message: types.Message):
    image = FSInputFile("tort4.png")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>Bounty Cake</b>\n\n"
            "Chocolate sponge cake soaked in rich chocolate syrup.\n"
            "💰 Price: <b>259,000 UZS</b>"
        ),
        parse_mode="HTML",
        reply_markup=menyu_eng()
    )

@dp.message(F.text == "🗣Yangiliklar")
async def menu_handler(message: types.Message):
    await message.answer(
        text="Hozircha yangiliklar yo‘q",
        reply_markup=menu()
    )

@dp.message(F.text == "🗣News")
async def menu_handler(message: types.Message):
    await message.answer(
        text="Haven't got any news yet",
        reply_markup=menu_eng()
    )

@dp.message(F.text == "📞Kontaktlar/Manzil")
async def menu_handler(message: types.Message):
    image = FSInputFile("safiafill1.jpg")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>TINCHLIK</b>\n"
            "Olmazor tumani, Beruniy ko'chasi 88\n\n"
            "<b>📞 Nomer telefoni:</b> +998 78 113-40-40\n"
            "<b>🕒 Ish vaqti:</b> 08:00–22:00"
        ),
        parse_mode="HTML",
        reply_markup=menu()
    )

@dp.message(F.text == "📞Contacts/Address")
async def menu_handler(message: types.Message):
    image = FSInputFile("safiafill1.jpg")
    await message.answer_photo(
        photo=image,
        caption=(
            "<b>TINCHLIK</b>\n"
            "Olmazor District, 88 Beruniy Street\n\n"
            "<b>📞 Phone number:</b> +998 78 113-40-40\n"
            "<b>🕒 Working hours:</b> 08:00–22:00"
        ),
        parse_mode="HTML",
        reply_markup=menu_eng()
    )

@dp.message(F.text == "🇺🇿/🏴󠁧󠁢󠁥󠁮󠁧󠁿Til")
async def menu_handler(message: types.Message):
    await message.answer("Tilni tanlang",
                          reply_markup=til())

@dp.message(F.text == "🇺🇿/🏴󠁧󠁢󠁥󠁮󠁧󠁿Language")
async def menu_handler(message: types.Message):
    await message.answer("Choose Language",
                          reply_markup=til_eng())

@dp.message(F.text == "🇺🇿 Uzbek tili")
async def menu_handler(message: types.Message):
    await message.answer("Til tanlangan",
                          reply_markup=menu())

@dp.message(F.text == "🇺🇿 Uzbek Language")
async def menu_handler(message: types.Message):
    await message.answer("Til tanlangan",
                          reply_markup=menu())
    
@dp.message(F.text == "🏴󠁧󠁢󠁥󠁮󠁧󠁿 English")
async def menu_handler(message: types.Message):
    await message.answer("Language selected",
                          reply_markup=menu_eng())


async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
