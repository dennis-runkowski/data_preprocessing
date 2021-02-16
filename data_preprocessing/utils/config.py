"""Module for validating config.

In order to process data a validate config object
is required. The validate config method ensures all the require steps are
included and the steps are defined correctly.

    Example Usage:

    config = {
        "data_loader": {
            "type": "list",
            "batch_size": 10
        },
        "steps": [
            {
                "name": "normalize_text",
                "type": "lowercase"
            },
            {
                "name": "normalize_text",
                "type": "remove_stopwords"
            }
        ]
    }
    config = validate_config(config, log_level="DEBUG")
"""

import json

# Data Loaders
DATA_LOADER = {
    "csv": {
        "file_path": "str",
        "columns": {}
    },
    "list": {},
    "single_item": {}
}
PERMITTED_STEPS = {
    "steps": {
        "normalize_text": {
            "type": [
                "lowercase",
                "remove_digits",
                "remove_punctuation",
                "remove_urls",
                "remove_stopwords",
                "remove_whitespace",
                "expand_contractions",
                "remove_html",
                "porter_stemmer",
                "snowball_stemmer",
                "lemmatizer",
                "debugger_step",
                "expand_contractions",
                "custom_normalize",
            ]
        },
    }
}
PERMITTED_TOKENIZER = {
    "tokenizer": {
        "type": [
            "spaces",
            "spacy_word_tokenize",
            "nltk_word_tokenize",
            "nltk_regex"
        ]
    }
}
# If you use the key it must run before the value
STEP_ORDER = {
    "remove_html": [
        "remove_punctuation",
        "porter_stemmer",
        "snowball_stemmer",
        "lemmatizer"
    ],
    "remove_urls": [
        "remove_punctuation"
    ],
}
REQUIRED_PRE_STEPS = {
    "remove_stopwords": ["lowercase"],
    "expand_contractions": ["lowercase"]
}


def validate_config(config, log_level="INFO"):
    """Validate config passed.

    Ensure all the require steps are included and the steps are defined
    correctly. The default log_level for each step is set to the value defined
    in the log_level Arg.

    Args:
        config (obj): config object
        log_level (str): log level for each step

    Returns:
        The valid config object is returned. If there are errors, an error is
        raised.
    """
    config = _check_data_loader(config, log_level)
    config = _check_tokenizer(config, log_level)
    config = _check_normalize_text(config, log_level)
    return config


def _check_data_loader(config, log_level):
    """Check data loader config.

    Args:
        config (obj): config object
        log_level (str): log level for each step
    Returns:
        The valid config object is returned. If there are errors, an error is
        raised.
    """
    # Check that a data loader is defined and correct
    check_data_loader = config.get("data_loader")
    if not check_data_loader:
        raise KeyError(
            "You must define a data_loader key to define your data loader!"
        )

    # Get the data loader type
    check_data_config = config["data_loader"].get("type")
    if not check_data_config:
        raise KeyError("You must define the data loader type!")

    # Check the type is correct
    if check_data_config not in DATA_LOADER.keys():
        raise ValueError(
            "The data loader type {a} is not a supported loader. "
            "Please use one of the supported loaders {b}.".format(
                a=check_data_config,
                b=" ,".join([k for k in DATA_LOADER])
            )
        )
    # Check that the required config is provided for the data loader
    check_data_type = DATA_LOADER.get(check_data_config)
    for key, value in check_data_type.items():
        if not check_data_loader.get(key):
            raise KeyError(
                "The key {} is missing for this data loader!".format(key)
            )
        config_type = type(value)
        if not isinstance(check_data_loader.get(key), config_type):
            raise TypeError(
                "The value for {a} must be of type {b}".format(
                    a=key,
                    b=config_type
                )
            )
    # Preserve orginal data, default it is off
    check_preserve = check_data_loader.get("preserve_original")
    if check_preserve:
        config["data_loader"]["preserve_original"] = True
    else:
        config["data_loader"]["preserve_original"] = False

    # If the batch size is not set, add the default batch size of 10
    check_data_batch = check_data_loader.get("batch_size")
    if check_data_batch:
        if not isinstance(check_data_batch, int):
            raise TypeError("The batch must be of type int!")
    else:
        config["data_loader"]["batch_size"] = 10

    # Set the name key - this is to import the data loader module
    config["data_loader"]["name"] = "data_loader"

    # Set the log level
    if not config["data_loader"].get("log_level"):
        config["data_loader"]["log_level"] = log_level

    return config


def _check_tokenizer(config, log_level):
    """Check tokenizer config.

    Args:
        config (obj): config object
        log_level (str): log level for each step
    Returns:
        The valid config object is returned. If there are errors, an error is
        raised.
    """
    # Set the tokenizer to the default if not configured
    tokenizer = config.get("tokenizer")
    if not tokenizer:
        default_tokenizer = {
            "type": "nltk_regex",
            "name": "tokenizer",
            "log_level": log_level
        }
        config["tokenizer"] = default_tokenizer
    else:
        # Check the tokenizer name
        if tokenizer.get("name") not in PERMITTED_TOKENIZER:
            raise KeyError("{} is not a valid name!".format(
                    tokenizer.get("name")
                )
            )
        tok_name = tokenizer["name"]
        tok_type = tokenizer.get("type")
        if tok_type not in PERMITTED_TOKENIZER[tok_name]["type"]:
            raise KeyError("{} is not a valid type!".format(
                    tok_type
                )
            )

    if not config["tokenizer"].get("log_level"):
        config["tokenizer"]["log_level"] = log_level

    return config


def _check_normalize_text(config, log_level):
    """Check normalize text steps.

    Args:
        config (obj): config object
        log_level (str): log level for each step
    Returns:
        The valid config object is returned. If there are errors, an error is
        raised.
    """
    steps_validated = []
    if config.get("steps"):
        # Check the steps are a list
        if not isinstance(config["steps"], list):
            raise TypeError("The config steps must be a list.")

        for step in config["steps"]:
            step_name = step.get("name")
            step_type = step.get("type")
            if not step.get("log_level"):
                step["log_level"] = log_level

            # Check for key errors
            if not step_name or not step_type:
                raise KeyError("Please include the keys, name and type.")

            # Check if the step is valid
            if not PERMITTED_STEPS["steps"].get(step_name):
                raise KeyError(
                    "{} is not a valid step!".format(step_name)
                )

            # Check if the type is valid
            permitted_type = PERMITTED_STEPS["steps"][step_name]["type"]
            if step_type not in permitted_type:
                raise ValueError(
                    "{} is not a valid option in {}!".format(
                        step_type,
                        step_name
                    )
                )

            # Check to see if order matters with other steps
            steps_validated.append(step_type)
            if STEP_ORDER.get(step_type):
                for check in STEP_ORDER.get(step_type):
                    if check in steps_validated:
                        raise KeyError(
                            "The {} step can not run before the {}"
                            " step!".format(
                                check,
                                step_type
                            )
                        )
            # Check for steps that require other steps
            if REQUIRED_PRE_STEPS.get(step_type):
                for check in REQUIRED_PRE_STEPS.get(step_type):
                    if check not in steps_validated:
                        raise KeyError(
                            "The {} step requires the {}"
                            " as a previous step!".format(
                                step_type,
                                check
                            )
                        )

    else:
        raise KeyError("Please add steps to your config!")

    return config
