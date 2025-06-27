import numpy as np
def cosine_similarity(query, bulk_vectors):
    """
    Calculate cosine similarity between a query vector and a list of bulk vectors.
    
    Args:
        query (np.ndarray): The query vector.
        bulk_vectors (np.ndarray): A 2D array where each row is a vector to compare against the query.
        
    Returns:
        np.ndarray: An array of cosine similarity scores for each vector in bulk_vectors.
    """

    if query.ndim == 1:
        query = query.reshape(1, -1)
    
    # Normalize query
    query_norm = np.linalg.norm(query)
    if query_norm == 0:
        return np.zeros(bulk_vectors.shape[0])
    
    # Compute dot product: shape (n_vectors, 1)
    dot_products = np.dot(bulk_vectors, query.T)
    
    # Compute norms of bulk vectors: shape (n_vectors,)
    bulk_norms = np.linalg.norm(bulk_vectors, axis=1)
    
    # Compute cosine similarities: shape (n_vectors,)
    similarities = dot_products.flatten() / (bulk_norms * query_norm)
    
    return similarities

def to_numpy(openai_respsonse):
    """
    Convert OpenAI response to a NumPy array.
    
    Args:
        openai_respsonse (list): A list of dictionaries containing 'embedding' keys.
        
    Returns:
        np.ndarray: A 2D NumPy array of embeddings.
    """
    
    return np.array([item['embedding'] for item in openai_respsonse['data']])