# Pythone game Hangman/Stickman - words and stickman art
# Author: DusanB98
# Date: 4.9.2025

# Words to guess
words = (
    "aardvark", "albatross", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo", "asp",
    "baboon", "badger", "bandicoot", "barnacle", "bat", "bear", "beaver", "bee", "beetle", "binturong",
    "bird", "bison", "boar", "bobcat", "buffalo", "bull", "butterfly", "camel", "capybara", "caracal",
    "caribou", "cassowary", "cat", "caterpillar", "centipede", "chameleon", "cheetah", "chicken", "chimpanzee", "clam",
    "cockatoo", "cockroach", "cougar", "cow", "coyote", "crab", "crane", "crawfish", "cricket", "crocodile",
    "crow", "cuckoo", "deer", "dingo", "dog", "dolphin", "donkey", "dormouse", "dove", "dragonfly",
    "duck", "eagle", "earthworm", "echidna", "eel", "elephant", "elk", "emu", "ermine", "falcon",
    "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gazelle", "gecko", "gerbil",
    "gibbon", "giraffe", "goat", "goldfish", "goose", "gorilla", "grasshopper", "guinea pig", "gull", "hamster",
    "hare", "hawk", "hedgehog", "heron", "herring", "hippopotamus", "horse", "hummingbird", "hyena", "ibex",
    "ibis", "iguana", "impala", "jackal", "jaguar", "jay", "jellyfish", "kangaroo", "kingfisher", "kiwi",
    "koala", "komodo dragon", "kookaburra", "krill", "ladybug", "lemur", "leopard", "lion", "lizard", "llama",
    "lobster", "locust", "lynx", "macaw", "magpie", "manatee", "mandrill", "manta ray", "marmoset", "marmot",
    "meerkat", "mink", "mole", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt",
    "nightingale", "octopus", "opossum", "orangutan", "orca", "ostrich", "otter", "owl", "ox", "oyster",
    "panda", "panther", "parrot", "partridge", "peacock", "pelican", "penguin", "pheasant", "pig", "pigeon",
    "platypus", "porcupine", "porpoise", "possum", "prairie dog", "prawn", "puppy", "quail", "quokka", "rabbit",
    "raccoon", "ram", "rat", "raven", "reindeer", "rhinoceros", "roadrunner", "robin", "rooster", "salamander",
    "salmon", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrimp", "skunk", "sloth",
    "snail", "snake", "sparrow", "spider", "squid", "squirrel", "starfish", "stingray", "stork", "swan",
    "tapir", "tarantula", "termite", "tiger", "toad", "tortoise", "toucan", "turkey", "turtle", "urchin",
    "vulture", "wallaby", "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wombat", "woodpecker",
    "worm", "wren", "yak", "zebra"
)

# Dictionary for stickman art
stickman_art = {
    0: (
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        "),
    1: (
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "        ",
        "========"),
    2: (
        "│       ",
        "│       ",
        "│       ",
        "│       ",
        "│       ",
        "│       ",
        "========"),
    3: (
        "│‾‾‾‾‾‾ ",
        "│       ",
        "│       ",
        "│       ",
        "│       ",
        "│       ",
        "========"),
    4: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│        ",
        "│        ",
        "│        ",
        "│        ",
        "======== "),
    5: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│      O ",
        "│        ",
        "│        ",
        "│        ",
        "======== "),
    6: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│      O ",
        "│      | ",
        "│        ",
        "│        ",
        "======== "),
    7: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│      O ",
        "│     /| ",
        "│        ",
        "│        ",
        "======== "),
    8: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│      O ",
        "│     /|\\",
        "│        ",
        "│        ",
        "======== "),
    9: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│      O ",
        "│     /|\\",
        "│     /  ",
        "│        ",
        "======== "),
    10: (
        "│‾‾‾‾‾‾+ ",
        "│      │ ",
        "│      O ",
        "│     /|\\",
        "│     / \\",
        "│        ",
        "======== "),
}

