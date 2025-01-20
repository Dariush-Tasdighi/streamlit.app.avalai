import streamlit as st

import library_constants
import library_streamlit
import library_functions


def main() -> None:
    library_streamlit.set_page_config()
    library_streamlit.initial_session_state()
    library_streamlit.generate_sidebar_section()

    st.subheader(body=library_constants.PAGE_HEADER, divider="rainbow")

    if not st.session_state.model_name:
        st.error(body="لطفا برای انجام عملیات، مدل خود را انتخاب نمایید!")

    if not st.session_state.api_key:
        st.error(body="لطفا برای انجام عملیات، API Key خود را وارد نمایید!")

    if st.session_state.api_key and st.session_state.model_name:
        user_prompt = st.chat_input(
            placeholder=library_constants.CHAT_INPUT_PLACEHOLDER
        )

        if user_prompt:
            st.session_state.messages.append({"role": "user", "content": user_prompt})
            response = library_functions.get_response(
                query=user_prompt,
                api_key=st.session_state.api_key,
                model_name=st.session_state.model_name,
            )
            st.session_state.messages.append({"role": "assistant", "content": response})

        for _, message in enumerate(st.session_state.messages):
            if message["role"] == "user":
                with st.chat_message(name="Human"):
                    st.write(message["content"])
            elif message["role"] == "assistant":
                with st.chat_message(name="AI"):
                    st.write(message["content"])


if __name__ == "__main__":
    main()
