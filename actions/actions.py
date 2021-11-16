from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionReservationTime(Action):

    def name(self) -> Text:
        return "action_reservation_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        time = tracker.slots['Time']
        dispatcher.utter_message(text="{}に予約を完了しました！".format(time))

        return []
