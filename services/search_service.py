# services/search_service.py
"""
Service for searching online products using SerpAPI.
This module handles extracting descriptions from the AI's response
and searching for similar products online.
"""

import re
from serpapi import GoogleSearch

class SearchService:
    """
    Handles online product searches using SerpAPI.
    """
    
    def __init__(self, api_key):
        """
        Initialize the search service with the SerpAPI key.
        
        Args:
            api_key (str): SerpAPI key for authentication
        """
        self.api_key = api_key
    
    def extract_item_descriptions(self, bot_response):
        """
        Extract item descriptions from the bot's response.
        
        Args:
            bot_response (str): The response from the model
            
        Returns:
            list: Dictionaries containing item names and detailed descriptions
        """
        # TODO: Create a regular expression pattern to extract item names and descriptions
        # Hint: Use re.compile with a pattern that matches the format:
        # **Item Name** is description.
        pattern = None  # YOUR CODE HERE

        # TODO: Initialize an empty list to store extracted descriptions
        descriptions = []
        
        # TODO: Find all matches in the bot response using the pattern
        # Hint: Use pattern.finditer to iterate through all matches
        # Extract item_name and description from each match
        # YOUR CODE HERE
        
        return descriptions
    
    def search_alternatives(self, descriptions, top_n=5):
        """
        Search for alternatives using Google Shopping via SerpAPI.
        
        Args:
            descriptions (list): Item descriptions extracted from the bot's response
            top_n (int): Number of top alternatives to return for each item
            
        Returns:
            dict: Item names mapped to lists of alternatives
        """
        # TODO: Initialize a dictionary to store alternatives for each item
        alternatives = {}
        
        print("\n Starting SerpAPI search for alternatives...\n")
        
        # TODO: Iterate through each item description
        for desc in descriptions:
            # TODO: Extract item name and create search query
            # Hint: Use the description to form a meaningful query
            item_name = None  # YOUR CODE HERE
            query = None  # YOUR CODE HERE
            
            # TODO: Set up SerpAPI parameters
            # Hint: Include the engine type, query, and API key
            params = None  # YOUR CODE HERE
            
            try:
                # TODO: Initialize the SerpAPI search and get results
                # Hint: Use GoogleSearch with the parameters
                search = None  # YOUR CODE HERE
                search_results = None  # YOUR CODE HERE
                
                # TODO: Extract and process shopping items
                # Hint: Use the _extract_shopping_results helper method
                shopping_items = None  # YOUR CODE HERE
                
                # TODO: Add the results to the alternatives dictionary
                # Hint: Limit to top_n items
                alternatives[item_name] = None  # YOUR CODE HERE
            except Exception as e:
                print(f"Error querying SerpAPI for {item_name}: {e}")
                alternatives[item_name] = []
        
        return alternatives
    
    def _extract_shopping_results(self, json_response):
        """
        Extract relevant shopping results from a JSON response.
        
        Args:
            json_response (dict): The JSON response from SerpAPI
            
        Returns:
            list: Dictionaries containing product details
        """
        # TODO: Get the shopping_results from the JSON response
        # Hint: Use .get() with a default empty list
        shopping_results = None  # YOUR CODE HERE
        
        # TODO: Initialize a list to store extracted results
        extracted_results = []
        
        # TODO: Iterate through each item in shopping_results
        # For each item, extract title, price, link, and source
        # Add these details to extracted_results
        # YOUR CODE HERE
        
        return extracted_results