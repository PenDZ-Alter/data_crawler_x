import os
import dotenv

class Data() : 
    def __init__(self) : 
        dotenv.dotenv_values("../.env")
        dotenv.load_dotenv()
        
        self.api_key = os.getenv("API_KEY") or ""
        self.api_secret = os.getenv("API_SECRET") or ""
        self.access_token = os.getenv("ACCESS_TOKEN") or ""
        self.access_secret = os.getenv("ACCESS_SECRET") or ""
        self.bearer_token = os.getenv("BEARER_TOKEN") or ""
    
    def get_api(self) : 
        return self.api_key, self.api_secret
    
    def get_access(self) : 
        return self.access_token, self.access_secret
    
    def get_bearer(self) :
        return self.bearer_token
