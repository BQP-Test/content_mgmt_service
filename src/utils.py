import requests
import threading
import json

class NotifierClient(threading.Thread):
    def __init__(self, followers, articleid):
        super().__init__()
        self.followers = [i['email'] for i in followers] if followers else []
        self.article_id = articleid
        print(self.followers)
        self.url = "http://bqp-notify-service:6004"
        self.start()
        
        
    def run(self):
        try:
            print(self.followers)
            # Construct the URL with appropriate query parameters
            response = requests.post(f"{self.url}/send-email-new-post/", json={"receiver_email": self.followers, "article_id":self.article_id})
            if response.status_code == 200:
                print("Email sent successfully")
            else:
                print(f"Failed to send email, status code {response.status_code}")
            return response.json()
        except Exception as e:
            print(f"Failed to send email: {e}")
            return None
        
class UserProfileClient:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.url = "http://bqp-auth-profile-service:6001"
        
    def get_user_profile(self):
        try:
            profile = requests.get(f"{self.url}/users/me/{self.user_id}/").json()
            return profile
        except:
            return None