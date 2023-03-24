import random


class Activity:
    """Each activity has a name and description"""

    def __init__(self, name, description):  # name and description are strings
        self._name = name
        self._description = description

    def get_name(self):
        """Returns activity name"""
        return self._name

    def get_description(self):
        """Return activity description"""
        return self._description


class ActivityList:
    """List containing Activity objects"""

    def __init__(self):
        self._list_of_activities = []

    def add_activity(self, name, description):
        """Creates and adds Activity object to list_of_activities"""

        self._list_of_activities.append(Activity(name, description))

    #def delete_activity(self):

    def choose_activity(self):
        """Print random activity name and description from list_of_activities"""

        activity_object = random.choice(self._list_of_activities)
        print(f"{activity_object.get_name()}{chr(10)}{activity_object.get_description()}")


test = ActivityList()
test.add_activity("Horrible Chore", "Do one chore that you have been putting off")
test.add_activity("Walk", "Goi on a 20 minute walk outside")
test.add_activity("Read", "Take 15 minutes to read about a new topic")
test.add_activity("Clean", "Spend 15 minutes cleaning something you regularly ignore")
test.choose_activity()
