class Persona:
    def __init__(self, name, level, fusions):
        self.name = name
        self.level = level
        self.fusions = fusions

    def description(self):
        return f"[{self.level:02d}] {self.name}"
    
    def fusion_recipes(self):
        msg = ""
        for i in range(len(self.fusions)):
            if len(self.fusions[i]) == 2:
                msg = msg + f"\n{i+1}. {self.fusions[i][0]} + {self.fusions[i][1]}"
            elif len(self.fusions[i]) == 3:
                msg = msg + f"\n{i+1}. {self.fusions[i][0]} + {self.fusions[i][1]} + {self.fusions[i][2]}"
            elif len(self.fusions[i]) == 4:
                msg = msg + f"\n{i+1}. {self.fusions[i][0]} + {self.fusions[i][1]} + {self.fusions[i][2]} + {self.fusions[i][3]}"
            elif len(self.fusions[i]) == 5:
                msg = msg + f"\n{i+1}. {self.fusions[i][0]} + {self.fusions[i][1]} + {self.fusions[i][2]} + {self.fusions[i][3]} + {self.fusions[i][4]}"
            else:
                return "There was an ERROR parsing the fusion recipes"     
        return msg