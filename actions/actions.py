# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017")
DB=client["Canteen"]
TRajColl=DB["Yamuna"]
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        breakFast = TRajColl.find({"_id":1})
        c=1
        for i in breakFast:
            item = i["item"+str(c)]
            dispatcher.utter_message(item)
            c=c+1
            
#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.events import SlotSet
#from rasa_sdk.executor import CollectingDispatcher

#class ActionSetChosenCanteen(Action):
#    def name(self) -> Text:
#        return "action_set_chosen_canteen"

#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        chosen_canteen = next(tracker.get_latest_entity_values("canteen_name"), None)
        
#        if chosen_canteen:
#            dispatcher.utter_message(text="Great choice! You've chosen the {} Canteen for your order.".format(chosen_canteen))
#            return [SlotSet("chosen_canteen", chosen_canteen)]
#        else:
#            dispatcher.utter_message(text="I'm sorry, I didn't catch which canteen you chose.")
#            return []

#from typing import Any, Text, Dict, List
#from rasa_sdk import Action, Tracker
#from rasa_sdk.executor import CollectingDispatcher
#import pymongo

#class ActionShowMenu(Action):
#    def name(self) -> Text:
#        return "action_show_menu"
#
#    def run(self, dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        # Connect to MongoDB
#        client = pymongo.MongoClient("mongodb://localhost:27017/")
#        db = client["your_database_name"]
#        
#        # Get the chosen canteen from the slot
#        chosen_canteen = tracker.get_slot("chosen_canteen")
#        
#       # Fetch the menu from the database
#       menu_collection = db["menu_collection_name"]
#        menu_data = menu_collection.find_one({"canteen": chosen_canteen})
#        
#        if menu_data:
#            menu_items = menu_data.get("menu_items", [])
#            if menu_items:
#                menu_response = "\n".join(menu_items)
#                dispatcher.utter_message(text=f"Here's the menu for {chosen_canteen}:\n{menu_response}")
#            else:
#                dispatcher.utter_message(text=f"Apologies, but it seems like the menu for {chosen_canteen} is not available.")
#        else:
#            dispatcher.utter_message(text="I'm sorry, I couldn't find the menu for the selected canteen.")
#        
#        return []

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pymongo

class ActionShowMenu(Action):
    def name(self) -> Text:
        return "action_show_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Connect to MongoDB
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["canteen_db"]  # Change to your database name
        
        # Get the chosen canteen from the slot
        chosen_canteen = tracker.get_slot("chosen_canteen")
        
        # Fetch the menu from the database
        menu_collection = db["north canteen"]  # Change to your collection name
        menu_data = menu_collection.find_one({"canteen": chosen_canteen})
        
        if menu_data:
            menu_items = menu_data.get("menu_items", [])
            if menu_items:
                menu_response = "\n".join([f"{item['item']} - ${item['price']:.2f}" for item in menu_items])
                dispatcher.utter_message(text=f"Here's the menu for {chosen_canteen}:\n{menu_response}")
        else:
                dispatcher.utter_message(text=f"Apologies, but it seems like the menu for {chosen_canteen} is not available.")
         else:
                dispatcher.utter_message(text="I'm sorry, I couldn't find the menu for the selected canteen.")
        
        return []


