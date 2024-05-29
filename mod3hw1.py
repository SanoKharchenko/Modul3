
def single_root_words (root_world, *other_world):
    same_words = []
    root_world = root_world.lower()
    for i in other_world:
            i = i.lower()
            if root_world in i or i in root_world:
                same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
