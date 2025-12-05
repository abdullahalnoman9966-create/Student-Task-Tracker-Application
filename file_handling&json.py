
import json

def save_to_file(self):
        data = [task.to_dict() for task in self.tasks]
        with open("tasks.json","w") as f:
            json.dump(data,f, indent=4)
        print("Saved to JSON file!\n")

def load_from_file(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for item in data:
                    task = task (
                        item["id"],
                        item["title"],
                        item["description"],
                        item["created_at"]
                    )
                    self.tasks.append(task)
        except FileNotFoundError:
            print("JSON file not found, creating a new one...\n")
        except json.JSONDecodeError:
            print("JSON file corrupted!\n")