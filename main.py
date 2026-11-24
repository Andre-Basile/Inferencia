from utils import load_content, wait
from pathlib import Path
from classes.inferencia import InferenceEngine


def ask_facts ():
    return {
        "étudiant",
        "inscrit_L3",
        "carte_valide"
    }

def main ():
    msg = "Welcome to Inferencia, the inference system for every one."
    print(f"\n\t {msg}\n\t {'-'*len(msg)}")
    wait(.5)
    
    rules_json_file_path = Path(__file__).parent / "rules" / "rules.json"
    rules = load_content(rules_json_file_path)
    facts = ask_facts()

    if rules == -1:
        print("\t Errno :> You don't have the json file that contains the rules.Create the file \"rules.json\" in the folder \"rules\"")
        return None
    
    # else
    # Inference
    inferencia = InferenceEngine(rules=rules)
    inferencia.infer(facts=facts)
    inferencia.resume(wait_callback_function=lambda x=1: wait(x))


if __name__ == "__main__":
    main()