"""
Constants
"""

# **************************************************
API_KEY_NAME: str = "AVALAI_API_KEY"
BASE_URL: str = "https://api.avalai.ir/v1"
# **************************************************

# **************************************************
MODELS: list[str] = ["gpt-4o", "gpt-4o-mini", "gpt-3.5-turbo"]
# **************************************************

# **************************************************
SYSTEM_PROMPT: str = """
    You are a professional translator assistant from English language to Farsi language.

    User must write just one word in English language.

    If user wrote more than one word, or one word but \
    not in English language, answer 'Error! Try Again...'.

    Just translate English word, based on the below instructions.

    Write the translated to Farsi language of user word in ## part.
    Write the English Pronounce of user word in ### part.
    Write the 5 English Synonyms in #### parts.
    Write the 2 English Antonyms in ##### parts.
    Write the 2 sample and simple English sentences in ###### parts.

    Just write the below text based on above instructions and replace '#' \
    with your answers and never write '#' in your result.

    Translated to Farsi Language: ##
    English Pronounce: ###

    Synonyms:
    1. ####
    2. ####
    3. ####
    4. ####
    5. ####

    Antonyms:
    1. #####
    2. #####

    Two Sample Sentences:
    1. ######
    2. ######
"""
# **************************************************

# **************************************************
# *** Streamlit Constants **************************
# **************************************************

# **************************************************
PAGE_STYLE = """
<style>
    @import url('https://fonts.cdnfonts.com/css/iransansx');

    html, body, p, h1, h2, h3, h4, h5, h6, input, textarea {
        font-family: 'IRANSansX', tahoma !important;
    }

    div.e121c1cl0 {
        margin-right: 10px !important;
    }

    [role=radiogroup], pre {
        direction: ltr;
        text-align: left;
    }

    .block-container, section, input, textarea {
        direction: rtl;
        text-align: justify;
    }

    .stMarkdown {
        direction: ltr;
        text-align: left;
    }
</style>
"""
# **************************************************

# **************************************************
PAGE_ICON: str = "👋"
PAGE_LAYOUT: str = "wide"
# PAGE_TITLE: str = "DT Chatbot"
PAGE_TITLE: str = "DT Dictionary"
# PAGE_HEADER: str = "👋 به Chatbot داریوش تصدیقی خوش آمدید!"
PAGE_HEADER: str = "👋" + "به دیکشنری داریوش تصدیقی خوش آمدید" + "!"
# **************************************************

# **************************************************
# CHAT_INPUT_PLACEHOLDER: str = "لطفا سوال خودتان را اینجا بنویسید..."
CHAT_INPUT_PLACEHOLDER: str = "لطفا کلمه انگلیسی خودتان را در این کادر، وارد نمایید..."
FIRST_RESPONSE: str = "سلام، وقت به خیر. من داریوش هستم، چه کمکی می‌تونم به شما بکنم؟"

PAGE_INFO: str = """
<p style="direction: rtl; text-align: justify;">
    👋
    دوست گرامی، شما می‌توانید در سایت ذیل
    ثبت‌نام کرده، و پس از ورود، نسبت به دریافت
    API Key
    اقدام نمایید:
</p>

<p style="direction: ltr; text-align: left;">
    🌐 <a href="https://avalai.ir">https://avalai.ir</a>
</p>

<hr />

<p style="direction: rtl; text-align: justify;">
    👋
    توسعه دهنده: داریوش تصدیقی
</p>

<p style="direction: ltr; text-align: left;">
    Version: 1.1
    <br />
    📞 +98-912-108-7461
    <br />
    📧 DariushT@Gmail.com
    <br />
    🌐 <a href='https://t.me/IranianExperts'>https://t.me/IranianExperts</a>
</p>

<hr />
"""
# **************************************************

if __name__ == "__main__":
    print("This file is a library file! So, you cannot run this file directly...")
