from functools import partial


def convert_choice(choice):
    return choice[0].lower() + choice[1:]


def doc_to_instruction(doc, connector):
    # following T0
    instruction = "Memilih alternatif yang paling masuk akal.\n\n"
    conn = connector[doc["question"]]
    return instruction + doc["premise"].strip()[:-1] + f" {conn}..." + f'\nA. {convert_choice(doc["choice1"])}\nB. {convert_choice(doc["choice2"])}'

def doc_to_label(doc):
    if doc["label"] == 0: 
        return "A"
    else: 
        return "B"


def doc_to_text(doc, connector):
    conn = connector[doc["question"]]
    return doc["premise"].strip()[:-1] + f" {conn}"


def doc_to_choice(doc):
    return [convert_choice(doc["choice1"]), convert_choice(doc["choice2"])]


doc_to_text_id = partial(
    doc_to_text,
    connector={
        "cause": "karena",
        "effect": "maka",
    },
)

doc_to_instruction_id = partial(
    doc_to_instruction,
    connector={
        "cause": "karena",
        "effect": "maka",
    },
)
