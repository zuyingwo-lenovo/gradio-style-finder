# models/llm_service.py
"""
Service for interacting with the Llama 3.2 Vision Instruct model.
This module handles the communication with the AI model and
generates fashion-specific responses.
"""

from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters

class LlamaVisionService:
    """
    Provides methods to interact with the Llama 3.2 Vision Instruct model.
    """
    
    def __init__(self, model_id, project_id, region="us-south", 
                 temperature=0.2, top_p=0.6, api_key=None):
        """
        Initialize the service with the specified model and parameters.
        
        Args:
            model_id (str): Unique identifier for the model
            project_id (str): Project ID to associate the task
            region (str): Region for the watsonx AI service
            temperature (float): Controls randomness in generation
            top_p (float): Nucleus sampling parameter
            api_key (str, optional): API key for authentication
        """
        # TODO: Set up authentication credentials
        # Hint: Use the Credentials class with the region URL
        credentials = None  # YOUR CODE HERE
        
        # TODO: Initialize the API client
        # Hint: Use the APIClient class with the credentials
        self.client = None  # YOUR CODE HERE
        
        # TODO: Define parameters for the model's behavior
        # Hint: Use TextChatParameters with temperature and top_p
        params = None  # YOUR CODE HERE
        
        # TODO: Initialize the model inference object
        # Hint: Use ModelInference with model_id, credentials, project_id, and params
        self.model = None  # YOUR CODE HERE
    
    def generate_response(self, encoded_image, prompt):
        """
        Generate a response from the model based on an image and prompt.
        
        Args:
            encoded_image (str): Base64-encoded image string
            prompt (str): Text prompt to guide the model's response
            
        Returns:
            str: Model's response
        """
        try:
            # TODO: Create the messages object with text and image
            # Hint: The messages should include a user role with text and image content
            messages = None  # YOUR CODE HERE
            
            # TODO: Send the request to the model
            # Hint: Use the model.chat method with the messages
            response = None  # YOUR CODE HERE
            
            # TODO: Return the model's response
            # Hint: Extract the content from the first choice in the response
            return None  # YOUR CODE HERE
        except Exception as e:
            return f"Error generating response: {e}"
    
    def generate_fashion_response(self, user_image_base64, matched_row, all_items, 
                                 similarity_score, threshold=0.8):
        """
        Generate a fashion-specific response using role-based prompts.
        
        Args:
            user_image_base64: Base64-encoded user-uploaded image
            matched_row: The closest match row from the dataset
            all_items: DataFrame with all items related to the matched image
            similarity_score: Similarity score between user and matched images
            threshold: Minimum similarity for considering an exact match
            
        Returns:
            str: Detailed fashion response
        """
        # TODO: Generate a detailed list of items with prices and links
        # Hint: Use string join with a list comprehension over all_items
        items_description = None  # YOUR CODE HERE

        # TODO: Create different prompts based on similarity score
        # For high similarity (>= threshold), create a prompt for exact match
        # For low similarity (< threshold), create a prompt for closest match
        if similarity_score >= threshold:
            # TODO: Create assistant prompt for exact match
            # Hint: Include role definition, matched outfit details, and step-by-step instructions
            assistant_prompt = None  # YOUR CODE HERE
        else:
            # TODO: Create assistant prompt for closest match
            # Hint: Include role definition and instructions for analyzing the image
            assistant_prompt = None  # YOUR CODE HERE

        # Send the prompt to the model
        return self.generate_response(user_image_base64, assistant_prompt)