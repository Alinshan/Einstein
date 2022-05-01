class script(object):
    START_TXT = """<b>Hello {}</b>

<i>Iam A Simple Auto Filter + Movie Search + Manual Filter Bot. I Can Provide Movies In Telegram Groups. You Can Search Movies Via Inline. I Can Also Add Filters In Telegram Groups.  Just Add Me To Your Group And Enjoy</i>"""
    HELP_TXT = """<b>Hᴇʟʟᴏ {}
Welcome to Help Area 1 🎁</b>"""
    HELOP_TXT = """<b>Hᴇʟʟᴏ {}
Welcome to Help Area 2 🎁</b>"""
    HELOOP_TXT = """<b>Hᴇʟʟᴏ {}
Welcome to Help Area 3 🎁</b>"""
    SPSHIVA_TXT = """<b><i>This Is The Module Page Info</i>

🔰 Your Taken Page Is 1/3 📖</b>"""
    SPSHIVA2_TXT = """<b><i>This Is The Module Page Info</i>

🔰 Your Taken Page Is 2/3 📖</b>"""
    SPSHIVA3_TXT = """<b><i>This Is The Module Page Info</i>

🔰 Your Taken Page Is 3/3 📖</b>"""
    ABOUT_TXT = """<b>🤖 𝖡ᴏᴛ ɴᴀᴍᴇ : <a href='http://t.me/Spidey_Autofilterbot'>sᴘɪᴅᴇʏ</a>

📝 𝖫ᴀɴɢᴜᴀɢᴇ : <a href='https://www.python.org/'>𝖯ʏᴛʜᴏɴ</a>

📚 𝖥ʀᴀᴍᴇᴡᴏʀᴋ : <a href='https://github.com/pyrogram/pyrogram'>𝖯ʏʀᴏɢʀᴀᴍ</a>

📡 𝖧ᴏsᴛᴇᴅ ᴏɴ : <a href='http://heroku.com/'>𝖧ᴇʀᴏᴋᴜ</a>

👨‍💻 𝖣ᴇᴠᴇʟᴏᴘᴇʀ : <a href='http://t.me/OGGY123kph'>𝖲ʜɪᴠᴀ</a>

📃 𝖲ᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : <a href='https://t.me/kgf_2_movie_r'>𝖢ʟɪᴄᴋ ʜᴇʀᴇ</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : <a href='https://t.me/Coby_Support'>𝖬𝖧 ʙᴏᴛs</a>

📢 𝖴ᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+NeK_dvXeatwyMWRl'>𝖬𝖧 ʙᴏᴛs</a></b>"""
    
    FILE_TXT = """➤ Help: File Store Module..🛃

<b><i>By Using This Module You Can Store Media,Files In My Database And I Will Give You A Permanent Link  To Access The Saved Media/Files.If You Want To Add Files From A Public Channel Send The File Link Only Or Want To Add Files From A Privet Channesl You Must Make Me Admin On The Channel To Access Media/Files...</i></b>

<b><i>⪼ Commands And Usage ›</i></b>

➪ /plink ›› <b>Replay To Any Media To Get Link</b>
➪ /pbatch ›› <b>Use Your Media Link With This Command.</b>
➪ /batch ›› <b>To Create A Link For Multiple Media</b>

<b><i>⪼ Example ›</i></b>
<code>/batch https://t.me/c/1541932075/4957 https://t.me/c/1541932075/4958</code>

<b>Credits</b> ›› <a href=https://t.me/moviehubgroupp><b>MH-UPDATES</b></a>"""
    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
•/whois :-give a user full details"""
    FUN_TXT ="""<b>Games</b> 
    
<b>⚡ Just Some Kind Of Fun Things ⚡</b>
 
𝟣. /dice - Role The Dice
𝟤. /Throw 𝗈𝗋 /Dart - To Make Dart
3. /Runs - Some Random Dialogues
4. /Goal or /Shoot - To Make A Goal Or Shoot 
5. /luck or /cownd - Spin And Try Your Luck"""
    DEPLOY_TXT = """<b>𝙷𝙾𝚆 𝚃𝙾 𝙳𝙴𝙿𝙻𝙾𝚈..?</b> 
  
<b>✮ Deploy Tutorial ››</b> <i><b>https://youtu.be/kB9TkCs8cX0</b></i>

<b>𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙷𝙴 𝙰𝙹𝙰𝚇-𝙿𝚁𝙾-𝙼𝙰𝚇 𝚁𝙴𝙿𝙾 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 <a href=https://t.me/Aadhi011>𝙰𝙰𝙳𝙷𝙸</a></b>

<b>𝚂𝙷𝙰𝚁𝙴 𝙰𝙽𝙳 𝚂𝚄𝙱𝚂𝙲𝚁𝙸𝙱𝙴</b>
𝙲𝚁𝙴𝙳𝙸𝚃𝚂 ›› <a href=https://t.me/MWUpdatez><b>𝙼𝚆-𝚄𝙿𝙳𝙰𝚃𝙴𝚉</b></a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ᗩᒍᗩ᙭  will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᗩᒍᗩ᙭ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>🎵 Song Download Module 🎵</b>

<i>Song Download Module, For Those Who Love Music. You Can Use This Feature For Download Any Song With Suoer Fast Speed...🚀</i>

<b>Commands</b>
››  /song Song Name

<b>📝 Credits :- <a href=https://t.me/MovieHubOtt>MH-Updates</a></b>"""
    PIN_TXT ="""<b>PIN MODULE</b>

<b>Pin A Message../</b>

<b>All The Pin Related Commands Can Be Found Here::</b>

<b>📌 Commands And Usage 📌</b>

◉ /pin :- To Pin The Message On Your Chat
◉ /unpin :- To Unpin Current Pinned Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

• /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

• These commands works on both pm and group.
• These commands can be used by any group member."""
    TTS_TXT = """Help: <b> TTS 🎤 module:</b>

Translate text to speech

<b>Commands and Usage:</b>

• /tts <text> : convert text to speech

<b>NOTE:</b>

• IMDb should have admin privillage.
• These commands works on both pm and group.
• IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>🌟 Ping:</b>

Helps you to know your ping 🚶🏼‍♂️

<b>Commands:</b>

• /alive - To check you are alive.
• /help - To get help.
• /ping - To get your ping.
• /repo - Source Code.
• /channel - Channel Details.
• /ajax - Bot Link.
<b>🏹Usage🏹 :</b>

• This commands can be used in pms and groups
• This commands can be used buy everyone in the groups and bots pm
• Share us for more features"""
    TELE_TXT = """<b>📚 HELP : Telegraph 🖼️</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

🤧 /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

• This Command Is Available in goups and pms
• This Command Can be used by everyone"""

    PRIVATEBOT_TXT = """<b>𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙱𝙾𝚃 𝙵𝙾𝚁 𝚈𝙾𝚄</b>
<b>›› 𝙳𝙾 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙰 𝙱𝙾𝚃 𝚂𝙰𝙼𝙴 𝙻𝙸𝙺𝙴 𝚃𝙷𝙸𝚂</b>
<b>›› 𝚆𝙸𝚃𝙷 𝙰𝙻𝙻 𝚈𝙾𝚄𝚁 𝙲𝚁𝙴𝙳𝙸𝚃𝚂</b>
<b>›› 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙾𝚆𝙽𝙴𝚁𝚂𝙷𝙸𝙿</b>
<b>›› 𝙲𝙾𝙽𝚃𝙰𝙲𝚃 𝙼𝙴 <a href=https://t.me/Aadhi011>𝙰𝙰𝙳𝙷𝙸</a></b>"""

    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>Purge</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

◉ /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

-sᴘɪᴅᴇʏ  Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. sᴘɪᴅᴇʏ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Spidey_Files)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>Auto Filter On/Off Module..</b>

<i>Auto Filter Is The Feature To Filter Any Saved The Files Automatically Channel To Group. You Can Use The Following Commands To On And Off The AutoFilter In Your Group...</i>

<b>COMMANDS :-
<b>›› /autofilter on - Enable Autofilter On Your Groups.</b>
<b>›› /autofilter off - Disabled Autofilter On Your Groups.</b>
<b>›› /set_template - Set Custom IMDB Templates For Auto Filter.</b>
<b>›› /get_template - Get Current IMDB Template Of Autofilter.</b>"""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of sᴘɪᴅᴇʏ 📝

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban_user  - <code>to ban a user.</code>
• /unban_user  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>📁 ᴛᴏᴛᴀʟ ғɪʟᴇs : <code>{}</code></b>
<b>👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs : <code>{}</code></b>
<b>👥 ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs : <code>{}</code></b>
<b>🗃️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ : <code>{}</code> 𝙼𝙱</b>
<b>📂 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ : <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
   🔮 sᴘɪᴅᴇʏ ʙᴏᴛ 🔮
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
   🔮 sᴘɪᴅᴇʏ ʙᴏᴛ 🔮
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """<b>📚 HELP : Rᴇᴘᴏʀᴛ ⚠️</b>

This Commands Helps You To <b>Report</b> A Message Or A User To The Admins Of The Recpective.\n<b>Don't Misuse This Command</b>

<b>🗣️ COMMANDS AND USAGE:</b>

➪/report 𝗈𝗋 @admins - To Report A User To Admins (Replay To A Message)."""

    CORONA_TXT = """<b>📚 HELP : 𝖢𝗈𝗏𝗂𝖽 🦠</b>

<i>This Commands Helps You To Know Daily Information About Covid</i>

<b>🗣️ COMMANDS AND USAGE:</b>

<i>➪ /covid - Use This Command With Your Country Name To Get Covid Information

➛ Example:</i>
<code>/covid 𝖨𝗇𝖽𝗂𝖺</code>"""

    URLSHORT_TXT = """<b>📚 HELP : URL Shortner</b>

<i>This Command Helps You To Short A URL</i>

<b>🗣️ COMMANDS AND USAGE:</b>

<b>➪ /short</b>: <i>Use This Command With Your Link To Get Shorted Links

➛ Example:</i>
<code>/short https://youtu.be/8xp8s6tj0Ts</code>"""

    VIDEO_TXT ="""<b>📚 HELP : YOUTUBE Video</b>

• 𝘜𝘴𝘢𝘨𝘦
𝘠𝘰𝘶 𝘊𝘢𝘯 𝘋𝘰𝘸𝘯𝘭𝘰𝘢𝘥 𝘈𝘯𝘺 𝘝𝘪𝘥𝘦𝘰 𝘍𝘳𝘰𝘮 𝘠𝘰𝘶𝘵𝘶𝘣𝘦

𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
• 𝘛𝘺𝘱𝘦 /video or /mp4 𝘈𝘯𝘥 (https://youtu.be/8xp8s6tj0Ts)
• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦:
🔖<code>/mp4 https://youtu.be/8xp8s6tj0Ts</code>
🔖<code>/video https://youtu.be/8xp8s6tj0Ts</code>"""

    ZOMBIES_TXT = """<b>📚 HELP : Kick Users</b>

<i>Kick incative members from group. Add me as admin with ban users permission in group.</i>

<b>🗣️ Commands and Usage:</b>
• /inkick - command with required arguments and i will kick members from group.
• /instatus - to check current status of chat member from group.
• /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
• /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
• /dkick - to kick deleted accounts."""

    IMAGE_TXT = """<b>📚 HELP : Edit Image</b>

This Command Helps 𝚢𝚘𝚞 To Edit Image Very Easily..🖼️

<b>🗣️ COMMANDS AND USAGE:</b>

🖼️ Just Send Me An Image To Edit ✨"""

    STICKER_TXT = """<b>📚 HELP : Sticker ID</b>

<i>You Can Use This Module To Find Any Stickers Id.</i>

• 𝐔𝐒𝐀𝐆𝐄
To Get Sticker ID
 
  ⚙️ 𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚
 
◉ Reply To Any Sticker With /stickerid Command"""

    YTTHUMB_TXT = """<b>📚 HELP : Youtube Thumbnail</b>

Helps You To Download Any Youtube Video Thumbnail 🖼️
    
⭕𝙃𝙤𝙬 𝙏𝙤 𝙐𝙨𝙚

𝘛𝘺𝘱𝘦 /ytthumb 𝘈𝘯𝘥 𝘝𝘪𝘥𝘦𝘰 𝘓𝘪𝘯𝘬

• 𝘌𝘹𝘢𝘮𝘱𝘭𝘦
<code>/ytthumb https://youtu.be/8xp8s6tj0Ts</code>"""

    ABOOK_TXT = """<b>📚 HELP : AudioBook</b>

<i>You Can Convert A PDF File To A Audio File With This Command...</i>

<b>🗣️ COMMANDS AND USAGE:</b>

➪ /audiobook: Replay This Command To Any PDF To Generate The Audio"""

    GTRANS_TXT = """<b>📚 HELP : Google Translator</b>

<i>This Command Helps You To Translate A Text To Any Languages You Want...</i>

➤ 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 𝐚𝐧𝐝 𝐔𝐬𝐚𝐠𝐞:

➪/tr - 𝖳𝗈 𝗍𝗋𝖺𝗇𝗌𝗅𝖺𝗍𝖾𝗋 𝗍𝖾𝗑𝗍𝗌 𝗍𝗈 𝖺 𝗌𝗉𝖾𝖼𝗂𝖿𝖼 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tr 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗅𝖺𝗇𝗀𝗎𝖺𝗀𝖾 𝖼𝗈𝖽𝖾

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝗋 𝗆𝗅
• 𝖾𝗇 = 𝖤𝗇𝗀𝗅𝗂𝗌𝗁
• 𝗆𝗅 = 𝖬𝖺𝗅𝖺𝗒𝖺𝗅𝖺𝗆
• 𝗁𝗂 = 𝖧𝗂𝗇𝖽𝗂"""

    RESTRIC_TXT = """➤ 𝐇𝐞𝐥𝐩: Mᴜᴛᴇ 🚫

𝚃𝚑𝚎𝚜𝚎 𝚊𝚛𝚎 𝚝𝚑𝚎 𝚌𝚘𝚖𝚖𝚊𝚗𝚍𝚜 𝚊 𝚐𝚛𝚘𝚞𝚙 𝚊𝚍𝚖𝚒𝚗 𝚌𝚊𝚗 𝚞𝚜𝚎 𝚝𝚘 𝚖𝚊𝚗𝚊𝚐𝚎 𝚝𝚑𝚎𝚒𝚛 𝚐𝚛𝚘𝚞𝚙 𝚖𝚘𝚛𝚎 𝚎𝚏𝚏𝚒𝚌𝚒𝚎𝚗𝚝𝚕𝚢.

➪/ban: 𝖳𝗈 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝖿𝗋𝗈𝗆 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unban: 𝖳𝗈 𝗎𝗇𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tban: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝖻𝖺𝗇 𝖺 𝗎𝗌𝖾𝗋.
➪/mute: 𝖳𝗈 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/unmute: 𝖳𝗈 𝗎𝗇𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋 𝗂𝗇 𝗍𝗁𝖾 𝗀𝗋𝗈𝗎𝗉.
➪/tmute: 𝖳𝗈 𝗍𝖾𝗆𝗉𝗈𝗋𝖺𝗋𝗂𝗅𝗒 𝗆𝗎𝗍𝖾 𝖺 𝗎𝗌𝖾𝗋.

➤ 𝖭𝗈𝗍𝖾:
𝖶𝗁𝗂𝗅𝖾 𝗎𝗌𝗂𝗇𝗀 /tmute 𝗈𝗋 /tban 𝗒𝗈𝗎 𝗌𝗁𝗈𝗎𝗅𝖽 𝗌𝗉𝖾𝖼𝗂𝖿𝗒 𝗍𝗁𝖾 𝗍𝗂𝗆𝖾 𝗅𝗂𝗆𝗂𝗍.

➛𝖤𝗑𝖺𝗆𝗉𝗅𝖾: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝖸𝗈𝗎 𝖼𝖺𝗇 𝗎𝗌𝖾 𝗏𝖺𝗅𝗎𝖾𝗌: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝗆𝗂𝗇𝗎𝗍𝖾𝗌
 • 𝗁 = 𝗁𝗈𝗎𝗋𝗌
 • 𝖽 = 𝖽𝖺𝗒𝗌"""
    CREATOR_REQUIRED = """❗<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "❗ **Arguments Required**"
      
    KICKED = """✔️ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """🚮 Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """❗<b>എന്നെ Admin ആക്കത്ത സ്ഥലത്ത് ഞാൻ നിക്കില്ല പോകുവാ Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """✔️ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>ഇപ്പൊ എല്ലാം അടിച്ചുമാറ്റി തരാം...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
