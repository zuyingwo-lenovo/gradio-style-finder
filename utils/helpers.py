"""
Utility functions for the Style Finder application.
"""

def get_all_items_for_image(image_url, dataset):
    """
    Get all items related to a specific image from the dataset.
    
    Args:
        image_url (str): The URL of the matched image
        dataset (DataFrame): Dataset containing outfit information
        
    Returns:
        DataFrame: All items related to the image
    """
    return dataset[dataset['Image URL'] == image_url]

def format_alternatives_response(user_response, alternatives, similarity_score, threshold=0.8):
    """
    Append alternatives to the user response in a formatted way.
    
    Args:
        user_response (str): Original response from the model
        alternatives (dict): Dictionary of alternatives for each item
        similarity_score (float): Similarity score of the match
        threshold (float): Threshold for determining match quality
        
    Returns:
        str: Enhanced response with alternatives
    """
    if similarity_score >= threshold:
        enhanced_response = user_response + "\n\n## Learning Activity: Budget-Friendly Alternatives\n\nAs part of your learning exercise, here are some more affordable options for each item:\n"
    else:
        enhanced_response = user_response + "\n\n## Learning Activity: Similar Items from Market Research\n\nHere are some visually similar items we found through our market research process:\n"
    
    for item, alts in alternatives.items():
        enhanced_response += f"\n### {item}:\n"
        if alts:
            for alt in alts:
                enhanced_response += f"- {alt['title']} for {alt['price']} from {alt['source']} (Buy it here: {alt['link']})\n"
        else:
            enhanced_response += "- No alternatives found in our database.\n"
    
    # Add educational context
    enhanced_response += "\n\n## Course Reflection\n"
    enhanced_response += "This exercise demonstrates how computer vision and API integration can be combined to create practical fashion technology applications. Consider how this approach could be applied to other domains or with different data sources."
    
    return enhanced_response
