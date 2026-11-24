class InferenceEngine:
    def __init__(self, rules):
        self.rules = rules
        self.conditions = [list(rule["conditions"]) for rule in rules]
        self.infer_yet = False
        self.start_infos = None
        self.inference_new_facts = None
        self.inference_informations = []

    def satisfy_condition (self, condition, facts):
        states = []
        for element in condition:
            states.append(element in facts)
        return all(states)
        
    def infer (self, facts):
        rules = self.rules
        self.start_infos = list(facts)
        informations = list(facts)
        for index, condition in enumerate(self.conditions):
            
            if (self.satisfy_condition(condition, facts)):
                informations.append(rules[index]["conclusion"])
                self.inference_informations.append(f"[{",".join(facts)}] helps me to decide that the subject has attributes : \"{"-".join(condition)}\"")
        self.inference_new_facts = informations
        self.infer_yet = True

    def resume (self, wait_callback_function=None):
        print()
        if not self.infer_yet:
            print("\t You didn't infer yet.")
            return None
        # ELSE
        message = "Resume of the informations gotten by application of rules to his facts."
        n = len(message) + 4
        if len(self.start_infos) < 2:
            print(f"\t (*_*):The subject has these facts : {",".join(self.start_infos)}")
        else:
            print(f"\t (*_*):The subject has these facts : {",".join(self.start_infos[:-1])} and {self.start_infos[-1]}")

        for element in self.inference_informations:
            print(f"\t\t Reasoning : {element}")
            if not wait_callback_function is None:
                wait_callback_function()
        
        print(f"\t (*_*): All of these helps me to come to this conclusion : <<the subject has \"{",".join(self.inference_new_facts)}\">>")            
        print()