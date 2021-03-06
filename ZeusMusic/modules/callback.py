# ZeusMusic (Telegram bot project)
# Copyright (C) 2021  Sathishzus & Bharathi2003

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from ZeusMusic.helpers.decorators import authorized_users_only
from ZeusMusic.config import BOT_NAME, BOT_USERNAME, OWNER, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from ZeusMusic.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ **๐ช๐ฒ๐น๐ฐ๐ผ๐บ๐ฒ**\n
๐ฏ๏ธ{BOT_NAME} ๐ฎ๐น๐น๐ผ๐ ๐๐ผ๐ ๐๐ผ ๐ฝ๐น๐ฎ๐ ๐บ๐๐๐ถ๐ฐ ๐ผ๐ป ๐ด๐ฟ๐ผ๐๐ฝ๐ ๐๐ต๐ฟ๐ผ๐๐ด๐ต ๐๐ต๐ฒ ๐ป๐ฒ๐ ๐ง๐ฒ๐น๐ฒ๐ด๐ฟ๐ฎ๐บ'๐ ๐๐ผ๐ถ๐ฐ๐ฒ ๐ฐ๐ต๐ฎ๐๐ !\n
๐ก ๐๐ถ๐ป๐ฑ ๐ผ๐๐ ๐ฎ๐น๐น ๐๐ต๐ฒ ๐๐ผ๐'๐ ๐ฐ๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฎ๐ป๐ฑ ๐ต๐ผ๐ ๐๐ต๐ฒ๐ ๐๐ผ๐ฟ๐ธ ๐ฏ๐ ๐ฐ๐น๐ถ๐ฐ๐ธ๐ถ๐ป๐ด ๐ผ๐ป ๐๐ต๐ฒ ยป ๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !
<b>""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โ ๐ฐ๐๐ ๐๐ ๐๐ ๐ข๐๐๐ ๐ถ๐๐๐๐ โ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],
                [
                    InlineKeyboardButton(
                        "๐ ๐๐ผ๐บ๐บ๐ฎ๐ป๐ฑ๐ ๐ฏ๐๐๐๐ผ๐ป !", callback_data="cbhelp")
                ],
                [
                   InlineKeyboardButton(
                       "๐ฅ แดาาษชแดษชแดส ษขสแดแดแด", url=f"https://t.me/ZeusSupport"
                   ),
                   InlineKeyboardButton(
                       "๐ฃ แดแดแดแดแดแดs แดสแดษดษดแดส", url=f"https://t.me/ZeusBotsNetwork"
                   )
                ],
                [
                    InlineKeyboardButton(
                        "๐แดแดแด?แดสแดแดแดส", callback_data="cbguide")
                ],
            ]
        ),
        disable_web_page_preview=True
        )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>
In this menu you can open several **Available Command** menus, in each command menu there is also a brief explanation of each **Command**
๐ by **@ZeusBotsNetwork**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ สแดsษชแด แดแดแด", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ แดแดแด?แดษดแดแดแด แดแดแด", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ แดแดแดษชษด แดแดแด", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ sแดแดแด แดsแดสs", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ แดแดกษดแดส แดแดแด", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฌสแดแดแด", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ here is the basic commands</b>
๐ง [ GROUP VC CMD ]
/play (song name) - play song from youtube
/ytp (song name) - play song directly from youtube 
/stream (reply to audio) - play song using audio file
/player - show the list song in queue
/song (song name) - download song from youtube
/search (video name) - search video from youtube detailed
/vsong (video name) - download video from youtube detailed
/lyric - (song name) lyrics scrapper
๐ง [ CHANNEL VC CMD ]
/cplay - stream music on channel voice chat
/cplayer - show the song in streaming
/cpause - pause the streaming music
/cresume - resume the streaming was paused
/cskip - skip streaming to the next song
/cend - end the streaming music
/admincache - refresh the admin cache
/ubjoinc - invite the assistant for join to your channel
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ here is the advanced commands</b>
/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/stats - show the bot statistic
/cache - refresh the admin cache
/restart - restart the bot without affecting music plays
/ping - check the bot ping status
/uptime - check the bot uptime status
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ here is the admin commands</b>
/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ here is the sudo commands</b>
/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/rmr - to delete all the downloaded files and caches
/frestart - to force restart bots server
/logs - send logs file
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ here is the owner commands</b>
/broadcast - send a broadcast message from bot
๐ note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )





@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**๐ก here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "โธ Pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "โถ๏ธ Resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โฉ Skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "โน End", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "โ Anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>This is the feature information :</b>
๐ก **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.
and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.
โ **usage:**
1๏ธโฃ ban & temporarily ban user from your group:
   ยป type `/b username/reply to message` ban permanently
   ยป type `/tb username/reply to message/duration` temporarily ban user
   ยป type `/ub username/reply to message` to unban user
2๏ธโฃ mute & temporarily mute user in your group:
   ยป type `/m username/reply to message` mute permanently
   ยป type `/tm username/reply to message/duration` temporarily mute user
   ยป type `/um username/reply to message` to unmute user
๐ note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>This is the feature information :</b>
        
**๐ก Feature:** delete every commands sent by users to avoid spam in groups !
โ usage:**
 1๏ธโฃ to turn on feature:
     ยป type `/delcmd on`
    
 2๏ธโฃ to turn off feature:
     ยป type `/delcmd off`
      
โ๐?๐จ๐๐ฃ๐๐ ๐น๐ช : โค๐๐ฆ๐ค ๐น๐?๐ฅ๐ค โ๐๐ฅ๐จ๐?๐ฃ๐""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "สแดแดแด", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>๐ก Hello there, welcome to the help menu !</b>
**In this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**
๐ค Bots by **@ZeusBotsNetwork**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "๐ Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "๐ Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "๐ก BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
