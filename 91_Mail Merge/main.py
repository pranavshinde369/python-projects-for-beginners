PLACEHOLDER = "[names]"


with open("./Input/Names/invited_names.txt") as names_file:
    names =names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_files:
    letter_contents = letter_files.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)