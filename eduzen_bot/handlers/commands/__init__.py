from handlers.commands.questions import q_menu
from handlers.commands.commands import (
    btc,
    caps,
    ayuda,
    dolar,
    start,
    expense,
    get_questions,
    get_users,
    add_question,
    add_answer,
    cotizaciones,
    weather,
    code,
    subte,
    subte_novedades,
    remove_question,
    edit_question,
)

COMMANDS = {
    "btc": btc,
    "caps": caps,
    "ayuda": ayuda,
    "dolar": dolar,
    "start": start,
    "users": get_users,
    "questions": get_questions,
    "gasto": expense,
    "add_question": add_question,
    "add_answer": add_answer,
    "edit_question": edit_question,
    "remove": remove_question,
    "cambio": cotizaciones,
    "clima": weather,
    "code": code,
    "subte": subte,
    "subtenews": subte_novedades,
    "question_menu": q_menu,
    "qmenu": q_menu,
}