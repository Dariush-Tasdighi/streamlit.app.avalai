"""
Streamlit Library
"""

import streamlit as st
import library_constants


def set_page_config() -> None:
    """
    Set Page Config Function
    """

    st.set_page_config(
        layout=library_constants.PAGE_LAYOUT,
        page_icon=library_constants.PAGE_ICON,
        page_title=library_constants.PAGE_TITLE,
    )

    st.markdown(body=library_constants.PAGE_STYLE, unsafe_allow_html=True)


def initial_session_state() -> None:
    """
    Initial Session State Function
    """

    if "api_key" not in st.session_state:
        st.session_state.api_key = ""

    if "model_name" not in st.session_state:
        st.session_state.model_name = library_constants.MODELS[0]

    if "messages" not in st.session_state:
        st.session_state.messages = []

        # message_assistant = {
        #     "role": "assistant",
        #     "content": library_constants.FIRST_RESPONSE,
        # }

        # st.session_state.messages = [message_assistant]


def generate_sidebar_section() -> None:
    """
    Generate Sidebar Section Function
    """

    with st.sidebar:
        st.subheader(body="تنظیمات", divider="rainbow")

        st.session_state.model_name = st.radio(
            label="لطفا مدل خود را انتخاب نمایید:",
            options=library_constants.MODELS,
            index=0,
        ).strip()
        st.divider()

        st.write("مدل انتخاب شده:", st.session_state.model_name)
        st.divider()

        st.session_state.api_key = st.text_input(
            label="API Key", type="password"
        ).strip()
        st.divider()

        st.markdown(body=library_constants.PAGE_INFO, unsafe_allow_html=True)


if __name__ == "__main__":
    print("This file is a library file! So, you cannot run this file directly...")
