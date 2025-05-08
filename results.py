import os


def text_open():
    # Specify the file name
    file_name = 'results.txt'

    # Check if the file exists
    if not os.path.isfile(file_name):
        # Create the file
        with open(file_name, 'w') as file:
            file.write("")
        print(f"File '{file_name}' created.")
    else:
        print(f"File '{file_name}' already exists.")


def text_make(score):
    with open('results.txt', 'r') as file:
        content = file.read().strip()
        if content:
            data = [float(num) for num in content.split()]
        else:
            data = []
        print(data)
        data.append(score)
        data.sort(reverse=True)
        klasyfikacja = data.index(score)
        data = data[:5]

    with open('results.txt', 'w') as file:
        file.write(' '.join(map(str, data)))
    text = ""
    awans = klasyfikacja < 5
    if awans:
        print('awans')
        text += f"\nWłaśnie zająłeś {klasyfikacja + 1} miejsce!"
    text +="\n\nRanking:\n"
    for i, value in enumerate(data, start=1):
        text += f"    {i}.    {int(value)} points\n"



    return text





