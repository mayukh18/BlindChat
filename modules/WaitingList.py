

class WaitingListDB:
    def __init__(self):
        self.waitList = []

    def get_match(self, gender, interest):
        print(self.waitList)
        for i in range(len(self.waitList)):
            user = self.waitList[i]
            if user["interest"] == gender or user["interest"] == "random":
                if user["gender"] == interest or interest == "random":
                    data = self.waitList.pop(i)
                    return data["id"]

        return None

    def enlist(self, id, gender, interest):
        data = {"id": id, "gender": gender, "interest": interest}
        self.waitList.append(data)



