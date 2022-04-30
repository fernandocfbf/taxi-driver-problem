def adjustRightLeft(steps):
    fix = [steps[0]]
    save_data = [steps[1], 1]
    for i in range(2, len(steps)):
        step = steps[i]
        if step != '':
            if (step == save_data[0]):
                save_data[1] += 1
            else:
                if(save_data[0] == 'left' or save_data[0] == 'right'):
                    fix += [save_data[0]] * (save_data[1]//2 + save_data[1] % 2)
                else:
                    fix += [save_data[0]] * save_data[1]
                save_data[0] = step
                save_data[1] = 1
    fix.append("dropoff")
    return fix
