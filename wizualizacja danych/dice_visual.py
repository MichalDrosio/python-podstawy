from roll_die import Die
import pygal

die = Die()
die_2 = Die()

results = []
for roll_num in range(10000):
    result = die.roll() + die_2.roll()
    results.append(result)

print(results)

max_result = die.num_sides + die_2.num_sides
frequencies = []
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()
hist.force_uri_protocol = 'http'

hist.title = "Wyniki rzutu dwiema kościami 10000 razy"
hist.x_labels = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Wynik"
hist.y_title = "Częstotliwość występowania wartości"

hist.add('D6+D10', frequencies)
hist.render_to_file('dice_visual.svg')