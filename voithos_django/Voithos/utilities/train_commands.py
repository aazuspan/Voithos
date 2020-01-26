import json
import os
from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN
from Voithos.CommandHandler import CommandHandler


def main():
    """
    This builds a training dataset, trains an NLU engine with it, and saves that engine. This must be done any time a
    new command is added or utterances are edited for a command.
    """
    training_json = json.loads(build_training_dataset())
    nlu_engine = SnipsNLUEngine(config=CONFIG_EN)
    nlu_engine = nlu_engine.fit(training_json)
    engine_path = os.path.join('Voithos', 'utilities', 'NLU')
    nlu_engine.persist(engine_path)


def build_training_dataset():
    """
    This uses utterance data from all Voithos commands to build a Json training dataset for use by SnipsNLU
    :return: A Json of training data built from all commands
    """
    cmd_handler = CommandHandler(voithos=None)
    cmd_dict = {'entities': {}, 'intents': {}, 'language': 'en'}

    for cmd in cmd_handler.cmd_list:
        try:
            cmd_dict['intents'][cmd.name] = {'utterances': [{'data': []}]}

            for utterance in cmd.utterances:
                # This is a nightmare.
                cmd_dict['intents'][cmd.name]['utterances'][0]['data'].append({'text': utterance})
        except AttributeError:
            pass

    training_json = json.dumps(cmd_dict)
    return training_json


if __name__ == '__main__':
    main()
