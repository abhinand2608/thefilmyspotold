class script(object):
    START_TXT = """ššššš {}šā¤ļøāš„ 
\nš ššš ššššššš šššššš & šššššš šš ššš šššš ššššššš šš ššššš šā¤ļøāš„   \nšššš ššš šš šš šššš ššššš & ššššš š„³š"""
    HELP_TXT = """š·š“š {}
š·š“šš“ šøš šš·š“ š·š“š»šæ šµš¾š š¼š š²š¾š¼š¼š°š½š³š."""
    ABOUT_TXT = """āæ  š¼š š½š°š¼š“: {}
\nāæ  š²šš“š°šš¾š: <a href=https://t.me/ABHINAND3510>AŅBŅHŅIŅNŅAŅNŅDŅ</a>
\nāæ  š»šøš±šš°šš & š»š°š½š¶: šæššš¾š¶šš°š¼ | šæššš·š¾š½ š¹
\nāæ  š³š°šš°š±š°šš“ & šš“ššš“š: š¼š¾š½š¶š¾š³š± | ššæš
\nāæ  š±ššøš»š³ ššš°ššš: v2.0.1 [ š±š“šš° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Source - https://t.me/thefilmyspot
<b>DEVS:</b>
- <a href=https://t.me/thefilmyspotin>šš¤</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>
- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message
<b>NOTE:</b>
1. should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.
<b>Commands and Usage:</b>
ā¢ /filter - <code>add a filter in chat</code>
ā¢ /filters - <code>list all the filters of a chat</code>
ā¢ /del - <code>delete a specific filter in chat</code>
ā¢ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>
-Supports both url and alert inline buttons.
<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/thefilmyspotbot)</code>
<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message Heheš)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>
<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my database ."""
    CONNECTION_TXT = """Help: <b>Connections</b>
- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.
<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM
<b>Commands and Usage:</b>
ā¢ /connect  - <code>connect a particular chat to your PM</code>
ā¢ /disconnect  - <code>disconnect from a chat</code>
ā¢ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>
<b>NOTE:</b>
these are the extra features of Botšš·ļø
<b>Commands and Usage:</b>
ā¢ /id - <code>get id of a specified user.</code>
ā¢ /info  - <code>get information about a user.</code>
ā¢ /imdb  - <code>get the film information from IMDb source.</code>
ā¢ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>
<b>NOTE:</b>
This module only works for my Adminsš¼
<b>Commands and Usage:</b>
ā¢ /logs - <code>to get the rescent errors</code>
ā¢ /stats - <code>to get status of files in db.</code>
ā¢ /delete - <code>to delete a specific file from db.</code>
ā¢ /users - <code>to get list of my users and ids.</code>
ā¢ /chats - <code>to get list of the my chats and ids </code>
ā¢ /leave  - <code>to leave from a chat.</code>
ā¢ /disable  -  <code>do disable a chat.</code>
ā¢ /ban  - <code>to ban a user.</code>
ā¢ /unban  - <code>to unban a user.</code>
ā¢ /channel - <code>to get list of total connected channels</code>
ā¢ /broadcast - <code>to broadcast a message to all users</code>
ā¢ /grp_broadcast - <code>to broadcast a msg to all connected groups</code>"""
    STATUS_TXT = """ā šš¾šš°š» šµšøš»š“š: <code>{}</code> š
ā šš¾šš°š» ššš“šš: <code>{}</code>
ā šš¾šš°š» š¶šš¾ššæš: <code>{}</code>
ā ššš“š³ ššš¾šš°š¶š“: <code>{}</code> 
ā šµšš“š“ ššš¾šš°š¶š“: <code>{}</code> """

    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser šš¤
ID - <code>{}</code>
Name - {}
"""
    ALRT_TXT = """Hey {} š,
į“ŹÉŖź± ÉŖź± É“į“į“ Źį“į“Ź į“į“į“ ÉŖį“ Źį“Qį“į“ź±į“,
Źį“Qį“į“ź±į“ Źį“į“Ź'ź±...
"""

    OLD_ALRT_TXT = """Źį“Ź {},
Źį“į“ į“Źį“ į“ź±ÉŖÉ“É¢ į“É“į“ į“ź° į“Ź į“Źį“ į“į“ź±ź±į“É¢į“ź±, 
į“Źį“į“ź±į“ ź±į“É“į“ į“Źį“ Źį“Qį“į“ź±į“ į“É¢į“ÉŖÉ“.
"""

    CUDNT_FND = """ÉŖ į“į“į“Źį“É“'į“ ź°ÉŖÉ“į“ į“É“Źį“ŹÉŖÉ“É¢ Źį“Źį“į“į“į“ į“į“ {}
į“ÉŖį“ Źį“į“ į“į“į“É“ į“É“Ź į“É“į“ į“ź° į“Źį“ź±į“?
"""


    I_CUDNT = """ÉŖ į“į“į“Źį“É“'į“ ź°ÉŖÉ“į“ į“É“Ź į“į“į“ ÉŖį“ Źį“Źį“į“į“į“ į“į“ {}
"""


    I_CUD_NT = """ÉŖ į“į“į“Źį“É“'į“ ź°ÉŖÉ“į“ į“É“Ź į“į“į“ ÉŖį“ Źį“Źį“į“į“į“ į“į“ {}.
į“Źį“į“ź±į“ į“Źį“į“į“ į“Źį“ ź±į“į“ŹŹÉŖÉ“É¢ į“É“ É¢į“į“É¢Źį“ į“Ź ÉŖį“į“Ź...
"""

    MVE_NT_FND = """į“į“į“ ÉŖį“ É“į“į“ ź°į“į“É“į“ ÉŖÉ“ į“į“į“į“Źį“ź±į“...
"""

    TOP_ALRT_MSG = """šš”ššš¤š¢š§š  ššØš« š¦šØšÆš¢š š¢š§ š­š”ššš¢š„š¦š²š¬š©šØš­ ššš­šššš¬š...
"""


    MELCOW_ENG = """HELLO {MENTION}šā¤ļø

WELCOME TO {GROUPNAME} š»š„ 

THANKS FOR JOINING &
 KEEP SUPPORTING US š¤šš».

Join our <a href='https://t.me/thefilmyspotin'>main channel</a> below to get access to the movies. Before requesting the movies, Must join our main channel. Only by joining will you get access to all the movies...

NB: You can only get the movie by typing in the correct spelling...

If you do not get the Movie / Series, mention the admin in the following format š

š¤· Example: @admin Avatar 2009 English 
            @admin Breaking Bad S05E07
Wį“ Dį“ Nį“į“ Oį“”É“ AÉ“Ź Cį“É“į“į“É“į“ Pį“sį“į“į“ Hį“Źį“. Wį“ OÉ“ŹŹ SŹį“Źį“ TŹį“sį“ FÉŖŹį“s WŹÉŖį“Ź AŹį“ AŹŹį“į“į“Ź SŹį“Źį“į“ BŹ Sį“į“į“Źį“į“Ź EŹsį“ OÉ“ TŹį“ IÉ“į“į“ŹÉ“į“į“

ā ļø Iź° Yį“į“ Oį“”É“ TŹį“ Cį“į“ŹŹÉŖÉ¢Źį“s Oź° AÉ“Ź Sį“į“ź°ź°, IÉ“į“ÉŖį“į“į“į“ Us WÉŖį“Ź PŹį“į“ź° Wį“ WÉŖŹŹ Rį“į“į“į“ į“

Do not contact Admin directly...

If you want to contact Admin, Please send the message to @thefilmyspothelpbot and the bot will deliver the message to the group Admin...

<a href='https://t.me/thefilmyspothelpbot'>If you are facing any problems with our movie files, bots or groups, report it in our Feedback Bot : @thefilmyspothelp</a>

For admin support type @admins with your message and the bot will forward the message to the admin...</b>"""

    OWNER_INFO = """
<b>āāāā[ į“į“”É“į“Ź į“į“į“į“ÉŖŹź± ]āāāā
    
ā¢ ź°į“ŹŹ É“į“į“į“ : AŅBŅHŅIŅNŅAŅNŅDŅ
ā¢ į“ź±į“ŹÉ“į“į“į“ : @Abhinand3510
ā¢ į“į“Źį“į“É“į“É“į“ į“į“ ŹÉŖÉ“į“ : <a href='t.me/abhinand3510'>į“ŹÉŖį“į“ Źį“Źį“</a></b>"""

    RESTART_TXT = """

<b>Bį“į“ Rį“sį“į“Źį“į“į“ !

š Dį“į“į“ : <code>{}</code>

ā°TÉŖį“į“ : <code>{}</code>

š TÉŖį“į“į“¢į“É“į“ : <code>Asia/Kolkata</code></b>"""

    NORSLTS = """
ā #š”š¼š„š²ššš¹šš ā

šš <b>: {}</b>

š”š®šŗš² <b>: {}</b>

š š²ššš®š“š² <b>: {}</b>"""

    CAPTION = """
<b>š</b> <code>{file_name}</code>

<b>
ā­āāāāāāā ā¢ ā ā¢ āāāāāāāā®

ā  <a href="https://t.me/+8lZE1YYLDqdjZTc1">Join š­š”ššš¢š„š¦š²š¬š©šØš­ š 
For All Movies & Series Files ā </a>

ā°āāāāāāā ā¢ ā ā¢ āāāāāāāāÆ

========= ā¢ ā  ā¢ =========

š Note : We Only Share contents that are Already on Telegram . 
So If You Have Any Issues With These Files, 
Then We aren't Responsible for That ā

========= ā¢ ā  ā¢ =========</b>"""

    IMDB_TEMPLATE_TXT = """
āæ <b>š· Title</b>: <a href={url}>{title}</a>

āæ š Year: <a href={url}/release_date>{year}</a>  | ā³ {runtime} Min

āæ š­ Genres: {genres}

āæ š Rating: <a href={url}/ratings>{rating} / 10</a> 

āæ šļø Languages : <code>{languages}</code>

āæ ā¶ļø : <a href={url}/box_office>{kind}</a> | Seasons š: {seasons}

āæ š„ Cast : <code>{cast}</code>

āæ š Storyline : {plot}

 ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ ā¹ 

Requested by : {message.from_user.mention} š"""
    
    ALL_FILTERS = """
<b>Hį“Ź {}, TŹį“sį“ į“Źį“ į“Ź į“ŹŹį“į“ į“Źį“į“s į“Ņ ŅÉŖŹį“į“Źs.</b>"""
    
    GFILTER_TXT = """
<b>Wį“Źį“į“į“į“ į“į“ GŹį“Źį“Ź FÉŖŹį“į“Źs. GŹį“Źį“Ź FÉŖŹį“į“Źs į“Źį“ į“Źį“ ŅÉŖŹį“į“Źs sį“į“ ŹŹ Źį“į“ į“į“į“ÉŖÉ“s į“”ŹÉŖį“Ź į“”ÉŖŹŹ į“”į“Źį“ į“É“ į“ŹŹ É¢Źį“į“į“s.</b>
    
Aį“ į“ÉŖŹį“ŹŹį“ į“į“į“į“į“É“į“s:
ā¢ /gfilter - <code>Tį“ į“Źį“į“į“į“ į“ É¢Źį“Źį“Ź ŅÉŖŹį“į“Ź.</code>
ā¢ /gfilters - <code>Tį“ į“ ÉŖį“į“” į“ŹŹ É¢Źį“Źį“Ź ŅÉŖŹį“į“Źs.</code>
ā¢ /delg - <code>Tį“ į“į“Źį“į“į“ į“ į“į“Źį“ÉŖį“į“Źį“Ź É¢Źį“Źį“Ź ŅÉŖŹį“į“Ź.</code>
ā¢ /delallg - <code>į“į“ į“į“Źį“į“į“ į“ŹŹ É¢Źį“Źį“Ź ź°ÉŖŹį“į“Źź±.</code>"""
    
    FILE_STORE_TXT = """
<b>FÉŖŹį“ sį“į“Źį“ ÉŖs į“Źį“ Ņį“į“į“į“Źį“ į“”ŹÉŖį“Ź į“”ÉŖŹŹ į“Źį“į“į“į“ į“ sŹį“Źį“į“ŹŹį“ ŹÉŖÉ“į“ į“Ņ į“ sÉŖÉ“É¢Źį“ į“Ź į“į“Źį“ÉŖį“Źį“ ŅÉŖŹį“s.</b>

Aį“ į“ÉŖŹį“ŹŹį“ į“į“į“į“į“É“į“s:
ā¢ /batch - <code>Tį“ į“Źį“į“į“į“ į“ Źį“į“į“Ź ŹÉŖÉ“į“ į“Ņ į“į“Źį“ÉŖį“Źį“ ŅÉŖŹį“s.</code>
ā¢ /link - <code>Tį“ į“Źį“į“į“į“ į“ sÉŖÉ“É¢Źį“ ŅÉŖŹį“ sį“į“Źį“ ŹÉŖÉ“į“.</code>
ā¢ /pbatch - <code>Jį“sį“ ŹÉŖį“į“ /batch, Źį“į“ į“Źį“ ŅÉŖŹį“s į“”ÉŖŹŹ Źį“ sį“É“į“ į“”ÉŖį“Ź Ņį“Źį“”į“Źį“ Źį“sį“ŹÉŖį“į“ÉŖį“É“s.</code>
ā¢ /plink - <code>Jį“sį“ ŹÉŖį“į“ /link, Źį“į“ į“Źį“ ŅÉŖŹį“ į“”ÉŖŹŹ Źį“ sį“É“į“ į“”ÉŖį“Ź Ņį“Źį“”į“Źį“ Źį“sį“ŹÉŖį“į“ÉŖį“É“.</code>"""

    RESTART_TXT = """
<b>Bį“į“ Rį“sį“į“Źį“į“į“ !

š Dį“į“į“ : <code>{}</code>
ā° TÉŖį“į“ : <code>{}</code>
š TÉŖį“į“į“¢į“É“į“ : <code>Asia/Kolkata</code>
š ļø Bį“ÉŖŹį“ Sį“į“į“į“s: <code>v2.7.1 [ Sį“į“ŹŹį“ ]</code></b>"""

