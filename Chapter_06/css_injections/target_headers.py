import streamlit as st


def main():
    css = """
        <style>
        h1 {
            text-align: center;
        }

        h2 {
            text-align: end;
        }

        h3 {
            text-align: justify;
        }
        </style>
    """

    if st.toggle("Inject CSS"):
        st.html(css)

    with st.echo(code_location="below"):
        st.title("A centered title")

    with st.echo(code_location="below"):
        st.header("An end-aligned header")

    with st.echo(code_location="below"):
        st.subheader("A start-aligned subheader")


if __name__ == "__main__":
    main()
