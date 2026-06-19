import streamlit as st

# st.hello()

# ------ Understanding Streamlit's re-execution model ------
st.title("Re-execution Demo")

name = st.text_input("Enter your name")

if name:
    st.write(f"Hello, {name}!")
else:
    st.write("Please type your name above.")

print("Script executed!")


# ============================================================================================================================


# ------ Using elements: title, header, subheader, markdown, text ------

st.title("This is a Title")
st.header("This is a Header")
st.subheader("This is a Subheader")

st.markdown("**Markdown** _is_ supported! [Visit Streamlit](https://streamlit.io)")
st.text("This is plain text")
st.write("`st.write()` can handle *mixed content*, like **bold**, _italic_, and numbers:", 123)


# ------ Displaying formatted text, code blocks, and LaTeX ------
st.markdown("### Code Block Example")
st.code("""
# Python example
def greet(name):
    return f"Hello, {name}!"
print(greet("Streamlit"))
""", language="python")

st.markdown("#### Inline LaTeX: $a^2 + b^2 = c^2$")
st.latex(r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}")

# ------ Showing feedback messages ------
st.success("This is a success message!")
st.warning("Be careful! This is a warning.")
st.error("Oops! Something went wrong.")
st.info("This is some information.")

# Adding a helpful tip:
st.markdown("> **Tip:** Use feedback messages to guide the user.")







# ============================================================================================================================





# ------ Basic interaction: button, radio, checkbox ------
import streamlit as st

if st.button("Click Me"):
    st.write("Button clicked!")

choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", choice)

agree = st.checkbox("I agree")
if agree:
    st.write("Thanks for agreeing!")

# Save and refresh.
# ------ streamlit run


# ------ Selectors: selectbox, multiselect ------
fruit = st.selectbox("Pick a fruit:", ["Apple", "Banana", "Orange"])
st.write("Your favorite fruit is:", fruit)

colors = st.multiselect("Pick some colors:", ["Red", "Green", "Blue", "Yellow"])
st.write("You chose:", colors)

# Save and refresh.
# ------ streamlit run


# ------ User inputs: slider, number input, text input, text area ------
age = st.slider("Select your age:", 0, 100, 25)
st.write("Age:", age)

number = st.number_input("Enter a number:", min_value=0, max_value=100, value=10)
st.write("Number:", number)

name = st.text_input("Enter your name:")
st.write("Hello,", name)

bio = st.text_area("Write a short bio:")
st.write("Your bio:", bio)

# Save and refresh.
# ------ streamlit run


# ------ Date and time pickers ------
date = st.date_input("Pick a date")
st.write("Selected date:", date)

time = st.time_input("Pick a time")
st.write("Selected time:", time)

# Save and refresh.
# ------ streamlit run


# ------ File uploader for reading external files ------
uploaded_file = st.file_uploader("Upload a text file", type=["txt"])

if uploaded_file is not None:
    content = uploaded_file.read().decode("utf-8")
    st.text_area("File Content", content, height=200)

# Save and refresh.
# ------ streamlit run