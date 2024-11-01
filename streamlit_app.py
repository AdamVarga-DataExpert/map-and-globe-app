import streamlit as st

# Set the title and introductory content
st.title("Welcome to the Maps and Globes Fan Page!")
st.subheader("Explore the World Through Maps and Globes")
st.write("Dive into the fascinating world of geography! Learn about the differences between maps and globes and why they are so important in understanding our planet.")

# Sidebar navigation
st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose an option:", ["Home", "What are Maps?", "What are Globes?"])

# Home section
if option == "Home":
    st.write("### Home")
    st.write("Welcome to the home section of our fan page. Use the sidebar to learn more about maps and globes.")

# Maps section
elif option == "What are Maps?":
    st.write("### What are Maps?")
    st.write(
        "Maps are flat, two-dimensional representations of the Earth's surface or parts of it. "
        "They are incredibly versatile and can show various types of information such as topography, "
        "population density, weather patterns, and more. Maps are widely used in education, navigation, "
        "and for planning purposes."
    )
    st.image("https://en.wikipedia.org/wiki/Wikipedia:Featured_pictures/Diagrams,_drawings,_and_maps/Maps#/media/File:Shanghai_1935_S1_AMS-WO.jpg", 
             caption="Example of a world map")

# Globes section
elif option == "What are Globes?":
    st.write("### What are Globes?")
    st.write(
        "A globe is a three-dimensional, spherical representation of the Earth. "
        "Unlike maps, globes provide an accurate depiction of the distances and relationships between locations "
        "because they maintain the Earth's true shape. They are especially useful for understanding global concepts, "
        "such as how the Earth rotates and how latitude and longitude work."
    )
    st.image("https://upload.wikimedia.org/wikipedia/commons/e/e4/Globe.png?20121115034505", 
             caption="Example of a globe")

# Footer
st.write("---")
st.write("Created with ❤️ for a test")
