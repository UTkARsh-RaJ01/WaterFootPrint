import streamlit as st

def run():
    def about_page():
        st.title("About Water Footprint")

        
        col1, col2 = st.columns(2)

       
        with col1:
            st.header("What is Water Footprint?")
            st.write(
                "The water footprint is a measure of the amount of freshwater used to produce goods and services. "
                "It accounts for the water consumed during the entire supply chain, from production to consumption. "
                "Water footprint can be categorized into three types: "
            )

            st.subheader("Types of Water Footprint")
            st.write(
                "- **Blue Water Footprint**: The volume of freshwater consumed from surface and groundwater resources. "
                "It is primarily related to irrigation and industrial processes.\n"
                "- **Green Water Footprint**: The volume of rainwater stored in the soil that is used for crop production. "
                "This is important for agricultural activities.\n"
                "- **Grey Water Footprint**: The amount of freshwater required to dilute pollutants in water bodies to maintain water quality standards."
            )

       
        with col2:
            st.image("quality.png", caption="Water Usage and Footprint", use_column_width=True)

        st.header("Why is Water Footprint Important?")

        
        col3, col4 = st.columns(2)

        with col3:
            st.write(
                "Understanding the water footprint is crucial for several reasons:\n"
            )
            
            st.markdown(
                """
                1. **Resource Management**: It helps in assessing and managing freshwater resources effectively to prevent scarcity.
                2. **Sustainability**: By understanding the water footprint, individuals and businesses can make more sustainable choices.
                3. **Environmental Protection**: It aids in minimizing the impact on ecosystems and biodiversity by understanding how much water is used and polluted.
                4. **Informed Decision Making**: Knowledge of water footprints allows consumers to choose products that are less water-intensive, promoting water conservation.
                5. **Policy Development**: Governments and organizations can formulate policies and strategies for water conservation and sustainable use based on water footprint data.
                """
            )

       
        with col4:
            st.image("ecology.png", caption="Importance of Water Footprint", use_column_width=True)  # Update the path to your image

       
        st.header("Conclusion")
        st.write(
            "In a world where water scarcity is becoming an increasing concern, understanding and reducing our water footprint is vital. "
            "By making informed choices and understanding our impact on freshwater resources, we can work towards a more sustainable future."
        )

    
    about_page()


if __name__ == "__main__":
    run()
