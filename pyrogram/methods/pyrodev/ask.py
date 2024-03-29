#  Pyrogram-Dev - Telegram MTProto API Client Library for Python
#  Copyright (C) 2024-present Aditya <https://github.com/AdityaHalder>
#
#  This file is part of Pyrogram-Dev.
#
#  Pyrogram-Dev is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram-Dev is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram-Dev.  If not, see <http://www.gnu.org/licenses/>.


from typing import Optional, Union

import pyrogram
from pyrogram.filters import Filter
from pyrogram.types import ListenerTypes


class Ask:
    async def ask(
        self: "pyrogram.Client",
        chat_id: Union[Union[int, str], list[Union[int, str]]],
        text: str,
        filters: Optional[Filter] = None,
        listener_type: ListenerTypes = ListenerTypes.MESSAGE,
        timeout: Optional[int] = None,
        unallowed_click_alert: bool = True,
        user_id: Optional[Union[int, str, list[Union[int, str]]]] = None,
        message_id: Optional[Union[int, list[int]]] = None,
        inline_message_id: Optional[Union[str, list[str]]] = None,
        *args,
        **kwargs,
    ):
        """
        Sends a message and waits for a response.

        Parameters:
            chat_id (``Union[int, str], List[Union[int, str]]``):
                The chat ID(s) to wait for a message from. The first chat ID will be used to send the message.

            text (``str``):
                The text to send.

            filters (``Optional[Filter]``):
                Same as :meth:`pyrogram.Client.listen`.

            listener_type (``ListenerTypes``):
                Same as :meth:`pyrogram.Client.listen`.

            timeout (``Optional[int]``):
                Same as :meth:`pyrogram.Client.listen`.

            unallowed_click_alert (``bool``):
                Same as :meth:`pyrogram.Client.listen`.

            user_id (``Optional[Union[int, str], List[Union[int, str]]]``):
                Same as :meth:`pyrogram.Client.listen`.

            message_id (``Optional[Union[int, List[int]]]``):
                Same as :meth:`pyrogram.Client.listen`.

            inline_message_id (``Optional[Union[str, List[str]]]``):
                Same as :meth:`pyrogram.Client.listen`.

            args (``Any``):
                Additional arguments to pass to :meth:`pyrogram.Client.send_message`.

            kwargs (``Any``):
                Additional keyword arguments to pass to :meth:`pyrogram.Client.send_message`.

        Returns:
            Same as :meth:`pyrogram.Client.listen`. The sent message is returned as the attribute ``sent_message``.
        """
        sent_message = None
        if text.strip() != "":
            chat_to_ask = chat_id[0] if isinstance(chat_id, list) else chat_id
            sent_message = await self.send_message(chat_to_ask, text, *args, **kwargs)

        response = await self.listen(
            filters=filters,
            listener_type=listener_type,
            timeout=timeout,
            unallowed_click_alert=unallowed_click_alert,
            chat_id=chat_id,
            user_id=user_id,
            message_id=message_id,
            inline_message_id=inline_message_id,
        )
        if response:
            response.sent_message = sent_message

        return response
