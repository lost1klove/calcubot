from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import emoji

choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1️⃣', callback_data="move:1"),
            InlineKeyboardButton(text='2️⃣', callback_data="move:2"),
            InlineKeyboardButton(text='3️⃣', callback_data="move:3"),
            InlineKeyboardButton(text="➕", callback_data="move:+"),
        ],
        [
            InlineKeyboardButton(text="4️⃣", callback_data="move:4"),
            InlineKeyboardButton(text="5️⃣", callback_data="move:5"),
            InlineKeyboardButton(text="6️⃣", callback_data="move:6"),
            InlineKeyboardButton(text="➖", callback_data="move:-"),
        ],
        [
            InlineKeyboardButton(text="7️⃣", callback_data="move:7"),
            InlineKeyboardButton(text="8️⃣", callback_data="move:8"),
            InlineKeyboardButton(text="9️⃣", callback_data="move:9"),
            InlineKeyboardButton(text="✖️", callback_data="move:*"),
        ],
        [
            InlineKeyboardButton(text="🔹", callback_data="move:."),
            InlineKeyboardButton(text="0️⃣", callback_data="move:0"),
            InlineKeyboardButton(text="🟰", callback_data="move:="),
            InlineKeyboardButton(text="➗", callback_data="move:/"),
        ],
        [
            InlineKeyboardButton(text="⏪", callback_data="move:<"),
            InlineKeyboardButton(text="🔁", callback_data="move:C"),
        ],
    ]
)
