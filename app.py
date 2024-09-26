"""
Streamlit app to find recipes based on ingredients using the Spoonacular API.
"""

import streamlit as st
import requests

API_KEY = "3a0aaf1dccae480c9da6d06e1ea617d4"

def get_recipes(ingredient_list):
    """
    Fetch recipes based on the given ingredients.
    
    Args:
        ingredient_list (str): Comma-separated list of ingredients.
    
    Returns:
        dict: JSON response from the Spoonacular API.
    """
    url = (
        f"https://api.spoonacular.com/recipes/findByIngredients"
        f"?ingredients={ingredient_list}&number=5&apiKey={API_KEY}"
    )
    response = requests.get(url, timeout=10)
    return response.json()

def main():
    """
    Main function to render the Streamlit app.
    """
    st.title("Recipe Finder")

    ingredients_input = st.text_input("Enter ingredients (comma separated)")

    if st.button("Search"):
        if ingredients_input:
            recipes = get_recipes(ingredients_input)

            if recipes:
                for recipe in recipes:
                    st.subheader(recipe['title'])
                    st.image(recipe['image'])

                    st.write("**Missing Ingredients:**")
                    for ingredient in recipe['missedIngredients']:
                        st.write(
                            f"{ingredient['name'].capitalize()} - "
                            f"{ingredient['amount']} {ingredient['unit']}"
                        )
                        st.image(ingredient['image'])
            else:
                st.write("No recipes found.")
        else:
            st.write("Please enter some ingredients.")

if __name__ == "__main__":
    main()
