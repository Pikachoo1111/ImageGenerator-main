import requests

url = "https://api.edenai.run/v2/image/generation"
payload = {
    "response_as_dict": True,
    "attributes_as_list": False,
    "show_original_response": False,
    "resolution": "256x256",
    "num_images": 1,
    "providers": "replicate",
    "text": "Modern looking Airplane in the sky where you can actually see the plane in the view."
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiM2E2ZWU5NDYtYTU5My00YjA1LWE2M2EtZTI5MjFkMTlmMTZiIiwidHlwZSI6ImFwaV90b2tlbiJ9.yPfMiy9XhPEQxrhfWkieTioX4MfopwjWdF_6Bu23Rac"
}

response = requests.post(url, json=payload, headers=headers)




def remove_text_before_keyword(text, keyword):
    # Split the text based on the keyword
    parts = text.split(keyword, 1)
    
    # If the keyword is found, return the portion after the keyword without the keyword itself
    if len(parts) > 1:
        return parts[1]
    else:
        return text

# Example usage


def remove_text_after_keyword(text, keyword):
    # Find the index of the keyword in the text
    keyword_index = text.find(keyword)
    
    # If the keyword is found, return the portion of text before the keyword
    if keyword_index != -1:
        return text[:keyword_index]
    else:
        return text
new_text = remove_text_before_keyword(response.text, '"image_resource_url":"')
new_text = remove_text_after_keyword(new_text, '"}],"cost":')
# Example usage


print(new_text)