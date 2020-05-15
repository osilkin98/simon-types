import time

import markovify


def get_text_model(filename: str, **kwargs) -> markovify.Text:
    with open(filename) as f:
        return markovify.Text(f, **kwargs)


def get_joint_model(filenames: list, weights: list = None, **kwargs) -> markovify.Text:
    models = [get_text_model(fn, **kwargs) for fn in filenames]
    model_combo = markovify.combine(models, weights)
    model_combo.compile()
    return model_combo


def get_sentences(model: markovify.Text, n=50, **kwargs):
    return [s for _ in range(n)if (s := model.make_sentence(**kwargs)) is not None]


def generate_sentances(model: markovify.Text, time_int: 0.5, **kwargs):
    while True:
        sent = model.make_sentence(**kwargs)
        while sent is None:
            sent = model.make_sentence(**kwargs)
        print(sent, end='\n' + '\n')
        time.sleep(time_int - 0.05)


if __name__ == '__main__':
    files = [
        "kitchen_nightmares.txt",
        "keil.txt",
        "joe chang.txt",
        "nathan_for_you.txt",
        "sopranos.txt",
        "family guy.txt",
        "superbad.txt",
        "arrested_development.txt"

    ]
    weights = [
        0.3,  # kitchen
        2, # keil
        0.2,     # joe
        1.2,     # nat
        0.1,  # sop
        1.1,   # family
        0.26,  # superbad
        1.5  # AD
    ]
    model = get_joint_model(files, weights, state_size=2, retain_original=False, well_formed=False)

    generate_sentances(model, time_int=2, max_words=50, max_overlap_ratio=0.7)