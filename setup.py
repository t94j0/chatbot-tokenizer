import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="discordtokenizer",
    version="0.0.1",
    author="Max Harley",
    author_email="maxh@maxh.io",
    description=
    "Tokenizer for discord.gg (also works on any other text-based messaging)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/t94j0/discord-tokenizer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
