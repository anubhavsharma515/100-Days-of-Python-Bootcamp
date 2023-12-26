
with open('input/names/invited_names.txt', 'r') as f:
  names = [name.replace("\n", "") for name in f.readlines()]

with open('input/letters/starting_letter.txt') as f:
  sample_letter = f.read()

for name in names:
    with open(f'output/ready_to_send/{name}.txt', 'w') as f:
        f.write(sample_letter.replace('[Name]', name))
    print(f"{name}'s letter written")

