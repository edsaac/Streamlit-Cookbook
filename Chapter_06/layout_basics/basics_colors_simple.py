import streamlit as st


def main():
    st.set_page_config(layout="wide")

    st.title(":rainbow-background[Colors]")
    st.slider("st.slider", value=50)

    cols = st.columns(2)
    with cols[0]:
        "Primary button"
        st.button("st.button", type="primary", use_container_width=True)

    with cols[1]:
        "Secondary button"
        st.button("st.button", type="secondary", use_container_width=True)

    st.text_input("st.text_input")

    with st.sidebar:
        st.title("🐍 `st.sidebar`")


if __name__ == "__main__":
    main()
