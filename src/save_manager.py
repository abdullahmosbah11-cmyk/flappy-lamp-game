import json
import os

class SaveManager:
    def __init__(self, filename="save_data.json"):
        self.filename = filename
        self.data = self.load()

    
    def load(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:return json.load(f)
            except Exception:
                pass

        return{"high_score": 0, "total_sparks": 0, "unlocked_flames": ["amber"], "selected_flame": "amber"}

    def save(self):
        with open(self.filename, "w") as f: json.dump(self.data, f, indent=4)

    def update_high_score(self, score):
        if score > self.data.get("high_score", 0):
            self.data["high_score"] = score
            self.save()

    def add_sparks(self, amount):
        self.data["total_sparks"] = self.data.get("total_sparks", 0) + amount
        self.save()

    def unlock_flame(self, flame_id, cost):

        if self.data.get("total_sparks", 0) >= cost:
            self.data["total_sparks"] -= cost
            if flame_id not in self.data.get("unlocked_flames", []):
                self.data.setdefault("unlocked_flames", []).append(flame_id)

            self.data["selected_flame"] = flame_id
            self.save()
            return True
        return False
    
    def select_flame(self, flame_id):
        if flame_id in self.data.get("unlocked_flames", []):
            self.data["selected_flame"] = flame_id
            self.save()
