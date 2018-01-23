# Module messages

class SMS_Store():
    # Constructor
    def __init__(self):
        self.inbox = []

    # Function: Show inbox content
    def show_inbox(self):
        print("Inbox: ", self.inbox)

    # Function: Add new message
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        message = (False, from_number, time_arrived, text_of_SMS)
        self.inbox.append(message)
        return message

    # Function: Returns quantity of messages on inbox
    def message_count(self):
        return len(self.inbox)

    # Function: Returns a list of indexes of unread messages
    def get_unread_indexes(self):
        indexes = []
        for i in range(len(self.inbox)):
            if self.inbox[i][0] != True:
                indexes.append(i)
        return indexes

    # Function: Reads message and changes its status to True
    def get_message(self, i):
        if i in range(len(self.inbox)):
            from_number = self.inbox[i][1]
            time_arrived = self.inbox[i][2]
            text_of_SMS = self.inbox[i][3]
            self.delete(i)
            message_updated = (True, from_number, time_arrived, text_of_SMS)
            self.inbox.append(message_updated)
            return message_updated
        else:
            return None

    # Function: Deletes message by index
    def delete(self, i):
        if i in range(len(self.inbox)):
            self.inbox.pop(i)
            return True
        else:
            return None

    # Function: Clears inbox
    def clear(self):
        self.inbox.clear()
        return self.inbox


print("Starting execution...")
sms_store = SMS_Store()
print("Adding new messages")
print(sms_store.add_new_arrival("1000", "18:45", "Hello"))
print(sms_store.add_new_arrival("1001", "19:55", "World"))
print(sms_store.add_new_arrival("1003", "20:00", "Test"))
print("Messages on inbox:", sms_store.message_count())
print("Unread messages:", sms_store.get_unread_indexes())
print("Reading message:", sms_store.get_message(0))
print("Unread messages:", sms_store.get_unread_indexes())
sms_store.show_inbox()
print("Deleting message:", sms_store.delete(0))
print("Messages on inbox:", sms_store.message_count())
sms_store.show_inbox()
print("Deleting all messages:", sms_store.clear())
sms_store.show_inbox()
