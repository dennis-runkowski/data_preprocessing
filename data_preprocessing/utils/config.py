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
        }
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

    # Set the tokenizer to the default if not configured
    if not config.get("tokenizer"):
        default_tokenizer = {
            "type": "nltk_regex",
            "name": "tokenizer",
            "log_level": log_level
        }
        config["tokenizer"] = default_tokenizer

    if not config["tokenizer"].get("log_level"):
        config["tokenizer"]["log_level"] = log_level

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
            # Snowball Stemmer can accept options - default is english
            if step_type == "snowball_stemmer":
                options = step.get("options", "english")
                supported_lang = [
                    "arabic",
                    "danish",
                    "dutch",
                    "english",
                    "finnish",
                    "french",
                    "german",
                    "hungarian",
                    "italian",
                    "norwegian",
                    "porter",
                    "portuguese",
                    "romanian",
                    "russian",
                    "spanish",
                    "swedish"
                ]
                if options not in supported_lang:
                    raise ValueError(
                        "This is not a supported language, please use choose "
                        "from the supported languages: {}".format(
                            supported_lang
                        )
                    )

            # Remove stopwords can accept options - default is short_list
            if step_type == "remove_stopwords":
                options = step.get("options", "short_list")
                if options not in ["short_list", "long_list", "custom"]:
                    raise ValueError(
                        "The remove stopwords options can only accept "
                        "short_list or long_list!"
                    )
                if options == "custom" and not step.get("custom_list"):
                    raise KeyError(
                        "Please add the custom list to your config with the "
                        "custom_list key!"
                    )
                step["options"] = options

            # Custom Step needs custom_path
            if step_type == "custom_normalize":
                if not step.get("custom_module"):
                    step["custom_module"] = "custom_step"

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
