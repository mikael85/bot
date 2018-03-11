import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent

logger = logging.getLogger()


def code_markdown(bot, update):
    query = update.inline_query.query

    if not query:
        return

    query = f"```\n{query}\n```"

    results = [
        InlineQueryResultArticle(
            id=uuid4().hex[:8],
            title='code',
            input_message_content=InputTextMessageContent(query, 'MARKDOWN')
        )
    ]
    bot.answer_inline_query(update.inline_query.id, results)