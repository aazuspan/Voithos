import json
import os
import shutil
from snips_nlu import SnipsNLUEngine, load_resources
from snips_nlu.default_configs import CONFIG_EN
from snips_nlu.exceptions import PersistingError
from Voithos.CommandHandler import CommandHandler


def main():
    """
    This builds a training dataset, trains an NLU engine with it, and saves that engine. This must be done any time a
    new command is added or utterances are edited for a command. If an NLU engine already exists, it is deleted.
    """
    training_json = json.loads(build_training_dataset())
    engine_path = os.path.join('Voithos', 'utilities', 'NLU')

    nlu_engine = SnipsNLUEngine(
        config=CONFIG_EN, resources=load_resources("snips_nlu_en"))
    nlu_engine = nlu_engine.fit(training_json)

    try:
        nlu_engine.persist(engine_path)
    except PersistingError:
        shutil.rmtree(engine_path)
        nlu_engine.persist(engine_path)


def build_training_dataset():
    """
    This uses utterance data from all Voithos commands to build a Json training dataset for use by SnipsNLU
    :return: A Json of training data built from all commands
    """
    cmd_handler = CommandHandler(voithos=None)
    cmd_dict = {"entities": {}, "intents": {}, "language": "en"}

    for cmd in cmd_handler.cmd_list:
        try:
            cmd_dict['intents'][cmd.name] = {"utterances": [{"data": []}]}

            for utterance in cmd.utterances:
                # This is a nightmare.
                cmd_dict['intents'][cmd.name]['utterances'][0]['data'].append(
                    {"text": utterance})
        except AttributeError:
            pass

    training_json = json.dumps(cmd_dict)

    return training_json


if __name__ == '__main__':
    main()
