def reverseLUT(lut):
    rev = {}
    for key in lut:
        rev[lut[key]] = key
    return rev


KEY_NONE = "OBS_KEY_NONE"
KEY_RETURN = "OBS_KEY_RETURN"
KEY_ENTER = "OBS_KEY_ENTER"
KEY_ESCAPE = "OBS_KEY_ESCAPE"
KEY_TAB = "OBS_KEY_TAB"
KEY_BACKTAB = "OBS_KEY_BACKTAB"
KEY_BACKSPACE = "OBS_KEY_BACKSPACE"
KEY_INSERT = "OBS_KEY_INSERT"
KEY_DELETE = "OBS_KEY_DELETE"
KEY_PAUSE = "OBS_KEY_PAUSE"
KEY_PRINT = "OBS_KEY_PRINT"
KEY_SYSREQ = "OBS_KEY_SYSREQ"
KEY_CLEAR = "OBS_KEY_CLEAR"
KEY_HOME = "OBS_KEY_HOME"
KEY_END = "OBS_KEY_END"
KEY_LEFT = "OBS_KEY_LEFT"
KEY_UP = "OBS_KEY_UP"
KEY_RIGHT = "OBS_KEY_RIGHT"
KEY_DOWN = "OBS_KEY_DOWN"
KEY_PAGEUP = "OBS_KEY_PAGEUP"
KEY_PAGEDOWN = "OBS_KEY_PAGEDOWN"

KEY_SHIFT = "OBS_KEY_SHIFT"
KEY_CONTROL = "OBS_KEY_CONTROL"
KEY_META = "OBS_KEY_META"
KEY_ALT = "OBS_KEY_ALT"
KEY_ALTGR = "OBS_KEY_ALTGR"
KEY_CAPSLOCK = "OBS_KEY_CAPSLOCK"
KEY_NUMLOCK = "OBS_KEY_NUMLOCK"
KEY_SCROLLLOCK = "OBS_KEY_SCROLLLOCK"

KEY_F1 = "OBS_KEY_F1"
KEY_F2 = "OBS_KEY_F2"
KEY_F3 = "OBS_KEY_F3"
KEY_F4 = "OBS_KEY_F4"
KEY_F5 = "OBS_KEY_F5"
KEY_F6 = "OBS_KEY_F6"
KEY_F7 = "OBS_KEY_F7"
KEY_F8 = "OBS_KEY_F8"
KEY_F9 = "OBS_KEY_F9"
KEY_F10 = "OBS_KEY_F10"
KEY_F11 = "OBS_KEY_F11"
KEY_F12 = "OBS_KEY_F12"
KEY_F13 = "OBS_KEY_F13"
KEY_F14 = "OBS_KEY_F14"
KEY_F15 = "OBS_KEY_F15"
KEY_F16 = "OBS_KEY_F16"
KEY_F17 = "OBS_KEY_F17"
KEY_F18 = "OBS_KEY_F18"
KEY_F19 = "OBS_KEY_F19"
KEY_F20 = "OBS_KEY_F20"
KEY_F21 = "OBS_KEY_F21"
KEY_F22 = "OBS_KEY_F22"
KEY_F23 = "OBS_KEY_F23"
KEY_F24 = "OBS_KEY_F24"
KEY_F25 = "OBS_KEY_F25"
KEY_F26 = "OBS_KEY_F26"
KEY_F27 = "OBS_KEY_F27"
KEY_F28 = "OBS_KEY_F28"
KEY_F29 = "OBS_KEY_F29"
KEY_F30 = "OBS_KEY_F30"
KEY_F31 = "OBS_KEY_F31"
KEY_F32 = "OBS_KEY_F32"
KEY_F33 = "OBS_KEY_F33"
KEY_F34 = "OBS_KEY_F34"
KEY_F35 = "OBS_KEY_F35"

KEY_MENU = "OBS_KEY_MENU"
KEY_HYPER_L = "OBS_KEY_HYPER_L"
KEY_HYPER_R = "OBS_KEY_HYPER_R"
KEY_HELP = "OBS_KEY_HELP"
KEY_DIRECTION_L = "OBS_KEY_DIRECTION_L"
KEY_DIRECTION_R = "OBS_KEY_DIRECTION_R"

KEY_SPACE = "OBS_KEY_SPACE"
KEY_EXCLAM = "OBS_KEY_EXCLAM"
KEY_QUOTEDBL = "OBS_KEY_QUOTEDBL"
KEY_NUMBERSIGN = "OBS_KEY_NUMBERSIGN"
KEY_DOLLAR = "OBS_KEY_DOLLAR"
KEY_PERCENT = "OBS_KEY_PERCENT"
KEY_AMPERSAND = "OBS_KEY_AMPERSAND"
KEY_APOSTROPHE = "OBS_KEY_APOSTROPHE"
KEY_PARENLEFT = "OBS_KEY_PARENLEFT"
KEY_PARENRIGHT = "OBS_KEY_PARENRIGHT"
KEY_ASTERISK = "OBS_KEY_ASTERISK"
KEY_PLUS = "OBS_KEY_PLUS"
KEY_COMMA = "OBS_KEY_COMMA"
KEY_MINUS = "OBS_KEY_MINUS"
KEY_PERIOD = "OBS_KEY_PERIOD"
KEY_SLASH = "OBS_KEY_SLASH"
KEY_0 = "OBS_KEY_0"
KEY_1 = "OBS_KEY_1"
KEY_2 = "OBS_KEY_2"
KEY_3 = "OBS_KEY_3"
KEY_4 = "OBS_KEY_4"
KEY_5 = "OBS_KEY_5"
KEY_6 = "OBS_KEY_6"
KEY_7 = "OBS_KEY_7"
KEY_8 = "OBS_KEY_8"
KEY_9 = "OBS_KEY_9"
KEY_NUMEQUAL = "OBS_KEY_NUMEQUAL"
KEY_NUMASTERISK = "OBS_KEY_NUMASTERISK"
KEY_NUMPLUS = "OBS_KEY_NUMPLUS"
KEY_NUMCOMMA = "OBS_KEY_NUMCOMMA"
KEY_NUMMINUS = "OBS_KEY_NUMMINUS"
KEY_NUMPERIOD = "OBS_KEY_NUMPERIOD"
KEY_NUMSLASH = "OBS_KEY_NUMSLASH"
KEY_NUM0 = "OBS_KEY_NUM0"
KEY_NUM1 = "OBS_KEY_NUM1"
KEY_NUM2 = "OBS_KEY_NUM2"
KEY_NUM3 = "OBS_KEY_NUM3"
KEY_NUM4 = "OBS_KEY_NUM4"
KEY_NUM5 = "OBS_KEY_NUM5"
KEY_NUM6 = "OBS_KEY_NUM6"
KEY_NUM7 = "OBS_KEY_NUM7"
KEY_NUM8 = "OBS_KEY_NUM8"
KEY_NUM9 = "OBS_KEY_NUM9"
KEY_COLON = "OBS_KEY_COLON"
KEY_SEMICOLON = "OBS_KEY_SEMICOLON"
KEY_QUOTE = "OBS_KEY_QUOTE"
KEY_LESS = "OBS_KEY_LESS"
KEY_EQUAL = "OBS_KEY_EQUAL"
KEY_GREATER = "OBS_KEY_GREATER"
KEY_QUESTION = "OBS_KEY_QUESTION"
KEY_AT = "OBS_KEY_AT"
KEY_A = "OBS_KEY_A"
KEY_B = "OBS_KEY_B"
KEY_C = "OBS_KEY_C"
KEY_D = "OBS_KEY_D"
KEY_E = "OBS_KEY_E"
KEY_F = "OBS_KEY_F"
KEY_G = "OBS_KEY_G"
KEY_H = "OBS_KEY_H"
KEY_I = "OBS_KEY_I"
KEY_J = "OBS_KEY_J"
KEY_K = "OBS_KEY_K"
KEY_L = "OBS_KEY_L"
KEY_M = "OBS_KEY_M"
KEY_N = "OBS_KEY_N"
KEY_O = "OBS_KEY_O"
KEY_P = "OBS_KEY_P"
KEY_Q = "OBS_KEY_Q"
KEY_R = "OBS_KEY_R"
KEY_S = "OBS_KEY_S"
KEY_T = "OBS_KEY_T"
KEY_U = "OBS_KEY_U"
KEY_V = "OBS_KEY_V"
KEY_W = "OBS_KEY_W"
KEY_X = "OBS_KEY_X"
KEY_Y = "OBS_KEY_Y"
KEY_Z = "OBS_KEY_Z"
KEY_BRACKETLEFT = "OBS_KEY_BRACKETLEFT"
KEY_BACKSLASH = "OBS_KEY_BACKSLASH"
KEY_BRACKETRIGHT = "OBS_KEY_BRACKETRIGHT"
KEY_ASCIICIRCUM = "OBS_KEY_ASCIICIRCUM"
KEY_UNDERSCORE = "OBS_KEY_UNDERSCORE"
KEY_QUOTELEFT = "OBS_KEY_QUOTELEFT"
KEY_BRACELEFT = "OBS_KEY_BRACELEFT"
KEY_BAR = "OBS_KEY_BAR"
KEY_BRACERIGHT = "OBS_KEY_BRACERIGHT"
KEY_ASCIITILDE = "OBS_KEY_ASCIITILDE"
KEY_NOBREAKSPACE = "OBS_KEY_NOBREAKSPACE"
KEY_EXCLAMDOWN = "OBS_KEY_EXCLAMDOWN"
KEY_CENT = "OBS_KEY_CENT"
KEY_STERLING = "OBS_KEY_STERLING"
KEY_CURRENCY = "OBS_KEY_CURRENCY"
KEY_YEN = "OBS_KEY_YEN"
KEY_BROKENBAR = "OBS_KEY_BROKENBAR"
KEY_SECTION = "OBS_KEY_SECTION"
KEY_DIAERESIS = "OBS_KEY_DIAERESIS"
KEY_COPYRIGHT = "OBS_KEY_COPYRIGHT"
KEY_ORDFEMININE = "OBS_KEY_ORDFEMININE"
KEY_GUILLEMOTLEFT = "OBS_KEY_GUILLEMOTLEFT"
KEY_NOTSIGN = "OBS_KEY_NOTSIGN"
KEY_HYPHEN = "OBS_KEY_HYPHEN"
KEY_REGISTERED = "OBS_KEY_REGISTERED"
KEY_MACRON = "OBS_KEY_MACRON"
KEY_DEGREE = "OBS_KEY_DEGREE"
KEY_PLUSMINUS = "OBS_KEY_PLUSMINUS"
KEY_TWOSUPERIOR = "OBS_KEY_TWOSUPERIOR"
KEY_THREESUPERIOR = "OBS_KEY_THREESUPERIOR"
KEY_ACUTE = "OBS_KEY_ACUTE"
KEY_MU = "OBS_KEY_MU"
KEY_PARAGRAPH = "OBS_KEY_PARAGRAPH"
KEY_PERIODCENTERED = "OBS_KEY_PERIODCENTERED"
KEY_CEDILLA = "OBS_KEY_CEDILLA"
KEY_ONESUPERIOR = "OBS_KEY_ONESUPERIOR"
KEY_MASCULINE = "OBS_KEY_MASCULINE"
KEY_GUILLEMOTRIGHT = "OBS_KEY_GUILLEMOTRIGHT"
KEY_ONEQUARTER = "OBS_KEY_ONEQUARTER"
KEY_ONEHALF = "OBS_KEY_ONEHALF"
KEY_THREEQUARTERS = "OBS_KEY_THREEQUARTERS"
KEY_QUESTIONDOWN = "OBS_KEY_QUESTIONDOWN"
KEY_AGRAVE = "OBS_KEY_AGRAVE"
KEY_AACUTE = "OBS_KEY_AACUTE"
KEY_ACIRCUMFLEX = "OBS_KEY_ACIRCUMFLEX"
KEY_ATILDE = "OBS_KEY_ATILDE"
KEY_ADIAERESIS = "OBS_KEY_ADIAERESIS"
KEY_ARING = "OBS_KEY_ARING"
KEY_AE = "OBS_KEY_AE"
KEY_CCEDILLA = "OBS_KEY_CCEDILLA"
KEY_EGRAVE = "OBS_KEY_EGRAVE"
KEY_EACUTE = "OBS_KEY_EACUTE"
KEY_ECIRCUMFLEX = "OBS_KEY_ECIRCUMFLEX"
KEY_EDIAERESIS = "OBS_KEY_EDIAERESIS"
KEY_IGRAVE = "OBS_KEY_IGRAVE"
KEY_IACUTE = "OBS_KEY_IACUTE"
KEY_ICIRCUMFLEX = "OBS_KEY_ICIRCUMFLEX"
KEY_IDIAERESIS = "OBS_KEY_IDIAERESIS"
KEY_ETH = "OBS_KEY_ETH"
KEY_NTILDE = "OBS_KEY_NTILDE"
KEY_OGRAVE = "OBS_KEY_OGRAVE"
KEY_OACUTE = "OBS_KEY_OACUTE"
KEY_OCIRCUMFLEX = "OBS_KEY_OCIRCUMFLEX"
KEY_OTILDE = "OBS_KEY_OTILDE"
KEY_ODIAERESIS = "OBS_KEY_ODIAERESIS"
KEY_MULTIPLY = "OBS_KEY_MULTIPLY"
KEY_OOBLIQUE = "OBS_KEY_OOBLIQUE"
KEY_UGRAVE = "OBS_KEY_UGRAVE"
KEY_UACUTE = "OBS_KEY_UACUTE"
KEY_UCIRCUMFLEX = "OBS_KEY_UCIRCUMFLEX"
KEY_UDIAERESIS = "OBS_KEY_UDIAERESIS"
KEY_YACUTE = "OBS_KEY_YACUTE"
KEY_THORN = "OBS_KEY_THORN"
KEY_SSHARP = "OBS_KEY_SSHARP"
KEY_DIVISION = "OBS_KEY_DIVISION"
KEY_YDIAERESIS = "OBS_KEY_YDIAERESIS"
KEY_MULTI_KEY = "OBS_KEY_MULTI_KEY"
KEY_CODEINPUT = "OBS_KEY_CODEINPUT"
KEY_SINGLECANDIDATE = "OBS_KEY_SINGLECANDIDATE"
KEY_MULTIPLECANDIDATE = "OBS_KEY_MULTIPLECANDIDATE"
KEY_PREVIOUSCANDIDATE = "OBS_KEY_PREVIOUSCANDIDATE"
KEY_MODE_SWITCH = "OBS_KEY_MODE_SWITCH"
KEY_KANJI = "OBS_KEY_KANJI"
KEY_MUHENKAN = "OBS_KEY_MUHENKAN"
KEY_HENKAN = "OBS_KEY_HENKAN"
KEY_ROMAJI = "OBS_KEY_ROMAJI"
KEY_HIRAGANA = "OBS_KEY_HIRAGANA"
KEY_KATAKANA = "OBS_KEY_KATAKANA"
KEY_HIRAGANA_KATAKANA = "OBS_KEY_HIRAGANA_KATAKANA"
KEY_ZENKAKU = "OBS_KEY_ZENKAKU"
KEY_HANKAKU = "OBS_KEY_HANKAKU"
KEY_ZENKAKU_HANKAKU = "OBS_KEY_ZENKAKU_HANKAKU"
KEY_TOUROKU = "OBS_KEY_TOUROKU"
KEY_MASSYO = "OBS_KEY_MASSYO"
KEY_KANA_LOCK = "OBS_KEY_KANA_LOCK"
KEY_KANA_SHIFT = "OBS_KEY_KANA_SHIFT"
KEY_EISU_SHIFT = "OBS_KEY_EISU_SHIFT"
KEY_EISU_TOGGLE = "OBS_KEY_EISU_TOGGLE"
KEY_HANGUL = "OBS_KEY_HANGUL"
KEY_HANGUL_START = "OBS_KEY_HANGUL_START"
KEY_HANGUL_END = "OBS_KEY_HANGUL_END"
KEY_HANGUL_HANJA = "OBS_KEY_HANGUL_HANJA"
KEY_HANGUL_JAMO = "OBS_KEY_HANGUL_JAMO"
KEY_HANGUL_ROMAJA = "OBS_KEY_HANGUL_ROMAJA"
KEY_HANGUL_JEONJA = "OBS_KEY_HANGUL_JEONJA"
KEY_HANGUL_BANJA = "OBS_KEY_HANGUL_BANJA"
KEY_HANGUL_PREHANJA = "OBS_KEY_HANGUL_PREHANJA"
KEY_HANGUL_POSTHANJA = "OBS_KEY_HANGUL_POSTHANJA"
KEY_HANGUL_SPECIAL = "OBS_KEY_HANGUL_SPECIAL"
KEY_DEAD_GRAVE = "OBS_KEY_DEAD_GRAVE"
KEY_DEAD_ACUTE = "OBS_KEY_DEAD_ACUTE"
KEY_DEAD_CIRCUMFLEX = "OBS_KEY_DEAD_CIRCUMFLEX"
KEY_DEAD_TILDE = "OBS_KEY_DEAD_TILDE"
KEY_DEAD_MACRON = "OBS_KEY_DEAD_MACRON"
KEY_DEAD_BREVE = "OBS_KEY_DEAD_BREVE"
KEY_DEAD_ABOVEDOT = "OBS_KEY_DEAD_ABOVEDOT"
KEY_DEAD_DIAERESIS = "OBS_KEY_DEAD_DIAERESIS"
KEY_DEAD_ABOVERING = "OBS_KEY_DEAD_ABOVERING"
KEY_DEAD_DOUBLEACUTE = "OBS_KEY_DEAD_DOUBLEACUTE"
KEY_DEAD_CARON = "OBS_KEY_DEAD_CARON"
KEY_DEAD_CEDILLA = "OBS_KEY_DEAD_CEDILLA"
KEY_DEAD_OGONEK = "OBS_KEY_DEAD_OGONEK"
KEY_DEAD_IOTA = "OBS_KEY_DEAD_IOTA"
KEY_DEAD_VOICED_SOUND = "OBS_KEY_DEAD_VOICED_SOUND"
KEY_DEAD_SEMIVOICED_SOUND = "OBS_KEY_DEAD_SEMIVOICED_SOUND"
KEY_DEAD_BELOWDOT = "OBS_KEY_DEAD_BELOWDOT"
KEY_DEAD_HOOK = "OBS_KEY_DEAD_HOOK"
KEY_DEAD_HORN = "OBS_KEY_DEAD_HORN"
KEY_BACK = "OBS_KEY_BACK"
KEY_FORWARD = "OBS_KEY_FORWARD"
KEY_STOP = "OBS_KEY_STOP"
KEY_REFRESH = "OBS_KEY_REFRESH"
KEY_VOLUMEDOWN = "OBS_KEY_VOLUMEDOWN"
KEY_VOLUMEMUTE = "OBS_KEY_VOLUMEMUTE"
KEY_VOLUMEUP = "OBS_KEY_VOLUMEUP"
KEY_BASSBOOST = "OBS_KEY_BASSBOOST"
KEY_BASSUP = "OBS_KEY_BASSUP"
KEY_BASSDOWN = "OBS_KEY_BASSDOWN"
KEY_TREBLEUP = "OBS_KEY_TREBLEUP"
KEY_TREBLEDOWN = "OBS_KEY_TREBLEDOWN"
KEY_MEDIAPLAY = "OBS_KEY_MEDIAPLAY"
KEY_MEDIASTOP = "OBS_KEY_MEDIASTOP"
KEY_MEDIAPREVIOUS = "OBS_KEY_MEDIAPREVIOUS"
KEY_MEDIANEXT = "OBS_KEY_MEDIANEXT"
KEY_MEDIARECORD = "OBS_KEY_MEDIARECORD"
KEY_MEDIAPAUSE = "OBS_KEY_MEDIAPAUSE"
KEY_MEDIATOGGLEPLAYPAUSE = "OBS_KEY_MEDIATOGGLEPLAYPAUSE"
KEY_HOMEPAGE = "OBS_KEY_HOMEPAGE"
KEY_FAVORITES = "OBS_KEY_FAVORITES"
KEY_SEARCH = "OBS_KEY_SEARCH"
KEY_STANDBY = "OBS_KEY_STANDBY"
KEY_OPENURL = "OBS_KEY_OPENURL"
KEY_LAUNCHMAIL = "OBS_KEY_LAUNCHMAIL"
KEY_LAUNCHMEDIA = "OBS_KEY_LAUNCHMEDIA"
KEY_LAUNCH0 = "OBS_KEY_LAUNCH0"
KEY_LAUNCH1 = "OBS_KEY_LAUNCH1"
KEY_LAUNCH2 = "OBS_KEY_LAUNCH2"
KEY_LAUNCH3 = "OBS_KEY_LAUNCH3"
KEY_LAUNCH4 = "OBS_KEY_LAUNCH4"
KEY_LAUNCH5 = "OBS_KEY_LAUNCH5"
KEY_LAUNCH6 = "OBS_KEY_LAUNCH6"
KEY_LAUNCH7 = "OBS_KEY_LAUNCH7"
KEY_LAUNCH8 = "OBS_KEY_LAUNCH8"
KEY_LAUNCH9 = "OBS_KEY_LAUNCH9"
KEY_LAUNCHA = "OBS_KEY_LAUNCHA"
KEY_LAUNCHB = "OBS_KEY_LAUNCHB"
KEY_LAUNCHC = "OBS_KEY_LAUNCHC"
KEY_LAUNCHD = "OBS_KEY_LAUNCHD"
KEY_LAUNCHE = "OBS_KEY_LAUNCHE"
KEY_LAUNCHF = "OBS_KEY_LAUNCHF"
KEY_LAUNCHG = "OBS_KEY_LAUNCHG"
KEY_LAUNCHH = "OBS_KEY_LAUNCHH"
KEY_MONBRIGHTNESSUP = "OBS_KEY_MONBRIGHTNESSUP"
KEY_MONBRIGHTNESSDOWN = "OBS_KEY_MONBRIGHTNESSDOWN"
KEY_KEYBOARDLIGHTONOFF = "OBS_KEY_KEYBOARDLIGHTONOFF"
KEY_KEYBOARDBRIGHTNESSUP = "OBS_KEY_KEYBOARDBRIGHTNESSUP"
KEY_KEYBOARDBRIGHTNESSDOWN = "OBS_KEY_KEYBOARDBRIGHTNESSDOWN"
KEY_POWEROFF = "OBS_KEY_POWEROFF"
KEY_WAKEUP = "OBS_KEY_WAKEUP"
KEY_EJECT = "OBS_KEY_EJECT"
KEY_SCREENSAVER = "OBS_KEY_SCREENSAVER"
KEY_WWW = "OBS_KEY_WWW"
KEY_MEMO = "OBS_KEY_MEMO"
KEY_LIGHTBULB = "OBS_KEY_LIGHTBULB"
KEY_SHOP = "OBS_KEY_SHOP"
KEY_HISTORY = "OBS_KEY_HISTORY"
KEY_ADDFAVORITE = "OBS_KEY_ADDFAVORITE"
KEY_HOTLINKS = "OBS_KEY_HOTLINKS"
KEY_BRIGHTNESSADJUST = "OBS_KEY_BRIGHTNESSADJUST"
KEY_FINANCE = "OBS_KEY_FINANCE"
KEY_COMMUNITY = "OBS_KEY_COMMUNITY"
KEY_AUDIOREWIND = "OBS_KEY_AUDIOREWIND"
KEY_BACKFORWARD = "OBS_KEY_BACKFORWARD"
KEY_APPLICATIONLEFT = "OBS_KEY_APPLICATIONLEFT"
KEY_APPLICATIONRIGHT = "OBS_KEY_APPLICATIONRIGHT"
KEY_BOOK = "OBS_KEY_BOOK"
KEY_CD = "OBS_KEY_CD"
KEY_CALCULATOR = "OBS_KEY_CALCULATOR"
KEY_TODOLIST = "OBS_KEY_TODOLIST"
KEY_CLEARGRAB = "OBS_KEY_CLEARGRAB"
KEY_CLOSE = "OBS_KEY_CLOSE"
KEY_COPY = "OBS_KEY_COPY"
KEY_CUT = "OBS_KEY_CUT"
KEY_DISPLAY = "OBS_KEY_DISPLAY"
KEY_DOS = "OBS_KEY_DOS"
KEY_DOCUMENTS = "OBS_KEY_DOCUMENTS"
KEY_EXCEL = "OBS_KEY_EXCEL"
KEY_EXPLORER = "OBS_KEY_EXPLORER"
KEY_GAME = "OBS_KEY_GAME"
KEY_GO = "OBS_KEY_GO"
KEY_ITOUCH = "OBS_KEY_ITOUCH"
KEY_LOGOFF = "OBS_KEY_LOGOFF"
KEY_MARKET = "OBS_KEY_MARKET"
KEY_MEETING = "OBS_KEY_MEETING"
KEY_MENUKB = "OBS_KEY_MENUKB"
KEY_MENUPB = "OBS_KEY_MENUPB"
KEY_MYSITES = "OBS_KEY_MYSITES"
KEY_NEWS = "OBS_KEY_NEWS"
KEY_OFFICEHOME = "OBS_KEY_OFFICEHOME"
KEY_OPTION = "OBS_KEY_OPTION"
KEY_PASTE = "OBS_KEY_PASTE"
KEY_PHONE = "OBS_KEY_PHONE"
KEY_CALENDAR = "OBS_KEY_CALENDAR"
KEY_REPLY= "OBS_KEY_REPLY"
KEY_RELOAD = "OBS_KEY_RELOAD"
KEY_ROTATEWINDOWS = "OBS_KEY_ROTATEWINDOWS"
KEY_ROTATIONPB = "OBS_KEY_ROTATIONPB"
KEY_ROTATIONKB= "OBS_KEY_ROTATIONKB"
KEY_SAVE = "OBS_KEY_SAVE"
KEY_SEND = "OBS_KEY_SEND"
KEY_SPELL = "OBS_KEY_SPELL"
KEY_SPLITSCREEN = "OBS_KEY_SPLITSCREEN"
KEY_SUPPORT = "OBS_KEY_SUPPORT"
KEY_TASKPANE = "OBS_KEY_TASKPANE"
KEY_TERMINAL = "OBS_KEY_TERMINAL"
KEY_TOOLS = "OBS_KEY_TOOLS"
KEY_TRAVEL = "OBS_KEY_TRAVEL"
KEY_VIDEO = "OBS_KEY_VIDEO"
KEY_WORD = "OBS_KEY_WORD"
KEY_XFER = "OBS_KEY_XFER"
KEY_ZOOMIN = "OBS_KEY_ZOOMIN"
KEY_ZOOMOUT = "OBS_KEY_ZOOMOUT"
KEY_AWAY = "OBS_KEY_AWAY"
KEY_MESSENGER = "OBS_KEY_MESSENGER"
KEY_WEBCAM = "OBS_KEY_WEBCAM"
KEY_MAILFORWARD = "OBS_KEY_MAILFORWARD"
KEY_PICTURES = "OBS_KEY_PICTURES"
KEY_MUSIC = "OBS_KEY_MUSIC"
KEY_BATTERY = "OBS_KEY_BATTERY"
KEY_BLUETOOTH = "OBS_KEY_BLUETOOTH"
KEY_WLAN = "OBS_KEY_WLAN"
KEY_UWB = "OBS_KEY_UWB"
KEY_AUDIOFORWARD = "OBS_KEY_AUDIOFORWARD"
KEY_AUDIOREPEAT = "OBS_KEY_AUDIOREPEAT"
KEY_AUDIORANDOMPLAY = "OBS_KEY_AUDIORANDOMPLAY"
KEY_SUBTITLE = "OBS_KEY_SUBTITLE"
KEY_AUDIOCYCLETRACK = "OBS_KEY_AUDIOCYCLETRACK"
KEY_TIME = "OBS_KEY_TIME"
KEY_HIBERNATE = "OBS_KEY_HIBERNATE"
KEY_VIEW = "OBS_KEY_VIEW"
KEY_TOPMENU = "OBS_KEY_TOPMENU"
KEY_POWERDOWN = "OBS_KEY_POWERDOWN"
KEY_SUSPEND = "OBS_KEY_SUSPEND"
KEY_CONTRASTADJUST = "OBS_KEY_CONTRASTADJUST"
KEY_MEDIALAST = "OBS_KEY_MEDIALAST"
KEY_CALL = "OBS_KEY_CALL"
KEY_CAMERA = "OBS_KEY_CAMERA"
KEY_CAMERAFOCUS = "OBS_KEY_CAMERAFOCUS"
KEY_CONTEXT1 = "OBS_KEY_CONTEXT1"
KEY_CONTEXT2 = "OBS_KEY_CONTEXT2"
KEY_CONTEXT3 = "OBS_KEY_CONTEXT3"
KEY_CONTEXT4 = "OBS_KEY_CONTEXT4"
KEY_FLIP = "OBS_KEY_FLIP"
KEY_HANGUP = "OBS_KEY_HANGUP"
KEY_NO = "OBS_KEY_NO"
KEY_SELECT = "OBS_KEY_SELECT"
KEY_YES = "OBS_KEY_YES"
KEY_TOGGLECALLHANGUP = "OBS_KEY_TOGGLECALLHANGUP"
KEY_VOICEDIAL = "OBS_KEY_VOICEDIAL"
KEY_LASTNUMBERREDIAL = "OBS_KEY_LASTNUMBERREDIAL"
KEY_EXECUTE = "OBS_KEY_EXECUTE"
KEY_PRINTER = "OBS_KEY_PRINTER"
KEY_PLAY = "OBS_KEY_PLAY"
KEY_SLEEP = "OBS_KEY_SLEEP"
KEY_ZOOM = "OBS_KEY_ZOOM"
KEY_CANCEL = "OBS_KEY_CANCEL"

MOUSEBTN_MOUSE1 = "OBS_KEY_MOUSE1"
MOUSEBTN_MOUSE2 = "OBS_KEY_MOUSE2"
MOUSEBTN_MOUSE3 = "OBS_KEY_MOUSE3"
MOUSEBTN_MOUSE4 = "OBS_KEY_MOUSE4"
MOUSEBTN_MOUSE5 = "OBS_KEY_MOUSE5"
MOUSEBTN_MOUSE6 = "OBS_KEY_MOUSE6"
MOUSEBTN_MOUSE7 = "OBS_KEY_MOUSE7"
MOUSEBTN_MOUSE8 = "OBS_KEY_MOUSE8"
MOUSEBTN_MOUSE9 = "OBS_KEY_MOUSE9"
MOUSEBTN_MOUSE10 = "OBS_KEY_MOUSE10"
MOUSEBTN_MOUSE11 = "OBS_KEY_MOUSE11"
MOUSEBTN_MOUSE12 = "OBS_KEY_MOUSE12"
MOUSEBTN_MOUSE13 = "OBS_KEY_MOUSE13"
MOUSEBTN_MOUSE14 = "OBS_KEY_MOUSE14"
MOUSEBTN_MOUSE15 = "OBS_KEY_MOUSE15"
MOUSEBTN_MOUSE16 = "OBS_KEY_MOUSE16"
MOUSEBTN_MOUSE17 = "OBS_KEY_MOUSE17"
MOUSEBTN_MOUSE18 = "OBS_KEY_MOUSE18"
MOUSEBTN_MOUSE19 = "OBS_KEY_MOUSE19"
MOUSEBTN_MOUSE20 = "OBS_KEY_MOUSE20"
MOUSEBTN_MOUSE21 = "OBS_KEY_MOUSE21"
MOUSEBTN_MOUSE22 = "OBS_KEY_MOUSE22"
MOUSEBTN_MOUSE23 = "OBS_KEY_MOUSE23"
MOUSEBTN_MOUSE24 = "OBS_KEY_MOUSE24"
MOUSEBTN_MOUSE25 = "OBS_KEY_MOUSE25"
MOUSEBTN_MOUSE26 = "OBS_KEY_MOUSE26"
MOUSEBTN_MOUSE27 = "OBS_KEY_MOUSE27"
MOUSEBTN_MOUSE28 = "OBS_KEY_MOUSE28"
MOUSEBTN_MOUSE29 = "OBS_KEY_MOUSE29"

KEY_BACKSLASH_RT102 = "OBS_KEY_BACKSLASH_RT102"

KEY_OPEN = "OBS_KEY_OPEN"
KEY_FIND = "OBS_KEY_FIND"
KEY_REDO = "OBS_KEY_REDO"
KEY_UNDO = "OBS_KEY_UNDO"
KEY_FRONT = "OBS_KEY_FRONT"
KEY_PROPS = "OBS_KEY_PROPS"

KEY_VK_CANCEL = "OBS_KEY_VK_CANCEL"
KEY_0x07 = "OBS_KEY_0x07"
KEY_0x0A = "OBS_KEY_0x0A"
KEY_0x0B = "OBS_KEY_0x0B"
KEY_0x0E = "OBS_KEY_0x0E"
KEY_0x0F = "OBS_KEY_0x0F"
KEY_0x16 = "OBS_KEY_0x16"
KEY_VK_JUNJA = "OBS_KEY_VK_JUNJA"
KEY_VK_FINAL = "OBS_KEY_VK_FINAL"
KEY_0x1A = "OBS_KEY_0x1A"
KEY_VK_ACCEPT = "OBS_KEY_VK_ACCEPT"
KEY_VK_MODECHANGE = "OBS_KEY_VK_MODECHANGE"
KEY_VK_SELECT = "OBS_KEY_VK_SELECT"
KEY_VK_PRINT = "OBS_KEY_VK_PRINT"
KEY_VK_EXECUTE = "OBS_KEY_VK_EXECUTE"
KEY_VK_HELP = "OBS_KEY_VK_HELP"
KEY_0x30 = "OBS_KEY_0x30"
KEY_0x31 = "OBS_KEY_0x31"
KEY_0x32 = "OBS_KEY_0x32"
KEY_0x33 = "OBS_KEY_0x33"
KEY_0x34 = "OBS_KEY_0x34"
KEY_0x35 = "OBS_KEY_0x35"
KEY_0x36 = "OBS_KEY_0x36"
KEY_0x37 = "OBS_KEY_0x37"
KEY_0x38 = "OBS_KEY_0x38"
KEY_0x39 = "OBS_KEY_0x39"
KEY_0x3A = "OBS_KEY_0x3A"
KEY_0x3B = "OBS_KEY_0x3B"
KEY_0x3C = "OBS_KEY_0x3C"
KEY_0x3D = "OBS_KEY_0x3D"
KEY_0x3E = "OBS_KEY_0x3E"
KEY_0x3F = "OBS_KEY_0x3F"
KEY_0x40 = "OBS_KEY_0x40"
KEY_0x41 = "OBS_KEY_0x41"
KEY_0x42 = "OBS_KEY_0x42"
KEY_0x43 = "OBS_KEY_0x43"
KEY_0x44 = "OBS_KEY_0x44"
KEY_0x45 = "OBS_KEY_0x45"
KEY_0x46 = "OBS_KEY_0x46"
KEY_0x47 = "OBS_KEY_0x47"
KEY_0x48 = "OBS_KEY_0x48"
KEY_0x49 = "OBS_KEY_0x49"
KEY_0x4A = "OBS_KEY_0x4A"
KEY_0x4B = "OBS_KEY_0x4B"
KEY_0x4C = "OBS_KEY_0x4C"
KEY_0x4D = "OBS_KEY_0x4D"
KEY_0x4E = "OBS_KEY_0x4E"
KEY_0x4F = "OBS_KEY_0x4F"
KEY_0x50 = "OBS_KEY_0x50"
KEY_0x51 = "OBS_KEY_0x51"
KEY_0x52 = "OBS_KEY_0x52"
KEY_0x53 = "OBS_KEY_0x53"
KEY_0x54 = "OBS_KEY_0x54"
KEY_0x55 = "OBS_KEY_0x55"
KEY_0x56 = "OBS_KEY_0x56"
KEY_0x57 = "OBS_KEY_0x57"
KEY_0x58 = "OBS_KEY_0x58"
KEY_0x59 = "OBS_KEY_0x59"
KEY_0x5A = "OBS_KEY_0x5A"
KEY_VK_LWIN = "OBS_KEY_VK_LWIN"
KEY_VK_RWIN = "OBS_KEY_VK_RWIN"
KEY_VK_APPS = "OBS_KEY_VK_APPS"
KEY_KEY_0x5E = "OBS_KEY_0x5E"
KEY_VK_SLEEP = "OBS_KEY_VK_SLEEP"
KEY_VK_SEPARATOR = "OBS_KEY_VK_SEPARATOR"
KEY_0x88 = "OBS_KEY_0x88"
KEY_0x89 = "OBS_KEY_0x89"
KEY_0x8A = "OBS_KEY_0x8A"
KEY_0x8B = "OBS_KEY_0x8B"
KEY_0x8C = "OBS_KEY_0x8C"
KEY_0x8D = "OBS_KEY_0x8D"
KEY_0x8E = "OBS_KEY_0x8E"
KEY_0x8F = "OBS_KEY_0x8F"
KEY_VK_OEM_FJ_JISHO = "OBS_KEY_VK_OEM_FJ_JISHO"
KEY_VK_OEM_FJ_LOYA = "OBS_KEY_VK_OEM_FJ_LOYA"
KEY_VK_OEM_FJ_ROYA = "OBS_KEY_VK_OEM_FJ_ROYA"
KEY_0x97 = "OBS_KEY_0x97"
KEY_0x98 = "OBS_KEY_0x98"
KEY_0x99 = "OBS_KEY_0x99"
KEY_0x9A = "OBS_KEY_0x9A"
KEY_0x9B = "OBS_KEY_0x9B"
KEY_0x9C = "OBS_KEY_0x9C"
KEY_0x9D = "OBS_KEY_0x9D"
KEY_0x9E = "OBS_KEY_0x9E"
KEY_0x9F = "OBS_KEY_0x9F"
KEY_VK_LSHIFT = "OBS_KEY_VK_LSHIFT"
KEY_VK_RSHIFT = "OBS_KEY_VK_RSHIFT"
KEY_VK_LCONTROL = "OBS_KEY_VK_LCONTROL"
KEY_VK_RCONTROL = "OBS_KEY_VK_RCONTROL"
KEY_VK_LMENU = "OBS_KEY_VK_LMENU"
KEY_VK_RMENU = "OBS_KEY_VK_RMENU"
KEY_VK_BROWSER_BACK = "OBS_KEY_VK_BROWSER_BACK"
KEY_VK_BROWSER_FORWARD = "OBS_KEY_VK_BROWSER_FORWARD"
KEY_VK_BROWSER_REFRESH = "OBS_KEY_VK_BROWSER_REFRESH"
KEY_VK_BROWSER_STOP = "OBS_KEY_VK_BROWSER_STOP"
KEY_VK_BROWSER_SEARCH = "OBS_KEY_VK_BROWSER_SEARCH"
KEY_VK_BROWSER_FAVORITES = "OBS_KEY_VK_BROWSER_FAVORITES"
KEY_VK_BROWSER_HOME = "OBS_KEY_VK_BROWSER_HOME"
KEY_VK_VOLUME_MUTE = "OBS_KEY_VK_VOLUME_MUTE"
KEY_VK_VOLUME_DOWN = "OBS_KEY_VK_VOLUME_DOWN"
KEY_VK_VOLUME_UP = "OBS_KEY_VK_VOLUME_UP"
KEY_VK_MEDIA_NEXT_TRACK = "OBS_KEY_VK_MEDIA_NEXT_TRACK"
KEY_VK_MEDIA_PREV_TRACK = "OBS_KEY_VK_MEDIA_PREV_TRACK"
KEY_VK_MEDIA_STOP = "OBS_KEY_VK_MEDIA_STOP"
KEY_VK_MEDIA_PLAY_PAUSE = "OBS_KEY_VK_MEDIA_PLAY_PAUSE"
KEY_VK_LAUNCH_MAIL = "OBS_KEY_VK_LAUNCH_MAIL"
KEY_VK_LAUNCH_MEDIA_SELECT = "OBS_KEY_VK_LAUNCH_MEDIA_SELECT"
KEY_VK_LAUNCH_APP1 = "OBS_KEY_VK_LAUNCH_APP1"
KEY_VK_LAUNCH_APP2 = "OBS_KEY_VK_LAUNCH_APP2"
KEY_0xB8 = "OBS_KEY_0xB8"
KEY_0xB9 = "OBS_KEY_0xB9"
KEY_0xC1 = "OBS_KEY_0xC1"
KEY_0xC2 = "OBS_KEY_0xC2"
KEY_0xC3 = "OBS_KEY_0xC3"
KEY_0xC4 = "OBS_KEY_0xC4"
KEY_0xC5 = "OBS_KEY_0xC5"
KEY_0xC6 = "OBS_KEY_0xC6"
KEY_0xC7 = "OBS_KEY_0xC7"
KEY_0xC8 = "OBS_KEY_0xC8"
KEY_0xC9 = "OBS_KEY_0xC9"
KEY_0xCA = "OBS_KEY_0xCA"
KEY_0xCB = "OBS_KEY_0xCB"
KEY_0xCC = "OBS_KEY_0xCC"
KEY_0xCD = "OBS_KEY_0xCD"
KEY_0xCE= "OBS_KEY_0xCE"
KEY_0xCF= "OBS_KEY_0xCF"
KEY_0xD0 = "OBS_KEY_0xD0"
KEY_0xD1 = "OBS_KEY_0xD1"
KEY_0xD2 = "OBS_KEY_0xD2"
KEY_0xD3 = "OBS_KEY_0xD3"
KEY_0xD4 = "OBS_KEY_0xD4"
KEY_0xD5 = "OBS_KEY_0xD5"
KEY_0xD6 = "OBS_KEY_0xD6"
KEY_0xD7 = "OBS_KEY_0xD7"
KEY_0xD8 = "OBS_KEY_0xD8"
KEY_0xD9 = "OBS_KEY_0xD9"
KEY_0xDA = "OBS_KEY_0xDA"
KEY_VK_OEM_8 = "OBS_KEY_VK_OEM_8"
KEY_0xE0 = "OBS_KEY_0xE0"
KEY_VK_OEM_AX = "OBS_KEY_VK_OEM_AX"
KEY_VK_ICO_HELP = "OBS_KEY_VK_ICO_HELP"
KEY_VK_ICO_00 = "OBS_KEY_VK_ICO_00"
KEY_VK_PROCESSKEY = "OBS_KEY_VK_PROCESSKEY"
KEY_VK_ICO_CLEAR = "OBS_KEY_VK_ICO_CLEAR"
KEY_VK_PACKET = "OBS_KEY_VK_PACKET"
KEY_0xE8 = "OBS_KEY_0xE8"
KEY_OEM_RESET = "OBS_KEY_VK_OEM_RESET"
KEY_OEM_JUMP = "OBS_KEY_VK_OEM_JUMP"
KEY_OEM_PA1 = "OBS_KEY_VK_OEM_PA1"
KEY_OEM_PA2 = "OBS_KEY_VK_OEM_PA2"
KEY_OEM_PA3 = "OBS_KEY_VK_OEM_PA3"
KEY_OEM_WSCTRL = "OBS_KEY_VK_OEM_WSCTRL"
KEY_OEM_CUSEL = "OBS_KEY_VK_OEM_CUSEL"
KEY_OEM_ATTN = "OBS_KEY_VK_OEM_ATTN"
KEY_OEM_FINISH = "OBS_KEY_VK_OEM_FINISH"
KEY_OEM_COPY = "OBS_KEY_VK_OEM_COPY"
KEY_OEM_AUTO = "OBS_KEY_VK_OEM_AUTO"
KEY_OEM_ENLW = "OBS_KEY_VK_OEM_ENLW"
KEY_VK_ATTN = "OBS_KEY_VK_ATTN"
KEY_VK_CRSEL = "OBS_KEY_VK_CRSEL"
KEY_VK_EXSEL = "OBS_KEY_VK_EXSEL"
KEY_VK_EREOF = "OBS_KEY_VK_EREOF"
KEY_VK_PLAY = "OBS_KEY_VK_PLAY"
KEY_VK_ZOOM = "OBS_KEY_VK_ZOOM"
KEY_VK_NONAME = "OBS_KEY_VK_NONAME"
KEY_VK_PA1 = "OBS_KEY_VK_PA1"
KEY_VK_OEM_CLEAR = "OBS_KEY_VK_OEM_CLEAR"


KEY_NAMES = {KEY_NONE : "NONE",
    KEY_RETURN : "RETURN",
    KEY_ENTER : "ENTER",
    KEY_ESCAPE : "ESCAPE",
    KEY_TAB : "TAB",
    KEY_BACKTAB : "BACKTAB",
    KEY_BACKSPACE : "BACKSPACE",
    KEY_INSERT : "INSERT",
    KEY_DELETE : "DELETE",
    KEY_PAUSE : "PAUSE",
    KEY_PRINT : "PRINT",
    KEY_SYSREQ : "SYSREQ",
    KEY_CLEAR : "CLEAR",
    KEY_HOME : "HOME",
    KEY_END : "END",
    KEY_LEFT : "LEFT",
    KEY_UP : "UP",
    KEY_RIGHT : "RIGHT",
    KEY_DOWN : "DOWN",
    KEY_PAGEUP : "PAGEUP",
    KEY_PAGEDOWN : "PAGEDOWN",

    KEY_SHIFT : "SHIFT",
    KEY_CONTROL : "CONTROL",
    KEY_META : "META",
    KEY_ALT : "ALT",
    KEY_ALTGR : "ALTGR",
    KEY_CAPSLOCK : "CAPSLOCK",
    KEY_NUMLOCK : "NUMLOCK",
    KEY_SCROLLLOCK : "SCROLLLOCK",

    KEY_F1 : "F1",
    KEY_F2 : "F2",
    KEY_F3 : "F3",
    KEY_F4 : "F4",
    KEY_F5 : "F5",
    KEY_F6 : "F6",
    KEY_F7 : "F7",
    KEY_F8 : "F8",
    KEY_F9 : "F9",
    KEY_F10 : "F10",
    KEY_F11 : "F11",
    KEY_F12 : "F12",
    KEY_F13 : "F13",
    KEY_F14 : "F14",
    KEY_F15 : "F15",
    KEY_F16 : "F16",
    KEY_F17 : "F17",
    KEY_F18 : "F18",
    KEY_F19 : "F19",
    KEY_F20 : "F20",
    KEY_F21 : "F21",
    KEY_F22 : "F22",
    KEY_F23 : "F23",
    KEY_F24 : "F24",
    KEY_F25 : "F25",
    KEY_F26 : "F26",
    KEY_F27 : "F27",
    KEY_F28 : "F28",
    KEY_F29 : "F29",
    KEY_F30 : "F30",
    KEY_F31 : "F31",
    KEY_F32 : "F32",
    KEY_F33 : "F33",
    KEY_F34 : "F34",
    KEY_F35 : "F35",

    KEY_MENU : "MENU",
    KEY_HYPER_L : "HYPER L",
    KEY_HYPER_R : "HYPER R",
    KEY_HELP : "HELP",
    KEY_DIRECTION_L : "DIRECTION L",
    KEY_DIRECTION_R : "DIRECTION R",

    KEY_SPACE : "SPACE",
    KEY_EXCLAM : "EXCLAM",
    KEY_QUOTEDBL : "QUOTEDBL",
    KEY_NUMBERSIGN : "NUMBERSIGN",
    KEY_DOLLAR : "DOLLAR",
    KEY_PERCENT : "PERCENT",
    KEY_AMPERSAND : "AMPERSAND",
    KEY_APOSTROPHE : "APOSTROPHE",
    KEY_PARENLEFT : "PARENLEFT",
    KEY_PARENRIGHT : "PARENRIGHT",
    KEY_ASTERISK : "ASTERISK",
    KEY_PLUS : "PLUS",
    KEY_COMMA : "COMMA",
    KEY_MINUS : "MINUS",
    KEY_PERIOD : "PERIOD",
    KEY_SLASH : "SLASH",
    KEY_0 : "0",
    KEY_1 : "1",
    KEY_2 : "2",
    KEY_3 : "3",
    KEY_4 : "4",
    KEY_5 : "5",
    KEY_6 : "6",
    KEY_7 : "7",
    KEY_8 : "8",
    KEY_9 : "9",
    KEY_NUMEQUAL : "NUMEQUAL",
    KEY_NUMASTERISK : "NUMASTERISK",
    KEY_NUMPLUS : "NUMPLUS",
    KEY_NUMCOMMA : "NUMCOMMA",
    KEY_NUMMINUS : "NUMMINUS",
    KEY_NUMPERIOD : "NUMPERIOD",
    KEY_NUMSLASH : "NUMSLASH",
    KEY_NUM0 : "NUM0",
    KEY_NUM1 : "NUM1",
    KEY_NUM2 : "NUM2",
    KEY_NUM3 : "NUM3",
    KEY_NUM4 : "NUM4",
    KEY_NUM5 : "NUM5",
    KEY_NUM6 : "NUM6",
    KEY_NUM7 : "NUM7",
    KEY_NUM8 : "NUM8",
    KEY_NUM9 : "NUM9",
    KEY_COLON : "COLON",
    KEY_SEMICOLON : "SEMICOLON",
    KEY_QUOTE : "QUOTE",
    KEY_LESS : "LESS",
    KEY_EQUAL : "EQUAL",
    KEY_GREATER : "GREATER",
    KEY_QUESTION : "QUESTION",
    KEY_AT : "AT",
    KEY_A : "A",
    KEY_B : "B",
    KEY_C : "C",
    KEY_D : "D",
    KEY_E : "E",
    KEY_F : "F",
    KEY_G : "G",
    KEY_H : "H",
    KEY_I : "I",
    KEY_J : "J",
    KEY_K : "K",
    KEY_L : "L",
    KEY_M : "M",
    KEY_N : "N",
    KEY_O : "O",
    KEY_P : "P",
    KEY_Q : "Q",
    KEY_R : "R",
    KEY_S : "S",
    KEY_T : "T",
    KEY_U : "U",
    KEY_V : "V",
    KEY_W : "W",
    KEY_X : "X",
    KEY_Y : "Y",
    KEY_Z : "Z",
    KEY_BRACKETLEFT : "BRACKETLEFT",
    KEY_BACKSLASH : "BACKSLASH",
    KEY_BRACKETRIGHT : "BRACKETRIGHT",
    KEY_ASCIICIRCUM : "ASCIICIRCUM",
    KEY_UNDERSCORE : "UNDERSCORE",
    KEY_QUOTELEFT : "QUOTELEFT",
    KEY_BRACELEFT : "BRACELEFT",
    KEY_BAR : "BAR",
    KEY_BRACERIGHT : "BRACERIGHT",
    KEY_ASCIITILDE : "ASCIITILDE",
    KEY_NOBREAKSPACE : "NOBREAKSPACE",
    KEY_EXCLAMDOWN : "EXCLAMDOWN",
    KEY_CENT : "CENT",
    KEY_STERLING : "STERLING",
    KEY_CURRENCY : "CURRENCY",
    KEY_YEN : "YEN",
    KEY_BROKENBAR : "BROKENBAR",
    KEY_SECTION : "SECTION",
    KEY_DIAERESIS : "DIAERESIS",
    KEY_COPYRIGHT : "COPYRIGHT",
    KEY_ORDFEMININE : "ORDFEMININE",
    KEY_GUILLEMOTLEFT : "GUILLEMOTLEFT",
    KEY_NOTSIGN : "NOTSIGN",
    KEY_HYPHEN : "HYPHEN",
    KEY_REGISTERED : "REGISTERED",
    KEY_MACRON : "MACRON",
    KEY_DEGREE : "DEGREE",
    KEY_PLUSMINUS : "PLUSMINUS",
    KEY_TWOSUPERIOR : "TWOSUPERIOR",
    KEY_THREESUPERIOR : "THREESUPERIOR",
    KEY_ACUTE : "ACUTE",
    KEY_MU : "MU",
    KEY_PARAGRAPH : "PARAGRAPH",
    KEY_PERIODCENTERED : "PERIODCENTERED",
    KEY_CEDILLA : "CEDILLA",
    KEY_ONESUPERIOR : "ONESUPERIOR",
    KEY_MASCULINE : "MASCULINE",
    KEY_GUILLEMOTRIGHT : "GUILLEMOTRIGHT",
    KEY_ONEQUARTER : "ONEQUARTER",
    KEY_ONEHALF : "ONEHALF",
    KEY_THREEQUARTERS : "THREEQUARTERS",
    KEY_QUESTIONDOWN : "QUESTIONDOWN",
    KEY_AGRAVE : "AGRAVE",
    KEY_AACUTE : "AACUTE",
    KEY_ACIRCUMFLEX : "ACIRCUMFLEX",
    KEY_ATILDE : "ATILDE",
    KEY_ADIAERESIS : "ADIAERESIS",
    KEY_ARING : "ARING",
    KEY_AE : "AE",
    KEY_CCEDILLA : "CCEDILLA",
    KEY_EGRAVE : "EGRAVE",
    KEY_EACUTE : "EACUTE",
    KEY_ECIRCUMFLEX : "ECIRCUMFLEX",
    KEY_EDIAERESIS : "EDIAERESIS",
    KEY_IGRAVE : "IGRAVE",
    KEY_IACUTE : "IACUTE",
    KEY_ICIRCUMFLEX : "ICIRCUMFLEX",
    KEY_IDIAERESIS : "IDIAERESIS",
    KEY_ETH : "ETH",
    KEY_NTILDE : "NTILDE",
    KEY_OGRAVE : "OGRAVE",
    KEY_OACUTE : "OACUTE",
    KEY_OCIRCUMFLEX : "OCIRCUMFLEX",
    KEY_OTILDE : "OTILDE",
    KEY_ODIAERESIS : "ODIAERESIS",
    KEY_MULTIPLY : "MULTIPLY",
    KEY_OOBLIQUE : "OOBLIQUE",
    KEY_UGRAVE : "UGRAVE",
    KEY_UACUTE : "UACUTE",
    KEY_UCIRCUMFLEX : "UCIRCUMFLEX",
    KEY_UDIAERESIS : "UDIAERESIS",
    KEY_YACUTE : "YACUTE",
    KEY_THORN : "THORN",
    KEY_SSHARP : "SSHARP",
    KEY_DIVISION : "DIVISION",
    KEY_YDIAERESIS : "YDIAERESIS",
    KEY_MULTI_KEY : "MULTI KEY",
    KEY_CODEINPUT : "CODEINPUT",
    KEY_SINGLECANDIDATE : "SINGLECANDIDATE",
    KEY_MULTIPLECANDIDATE : "MULTIPLECANDIDATE",
    KEY_PREVIOUSCANDIDATE : "PREVIOUSCANDIDATE",
    KEY_MODE_SWITCH : "MODE_SWITCH",
    KEY_KANJI : "KANJI",
    KEY_MUHENKAN : "MUHENKAN",
    KEY_HENKAN : "HENKAN",
    KEY_ROMAJI : "ROMAJI",
    KEY_HIRAGANA : "HIRAGANA",
    KEY_KATAKANA : "KATAKANA",
    KEY_HIRAGANA_KATAKANA : "HIRAGANA KATAKANA",
    KEY_ZENKAKU : "ZENKAKU",
    KEY_HANKAKU : "HANKAKU",
    KEY_ZENKAKU_HANKAKU : "ZENKAKU HANKAKU",
    KEY_TOUROKU : "TOUROKU",
    KEY_MASSYO : "MASSYO",
    KEY_KANA_LOCK : "KANA LOCK",
    KEY_KANA_SHIFT : "KANA SHIFT",
    KEY_EISU_SHIFT : "EISU SHIFT",
    KEY_EISU_TOGGLE : "EISU TOGGLE",
    KEY_HANGUL : "HANGUL",
    KEY_HANGUL_START : "HANGUL START",
    KEY_HANGUL_END : "HANGUL END",
    KEY_HANGUL_HANJA : "HANGUL HANJA",
    KEY_HANGUL_JAMO : "HANGUL JAMO",
    KEY_HANGUL_ROMAJA : "HANGUL ROMAJA",
    KEY_HANGUL_JEONJA : "HANGUL JEONJA",
    KEY_HANGUL_BANJA : "HANGUL BANJA",
    KEY_HANGUL_PREHANJA : "HANGUL PREHANJA",
    KEY_HANGUL_POSTHANJA : "HANGUL POSTHANJA",
    KEY_HANGUL_SPECIAL : "HANGUL SPECIAL",
    KEY_DEAD_GRAVE : "DEAD GRAVE",
    KEY_DEAD_ACUTE : "DEAD ACUTE",
    KEY_DEAD_CIRCUMFLEX : "DEAD CIRCUMFLEX",
    KEY_DEAD_TILDE : "DEAD TILDE",
    KEY_DEAD_MACRON : "DEAD MACRON",
    KEY_DEAD_BREVE : "DEAD BREVE",
    KEY_DEAD_ABOVEDOT : "DEAD ABOVEDOT",
    KEY_DEAD_DIAERESIS : "DEAD DIAERESIS",
    KEY_DEAD_ABOVERING : "DEAD ABOVERING",
    KEY_DEAD_DOUBLEACUTE : "DEAD DOUBLEACUTE",
    KEY_DEAD_CARON : "DEAD CARON",
    KEY_DEAD_CEDILLA : "DEAD CEDILLA",
    KEY_DEAD_OGONEK : "DEAD OGONEK",
    KEY_DEAD_IOTA : "DEAD IOTA",
    KEY_DEAD_VOICED_SOUND : "DEAD VOICED SOUND",
    KEY_DEAD_SEMIVOICED_SOUND : "DEAD SEMIVOICED SOUND",
    KEY_DEAD_BELOWDOT : "DEAD BELOWDOT",
    KEY_DEAD_HOOK : "DEAD HOOK",
    KEY_DEAD_HORN : "DEAD HORN",
    KEY_BACK : "BACK",
    KEY_FORWARD : "FORWARD",
    KEY_STOP : "STOP",
    KEY_REFRESH : "REFRESH",
    KEY_VOLUMEDOWN : "VOLUMEDOWN",
    KEY_VOLUMEMUTE : "VOLUMEMUTE",
    KEY_VOLUMEUP : "VOLUMEUP",
    KEY_BASSBOOST : "BASSBOOST",
    KEY_BASSUP : "BASSUP",
    KEY_BASSDOWN : "BASSDOWN",
    KEY_TREBLEUP : "TREBLEUP",
    KEY_TREBLEDOWN : "TREBLEDOWN",
    KEY_MEDIAPLAY : "MEDIAPLAY",
    KEY_MEDIASTOP : "MEDIASTOP",
    KEY_MEDIAPREVIOUS : "MEDIAPREVIOUS",
    KEY_MEDIANEXT : "MEDIANEXT",
    KEY_MEDIARECORD : "MEDIARECORD",
    KEY_MEDIAPAUSE : "MEDIAPAUSE",
    KEY_MEDIATOGGLEPLAYPAUSE : "MEDIATOGGLEPLAYPAUSE",
    KEY_HOMEPAGE : "HOMEPAGE",
    KEY_FAVORITES : "FAVORITES",
    KEY_SEARCH : "SEARCH",
    KEY_STANDBY : "STANDBY",
    KEY_OPENURL : "OPENURL",
    KEY_LAUNCHMAIL : "LAUNCHMAIL",
    KEY_LAUNCHMEDIA : "LAUNCHMEDIA",
    KEY_LAUNCH0 : "LAUNCH0",
    KEY_LAUNCH1 : "LAUNCH1",
    KEY_LAUNCH2 : "LAUNCH2",
    KEY_LAUNCH3 : "LAUNCH3",
    KEY_LAUNCH4 : "LAUNCH4",
    KEY_LAUNCH5 : "LAUNCH5",
    KEY_LAUNCH6 : "LAUNCH6",
    KEY_LAUNCH7 : "LAUNCH7",
    KEY_LAUNCH8 : "LAUNCH8",
    KEY_LAUNCH9 : "LAUNCH9",
    KEY_LAUNCHA : "LAUNCHA",
    KEY_LAUNCHB : "LAUNCHB",
    KEY_LAUNCHC : "LAUNCHC",
    KEY_LAUNCHD : "LAUNCHD",
    KEY_LAUNCHE : "LAUNCHE",
    KEY_LAUNCHF : "LAUNCHF",
    KEY_LAUNCHG : "LAUNCHG",
    KEY_LAUNCHH : "LAUNCHH",
    KEY_MONBRIGHTNESSUP : "MONBRIGHTNESSUP",
    KEY_MONBRIGHTNESSDOWN : "MONBRIGHTNESSDOWN",
    KEY_KEYBOARDLIGHTONOFF : "KEYBOARDLIGHTONOFF",
    KEY_KEYBOARDBRIGHTNESSUP : "KEYBOARDBRIGHTNESSUP",
    KEY_KEYBOARDBRIGHTNESSDOWN : "KEYBOARDBRIGHTNESSDOWN",
    KEY_POWEROFF : "POWEROFF",
    KEY_WAKEUP : "WAKEUP",
    KEY_EJECT : "EJECT",
    KEY_SCREENSAVER : "SCREENSAVER",
    KEY_WWW : "WWW",
    KEY_MEMO : "MEMO",
    KEY_LIGHTBULB : "LIGHTBULB",
    KEY_SHOP : "SHOP",
    KEY_HISTORY : "HISTORY",
    KEY_ADDFAVORITE : "ADDFAVORITE",
    KEY_HOTLINKS : "HOTLINKS",
    KEY_BRIGHTNESSADJUST : "BRIGHTNESSADJUST",
    KEY_FINANCE : "FINANCE",
    KEY_COMMUNITY : "COMMUNITY",
    KEY_AUDIOREWIND : "AUDIOREWIND",
    KEY_BACKFORWARD : "BACKFORWARD",
    KEY_APPLICATIONLEFT : "APPLICATIONLEFT",
    KEY_APPLICATIONRIGHT : "APPLICATIONRIGHT",
    KEY_BOOK : "BOOK",
    KEY_CD : "CD",
    KEY_CALCULATOR : "CALCULATOR",
    KEY_TODOLIST : "TODOLIST",
    KEY_CLEARGRAB : "CLEARGRAB",
    KEY_CLOSE : "CLOSE",
    KEY_COPY : "COPY",
    KEY_CUT : "CUT",
    KEY_DISPLAY : "DISPLAY",
    KEY_DOS : "DOS",
    KEY_DOCUMENTS : "DOCUMENTS",
    KEY_EXCEL : "EXCEL",
    KEY_EXPLORER : "EXPLORER",
    KEY_GAME : "GAME",
    KEY_GO : "GO",
    KEY_ITOUCH : "ITOUCH",
    KEY_LOGOFF : "LOGOFF",
    KEY_MARKET : "MARKET",
    KEY_MEETING : "MEETING",
    KEY_MENUKB : "MENUKB",
    KEY_MENUPB : "MENUPB",
    KEY_MYSITES : "MYSITES",
    KEY_NEWS : "NEWS",
    KEY_OFFICEHOME : "OFFICEHOME",
    KEY_OPTION : "OPTION",
    KEY_PASTE : "PASTE",
    KEY_PHONE : "PHONE",
    KEY_CALENDAR : "CALENDAR",
    KEY_REPLY: "REPLY",
    KEY_RELOAD : "RELOAD",
    KEY_ROTATEWINDOWS : "ROTATEWINDOWS",
    KEY_ROTATIONPB : "ROTATIONPB",
    KEY_ROTATIONKB: "ROTATIONKB",
    KEY_SAVE : "SAVE",
    KEY_SEND : "SEND",
    KEY_SPELL : "SPELL",
    KEY_SPLITSCREEN : "SPLITSCREEN",
    KEY_SUPPORT : "SUPPORT",
    KEY_TASKPANE : "TASKPANE",
    KEY_TERMINAL : "TERMINAL",
    KEY_TOOLS : "TOOLS",
    KEY_TRAVEL : "TRAVEL",
    KEY_VIDEO : "VIDEO",
    KEY_WORD : "WORD",
    KEY_XFER : "XFER",
    KEY_ZOOMIN : "ZOOMIN",
    KEY_ZOOMOUT : "ZOOMOUT",
    KEY_AWAY : "AWAY",
    KEY_MESSENGER : "MESSENGER",
    KEY_WEBCAM : "WEBCAM",
    KEY_MAILFORWARD : "MAILFORWARD",
    KEY_PICTURES : "PICTURES",
    KEY_MUSIC : "MUSIC",
    KEY_BATTERY : "BATTERY",
    KEY_BLUETOOTH : "BLUETOOTH",
    KEY_WLAN : "WLAN",
    KEY_UWB : "UWB",
    KEY_AUDIOFORWARD : "AUDIOFORWARD",
    KEY_AUDIOREPEAT : "AUDIOREPEAT",
    KEY_AUDIORANDOMPLAY : "AUDIORANDOMPLAY",
    KEY_SUBTITLE : "SUBTITLE",
    KEY_AUDIOCYCLETRACK : "AUDIOCYCLETRACK",
    KEY_TIME : "TIME",
    KEY_HIBERNATE : "HIBERNATE",
    KEY_VIEW : "VIEW",
    KEY_TOPMENU : "TOPMENU",
    KEY_POWERDOWN : "POWERDOWN",
    KEY_SUSPEND : "SUSPEND",
    KEY_CONTRASTADJUST : "CONTRASTADJUST",
    KEY_MEDIALAST : "MEDIALAST",
    KEY_CALL : "CALL",
    KEY_CAMERA : "CAMERA",
    KEY_CAMERAFOCUS : "CAMERAFOCUS",
    KEY_CONTEXT1 : "CONTEXT1",
    KEY_CONTEXT2 : "CONTEXT2",
    KEY_CONTEXT3 : "CONTEXT3",
    KEY_CONTEXT4 : "CONTEXT4",
    KEY_FLIP : "FLIP",
    KEY_HANGUP : "HANGUP",
    KEY_NO : "NO",
    KEY_SELECT : "SELECT",
    KEY_YES : "YES",
    KEY_TOGGLECALLHANGUP : "TOGGLECALLHANGUP",
    KEY_VOICEDIAL : "VOICEDIAL",
    KEY_LASTNUMBERREDIAL : "LASTNUMBERREDIAL",
    KEY_EXECUTE : "EXECUTE",
    KEY_PRINTER : "PRINTER",
    KEY_PLAY : "PLAY",
    KEY_SLEEP : "SLEEP",
    KEY_ZOOM : "ZOOM",
    KEY_CANCEL : "CANCEL",

    MOUSEBTN_MOUSE1 : "MOUSE1",
    MOUSEBTN_MOUSE2 : "MOUSE2",
    MOUSEBTN_MOUSE3 : "MOUSE3",
    MOUSEBTN_MOUSE4 : "MOUSE4",
    MOUSEBTN_MOUSE5 : "MOUSE5",
    MOUSEBTN_MOUSE6 : "MOUSE6",
    MOUSEBTN_MOUSE7 : "MOUSE7",
    MOUSEBTN_MOUSE8 : "MOUSE8",
    MOUSEBTN_MOUSE9 : "MOUSE9",
    MOUSEBTN_MOUSE10 : "MOUSE10",
    MOUSEBTN_MOUSE11 : "MOUSE11",
    MOUSEBTN_MOUSE12 : "MOUSE12",
    MOUSEBTN_MOUSE13 : "MOUSE13",
    MOUSEBTN_MOUSE14 : "MOUSE14",
    MOUSEBTN_MOUSE15 : "MOUSE15",
    MOUSEBTN_MOUSE16 : "MOUSE16",
    MOUSEBTN_MOUSE17 : "MOUSE17",
    MOUSEBTN_MOUSE18 : "MOUSE18",
    MOUSEBTN_MOUSE19 : "MOUSE19",
    MOUSEBTN_MOUSE20 : "MOUSE20",
    MOUSEBTN_MOUSE21 : "MOUSE21",
    MOUSEBTN_MOUSE22 : "MOUSE22",
    MOUSEBTN_MOUSE23 : "MOUSE23",
    MOUSEBTN_MOUSE24 : "MOUSE24",
    MOUSEBTN_MOUSE25 : "MOUSE25",
    MOUSEBTN_MOUSE26 : "MOUSE26",
    MOUSEBTN_MOUSE27 : "MOUSE27",
    MOUSEBTN_MOUSE28 : "MOUSE28",
    MOUSEBTN_MOUSE29 : "MOUSE29",

    KEY_BACKSLASH_RT102 : "BACKSLASH RT102",

    KEY_OPEN : "OPEN",
    KEY_FIND : "FIND",
    KEY_REDO : "REDO",
    KEY_UNDO : "UNDO",
    KEY_FRONT : "FRONT",
    KEY_PROPS : "PROPS",

    KEY_VK_CANCEL : "VK CANCEL",
    KEY_0x07 : "0x07",
    KEY_0x0A : "0x0A",
    KEY_0x0B : "0x0B",
    KEY_0x0E : "0x0E",
    KEY_0x0F : "0x0F",
    KEY_0x16 : "0x16",
    KEY_VK_JUNJA : "VK JUNJA",
    KEY_VK_FINAL : "VK FINAL",
    KEY_0x1A : "0x1A",
    KEY_VK_ACCEPT : "VK ACCEPT",
    KEY_VK_MODECHANGE : "VK MODECHANGE",
    KEY_VK_SELECT : "VK SELECT",
    KEY_VK_PRINT : "VK PRINT",
    KEY_VK_EXECUTE : "VK EXECUTE",
    KEY_VK_HELP : "VK HELP",
    KEY_0x30 : "0x30",
    KEY_0x31 : "0x31",
    KEY_0x32 : "0x32",
    KEY_0x33 : "0x33",
    KEY_0x34 : "0x34",
    KEY_0x35 : "0x35",
    KEY_0x36 : "0x36",
    KEY_0x37 : "0x37",
    KEY_0x38 : "0x38",
    KEY_0x39 : "0x39",
    KEY_0x3A : "0x3A",
    KEY_0x3B : "0x3B",
    KEY_0x3C : "0x3C",
    KEY_0x3D : "0x3D",
    KEY_0x3E : "0x3E",
    KEY_0x3F : "0x3F",
    KEY_0x40 : "0x40",
    KEY_0x41 : "0x41",
    KEY_0x42 : "0x42",
    KEY_0x43 : "0x43",
    KEY_0x44 : "0x44",
    KEY_0x45 : "0x45",
    KEY_0x46 : "0x46",
    KEY_0x47 : "0x47",
    KEY_0x48 : "0x48",
    KEY_0x49 : "0x49",
    KEY_0x4A : "0x4A",
    KEY_0x4B : "0x4B",
    KEY_0x4C : "0x4C",
    KEY_0x4D : "0x4D",
    KEY_0x4E : "0x4E",
    KEY_0x4F : "0x4F",
    KEY_0x50 : "0x50",
    KEY_0x51 : "0x51",
    KEY_0x52 : "0x52",
    KEY_0x53 : "0x53",
    KEY_0x54 : "0x54",
    KEY_0x55 : "0x55",
    KEY_0x56 : "0x56",
    KEY_0x57 : "0x57",
    KEY_0x58 : "0x58",
    KEY_0x59 : "0x59",
    KEY_0x5A : "0x5A",
    KEY_VK_LWIN : "VK LWIN",
    KEY_VK_RWIN : "VK RWIN",
    KEY_VK_APPS : "VK APPS",
    KEY_KEY_0x5E : "0x5E",
    KEY_VK_SLEEP : "VK SLEEP",
    KEY_VK_SEPARATOR : "VK SEPARATOR",
    KEY_0x88 : "0x88",
    KEY_0x89 : "0x89",
    KEY_0x8A : "0x8A",
    KEY_0x8B : "0x8B",
    KEY_0x8C : "0x8C",
    KEY_0x8D : "0x8D",
    KEY_0x8E : "0x8E",
    KEY_0x8F : "0x8F",
    KEY_VK_OEM_FJ_JISHO : "VK OEM FJ JISHO",
    KEY_VK_OEM_FJ_LOYA : "VK OEM FJ LOYA",
    KEY_VK_OEM_FJ_ROYA : "VK OEM FJ ROYA",
    KEY_0x97 : "0x97",
    KEY_0x98 : "0x98",
    KEY_0x99 : "0x99",
    KEY_0x9A : "0x9A",
    KEY_0x9B : "0x9B",
    KEY_0x9C : "0x9C",
    KEY_0x9D : "0x9D",
    KEY_0x9E : "0x9E",
    KEY_0x9F : "0x9F",
    KEY_VK_LSHIFT : "VK LSHIFT",
    KEY_VK_RSHIFT : "VK RSHIFT",
    KEY_VK_LCONTROL : "VK LCONTROL",
    KEY_VK_RCONTROL : "VK RCONTROL",
    KEY_VK_LMENU : "VK LMENU",
    KEY_VK_RMENU : "VK RMENU",
    KEY_VK_BROWSER_BACK : "VK BROWSER BACK",
    KEY_VK_BROWSER_FORWARD : "VK BROWSER FORWARD",
    KEY_VK_BROWSER_REFRESH : "VK BROWSER REFRESH",
    KEY_VK_BROWSER_STOP : "VK BROWSER STOP",
    KEY_VK_BROWSER_SEARCH : "VK BROWSER SEARCH",
    KEY_VK_BROWSER_FAVORITES : "VK BROWSER FAVORITES",
    KEY_VK_BROWSER_HOME : "VK BROWSER HOME",
    KEY_VK_VOLUME_MUTE : "VK VOLUME MUTE",
    KEY_VK_VOLUME_DOWN : "VK VOLUME DOWN",
    KEY_VK_VOLUME_UP : "VK VOLUME UP",
    KEY_VK_MEDIA_NEXT_TRACK : "VK MEDIA NEXT TRACK",
    KEY_VK_MEDIA_PREV_TRACK : "VK MEDIA PREV TRACK",
    KEY_VK_MEDIA_STOP : "VK MEDIA STOP",
    KEY_VK_MEDIA_PLAY_PAUSE : "VK MEDIA PLAY PAUSE",
    KEY_VK_LAUNCH_MAIL : "VK LAUNCH MAIL",
    KEY_VK_LAUNCH_MEDIA_SELECT : "VK LAUNCH MEDIA SELECT",
    KEY_VK_LAUNCH_APP1 : "VK LAUNCH APP1",
    KEY_VK_LAUNCH_APP2 : "VK LAUNCH APP2",
    KEY_0xB8 : "0xB8",
    KEY_0xB9 : "0xB9",
    KEY_0xC1 : "0xC1",
    KEY_0xC2 : "0xC2",
    KEY_0xC3 : "0xC3",
    KEY_0xC4 : "0xC4",
    KEY_0xC5 : "0xC5",
    KEY_0xC6 : "0xC6",
    KEY_0xC7 : "0xC7",
    KEY_0xC8 : "0xC8",
    KEY_0xC9 : "0xC9",
    KEY_0xCA : "0xCA",
    KEY_0xCB : "0xCB",
    KEY_0xCC : "0xCC",
    KEY_0xCD : "0xCD",
    KEY_0xCE: "0xCE",
    KEY_0xCF: "0xCF",
    KEY_0xD0 : "0xD0",
    KEY_0xD1 : "0xD1",
    KEY_0xD2 : "0xD2",
    KEY_0xD3 : "0xD3",
    KEY_0xD4 : "0xD4",
    KEY_0xD5 : "0xD5",
    KEY_0xD6 : "0xD6",
    KEY_0xD7 : "0xD7",
    KEY_0xD8 : "0xD8",
    KEY_0xD9 : "0xD9",
    KEY_0xDA : "0xDA",
    KEY_VK_OEM_8 : "VK OEM 8",
    KEY_0xE0 : "0xE0",
    KEY_VK_OEM_AX : "VK OEM AX",
    KEY_VK_ICO_HELP : "VK ICO HELP",
    KEY_VK_ICO_00 : "VK ICO 00",
    KEY_VK_PROCESSKEY : "VK PROCESSKEY",
    KEY_VK_ICO_CLEAR : "VK ICO CLEAR",
    KEY_VK_PACKET : "VK PACKET",
    KEY_0xE8 : "0xE8",
    KEY_OEM_RESET : "VK OEM RESET",
    KEY_OEM_JUMP : "VK OEM JUMP",
    KEY_OEM_PA1 : "VK OEM PA1",
    KEY_OEM_PA2 : "VK OEM PA2",
    KEY_OEM_PA3 : "VK OEM PA3",
    KEY_OEM_WSCTRL : "VK OEM WSCTRL",
    KEY_OEM_CUSEL : "VK OEM CUSEL",
    KEY_OEM_ATTN : "VK OEM ATTN",
    KEY_OEM_FINISH : "VK OEM FINISH",
    KEY_OEM_COPY : "VK OEM_COPY",
    KEY_OEM_AUTO : "VK OEM_AUTO",
    KEY_OEM_ENLW : "VK OEM_ENLW",
    KEY_VK_ATTN : "VK ATTN",
    KEY_VK_CRSEL : "VK CRSEL",
    KEY_VK_EXSEL : "VK EXSEL",
    KEY_VK_EREOF : "VK EREOF",
    KEY_VK_PLAY : "VK PLAY",
    KEY_VK_ZOOM : "VK ZOOM",
    KEY_VK_NONAME : "VK NONAME",
    KEY_VK_PA1 : "VK PA1",
    KEY_VK_OEM_CLEAR : "VK OEM CLEAR"
}

REVERSE_KEY_NAMES = reverseLUT(KEY_NAMES)
